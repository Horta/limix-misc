import numpy as np
from numba import jit

def isint_alike(arr):
    return np.all(arr == np.asarray(arr, int))

def _iscrescent(arr):
    i = 0
    while i < arr.shape[0]-1:
        if arr[i] > arr[i+1]:
            return False
        i += 1
    return True

def iscrescent(arr):
    arr = np.asarray(arr)
    return _iscrescent(arr)
