import cython

import numpy as np
cimport numpy as cnp
cnp.import_array()

DTYPE = np.float32
ctypedef cnp.float32_t DTYPE_t

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef DTYPE_t test(cnp.ndarray[DTYPE_t, ndim=2] grid):
    cdef int x_size = grid.shape[1]
    cdef int y_size = grid.shape[0]
    cdef DTYPE_t result = 0

#    cdef list x_order = range(x_size)
#    cdef list y_order = range(y_size)
#    np.random.shuffle(x_order)
#    np.random.shuffle(y_order)

    cdef int x,y

    for x in range(x_size):
        for y in range(y_size):
            if grid[(y, x)] > result:
                result = grid[(y, x)]
    return result
