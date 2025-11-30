def sum_of_squares(int n):
    cdef long long result = 0
    cdef int i
    for i in range(1, n + 1):
        result += i * i
    return result