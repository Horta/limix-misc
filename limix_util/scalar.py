import numpy as np

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def asfloat(value):
    if isfloat(value):
        return value
    return np.asscalar(value, float)
