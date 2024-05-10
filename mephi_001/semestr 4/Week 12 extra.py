import math

import numpy as np


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def find_max_factorial():
    n = 0
    while 1:
        try:
            factorial(n)
            n += 1
        except RecursionError:
            return n - 1




max_factorial = find_max_factorial()
print(f"Максимальное число, при котором работает функция factorial(): {max_factorial}")

x_values = [1, 10]


def exp_reversed_summ(x, n=100):
    sum = 1.0
    for i in range(n, 0, -1):
        sum = 1 + x * sum / i
    return sum

#
# large_x_values = [10, 100, 200]
# nmax = 1000
# for x in large_x_values:
#     exp_value = exp_reversed_summ(x, nmax)
#     print(f"exp({x}) with nmax={nmax}: {exp_value}")
#     print(f"math.exp({x}) = {math.exp(x)}")
#     print(f"Error {(abs(exp_value - math.exp(x))) / math.exp(x)}")
#     print()
#

def matrix_exp(A, n=100):
    I = np.eye(A.shape[0])  # единичная матрица
    term = I
    result = term

    for i in range(1, n + 1):
        term = np.matmul(A, term) / i
        result = term + result

    return result



def matrix_exp(A, n=100):
    I = np.eye(A.shape[0])  # единичная матрица
    term = I
    result = term


    sum = 1.0
    for i in range(n, 0, -1):
        result = 1 + np.matmul(A, term)  * result / i

    return result

M1 = np.array([[0, 1], [1, 0]])
print(matrix_exp(M1))


'''
import sys


print(sys.getrecursionlimit())
sys.setrecursionlimit(1500)
'''