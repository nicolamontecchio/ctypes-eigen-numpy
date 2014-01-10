#!/usr/bin/env python

import ctypes as C
import numpy as np

if __name__ == '__main__':
    print 'testing'
    a = np.array(np.random.random(45), dtype=np.float32)
    lib = C.CDLL('libeigentestpy.dylib')
    f_eigen_sum = lib.sum_float_numpy_array
    f_eigen_sum.argtypes = [np.ctypeslib.ndpointer(dtype = np.float32), C.c_int]
    f_eigen_sum.restype = C.c_float
    print 'python says sum is:', a.sum()
    print 'eigen instead says:', f_eigen_sum(a, len(a))

    print

    a = np.array([[1,5,23,21],
                  [3,-2,11,4],
                  [4,21,-44,-23],
                  [-12,11,10,4]], dtype=np.float32)
    ata = np.dot(a.T, a)
    print ata
    print np.max(np.abs(np.linalg.eig(ata)[0]))
    f_eigen_maxabseig = lib.biggest_abs_eigenvalue
    f_eigen_maxabseig.argtypes = [np.ctypeslib.ndpointer(dtype = np.float32), C.c_int]
    f_eigen_maxabseig.restype = C.c_float
    print f_eigen_maxabseig(ata, ata.shape[0])
