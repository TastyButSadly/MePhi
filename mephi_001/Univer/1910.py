import numpy as np
A = [[6, 4, -1],
     [5, 2, -7],
     [-4, 5, 1]]

B = [[6, 4, 7],
     [5, -7, 1],
     [8, 1, -3]]

a = 58
result_a = [[0] * 3 for _ in range(3)]  # создание пустой матрицы
for i in range(3):
    for j in range(3):
        result_a[i][j] = A[i][j] * a  # умножение на а

result_b = [[0] * 3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        result_b[i][j] = A[i][j] * B[i][j]  # поэлементное умножение матриц

result_c = [[0] * 3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        result_c[i][j] = B[i][j] / A[i][j] - A[i][j] * B[i][j]  # B/A - A × B

result_A = A * a
result_B = np.dot(A, B)
result_C = np.dot(B, np.linalg.inv(A)) - np.dot(A, B)
print("Специальный оператор:\n")
print("Результат умножения матрицы A на число a:", result_A)
print("\nРезультат поэлементного умножения матриц A и B: \n", result_B)
print("\nРезультат (c) - B/A - A × B по правилам линейной алгебры:\n", result_C)
print("\nЧерез цикл:\n")
print("Результат умножения матрицы A на число a:")
for i in result_a:
    print(i)

print("\nРезультат поэлементного умножения матриц A и B:")
for i in result_b:
    print(i)

print("\nРезультат  B/A - A × B:")
for i in result_c:
    print(i)