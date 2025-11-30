def dot_product(list a, list b):
    cdef int n = len(a)
    cdef double result = 0.0
    cdef int i
    for i in range(n):
        result += a[i] * b[i]
    return result