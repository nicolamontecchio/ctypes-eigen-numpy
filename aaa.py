#!/usr/bin/env python

import ctypes as C
import numpy as np

if __name__ == '__main__':
    print 'testing'
    a = np.array(np.random.random(45), dtype=np.float32)
    lib = C.CDLL('libeigentestpy.dylib')
    f_load_index = lib.sum_float_numpy_array
    f_load_index.argtypes = [np.ctypeslib.ndpointer(dtype = np.float32), C.c_int]
    f_load_index.restype = C.c_float
    print 'python says sum is:', a.sum()
    print 'eigen instead says:', f_load_index(a, len(a))


