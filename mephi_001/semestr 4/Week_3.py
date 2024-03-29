import sys
import numpy as np


def gauss(a, b):
    n = len(b)
    for k in range(n - 1):
        for i in range(k + 1, n):
            if a[i, k] != 0.0:
                lam = a[i, k] / a[k, k]
                a[i, k + 1:] = a[i, k + 1:] - lam * a[k, k + 1:]
                b[i] = b[i] - lam * b[k]

    for k in range(n - 1, -1, -1):
        b[k] = (b[k] - np.dot(a[k, k + 1:], b[k + 1:])) / a[k, k]
    return b


a = np.array([[np.pi ** 0.5, 3.0, -1.0],
              [8.0, np.exp(- 2 ** 0.5), -3.0],
              [1/3, 1.0, -5.0]])
b = np.array([i for i in map(float, input().split())])
a_r = []
for i in range(0, 3):
    a_r.append([])
    for j in range(0, 3):
        a_r[i].append(a[i][j])
    a_r[i].append(b[i])
a_r = np.array(a_r)

if np.linalg.matrix_rank(a_r) != np.linalg.matrix_rank(a) == 3:
    print('Не совместна')
    sys.exit()
a_orig = a.copy()
b_orig = b.copy()

x = gauss(a, b)

# print("A =\n", a)
print("x =\n", x)

if np.allclose(np.dot(a_orig, x), b_orig):

    print(np.dot(a_orig, x), b_orig)
    print("True")
else:
    print('False')
