# import numpy as np
# from numpy import concatenate as conc
# from numpy import newaxis
# import dask.array as da
#
# def hstack_row_read(Xs):
#     n = Xs[0].shape[0]
#     p = sum(X.shape[1] for X in Xs)
#
#     size = 1024**3 // 4
#     row_step = size // (8 * p)
#     row_step = min(max(row_step, 1), n)
#     print(row_step)
#
#     def row_stack(r, Xs):
#         left = r * row_step
#         right = min(left + row_step, n)
#         return np.hstack([X[left:right,:] for X in Xs])
#
#     dsk = {('x', r, 0): (row_stack, r, Xs) for r in range(n)}
#
#     row_chunks = [row_step,]*(n // row_step)
#     if n % row_step:
#         row_chunks.append(n % row_step)
#     row_chunks = tuple(row_chunks)
#
#     chunks = (row_chunks, (p,))
#
#     X = da.Array(dsk, name='x', chunks=chunks, dtype=float)
#     return X
#
# def hstack_col_read(Xs):
#     n = Xs[0].shape[0]
#     p = sum(X.shape[1] for X in Xs)
#
#     size = 1024**3
#     col_step = size // (8 * p)
#     col_step = min(max(col_step, 1), p)
#     print(col_step)
#
#     def col_stack(c, Xs):
#         c = c * col_step
#         col = None
#         for (ii, X) in enumerate(Xs):
#             if c < X.shape[1]:
#                 left = c
#                 right = left + col_step
#                 if right < X.shape[1]:
#                     col = X[:,left:right]
#                 else:
#                     Xn = Xs[ii+1]
#                     right = min(right-X.shape[1], Xn.shape[1])
#                     col = np.concatenate([X[:,left:], Xn[:,:right]])
#                 break
#             c -= X.shape[1]
#         return col[:,newaxis]
#
#     col_chunks = [col_step,]*(p // col_step)
#     if p - len(col_chunks)*col_step > 0:
#         col_chunks.append(p - len(col_chunks)*col_step)
#     col_chunks = tuple(col_chunks)
#
#     chunks = ((n,), col_chunks)
#     print(chunks)
#
#     dsk = {('x', 0, c): (col_stack, c, Xs) for c in range(len(col_chunks))}
#
#     X = da.Array(dsk, name='x', chunks=chunks, dtype=float)
#     return X
#
#
# def hstack_row_read2(filename, paths):
#     import h5py
#     with h5py.File(filename, 'r') as f:
#         n = f[paths[0]].shape[0]
#         p = sum(f[path].shape[1] for path in paths)
#
#     def row_stack(r, filename, paths):
#         with h5py.File(filename, 'r') as f:
#             return conc([f[path][r,:] for path in paths])[newaxis, :]
#
#     dsk = {('x', r, 0): (row_stack, r, filename, paths) for r in range(n)}
#     chunks = ((1,)*n, (p,))
#     X = da.Array(dsk, name='x', chunks=chunks, dtype=float)
#     return X
#
# def hstack_col_read2(filename, paths):
#     import h5py
#     with h5py.File(filename, 'r') as f:
#         n = f[paths[0]].shape[0]
#         p = sum(f[path].shape[1] for path in paths)
#
#     def col_stack(c, filename, paths):
#         col = None
#         with h5py.File(filename, 'r') as f:
#             for path in paths:
#                 if c < f[path].shape[1]:
#                     col = f[path][:,c]
#                     break
#                 c -= f[path].shape[1]
#         return col[:,newaxis]
#
#     dsk = {('x', 0, c): (col_stack, c, filename, paths) for c in range(p)}
#     chunks = ((n,), (1,)*p)
#     X = da.Array(dsk, name='x', chunks=chunks, dtype=float)
#     return X
