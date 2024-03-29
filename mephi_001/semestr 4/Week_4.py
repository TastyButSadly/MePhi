import numpy as np

A = np.array([[7, 8, 0],
              [0, 0.12, -3.5],
              [0.5, -10, 2]])
x = np.array([0, 5, -15])

s_values, s_vectors = np.linalg.eig(A)
print("Собственные значения матрицы A:")
print(s_values, '\n')
print("Собственные вектора матрицы A:")
print(s_vectors, '\n')

# for value, vector in zip(s_values, s_vectors):
#     print(np.allclose(np.dot(A, vector), np.dot(value, vector)))

for i in range(len(s_values)):
    lambda_i = s_values[i]
    v_i = s_vectors[:, i]

    if np.allclose(np.dot(A, v_i), lambda_i * v_i):
        print(f"Собственный вектор {i + 1} верен.")
    else:
        print(f"Собственный вектор {i + 1} неверен.")

coefficients = np.linalg.solve(s_vectors, x)
reconstr_x = np.dot(s_vectors, coefficients)

print("\nКоэффициенты разложения")
print(coefficients)
print("\nВосстановленный вектор x")
print([i.real for i in reconstr_x])

print(np.allclose(reconstr_x, x))
