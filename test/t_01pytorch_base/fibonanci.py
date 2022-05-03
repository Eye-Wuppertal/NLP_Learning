# def fib(n):
#     # base case
#     if n < 3:
#         return 1
#     return fib(n - 2) + fib(n - 1)

import numpy as np


def fib(n):
    tmp = np.zeros(n)
    tmp[0] = 1
    tmp[1] = 1
    for i in range(2, n):
        tmp[i] = tmp[i-2] + tmp[i-1]
    return tmp[n-1]


print(fib(70))
