import numpy as np
import matplotlib.pyplot as plt

R = 4.56 / 100  # cm to m
rho = 2700  # density of aluminium
I_exact = 0.4 * rho * (4 / 3) * np.pi * R ** 5  # exact moment of inertia


def f(theta):
    return rho * (R * np.sin(theta)) ** 2 * (R * np.sin(theta)) ** 2 * R * np.cos(theta)


def triangle_rule(f, a, b, N):
    # h = (b - a) / N
    # return sum(f(a + i * h) * h for i in range(N))

    h = (b - a) / N

    integral = 0.0
    for i in range(N):
        x_i = a + i * h
        x_i_plus_1 = x_i + h
        y_i = f(x_i)
        y_i_plus_1 = f(x_i_plus_1)

        triangle_area = 0.5 * h * (y_i + y_i_plus_1)
        integral += triangle_area
    return integral


def trapezoid_rule(f, a, b, N):
    # dx = (a - b) / N
    # area = 0
    # x = a
    # for i in range(N):
    #     area += dx * (f(x) + f(x + dx)) / 2
    #     x += dx
    # return area
    result = 0
    h = (a - b) / N
    for i in range(1, N):
        x = h * i
        result = result + f(x)
    result = h * (result + (f(0) + f(b)) / 2)

    return result


def simpsons_rule(f, a, b, N):
    # h = (b - a) / N
    # return h / 3 * (f(a) + f(b) + 4 * sum(f(a + (2 * i - 1) * h) for i in range(1, int(N / 2) + 1)) + 2 * sum(
    #     f(a + 2 * i * h) for i in range(1, int(N / 2))))
    # if N % 2 == 1:
    #     N += 1
    #
    # dx = 1.0 * (b - a) / N
    # sum = (f(a) + 4 * f(a + dx) + f(b))
    # for i in range(1, N // 2):
    #     sum += 2 * f(a + (2 * i) * dx) + 4 * f(a + (2 * i + 1) * dx)
    #
    # return sum * dx / 3
    result = 0
    h = (a - b) / N
    for i in range(N // 2):
        x = h * i * 2
        result = result + f(x) + 4 * f(x + h) + f(x + h * 2)
    result = h * result / 3

    return result


N_values = np.arange(10, 1001)
I_diff_triang = []
I_diff_trap = []
I_diff_simp = []

for N in N_values:
    I_triang = 2 * triangle_rule(f, 0, np.pi / 2, N)
    I_trap = 2 * trapezoid_rule(f, 0, np.pi / 2, N)
    I_simp = 2 * simpsons_rule(f, 0, np.pi / 2, N)
    I_diff_triang.append(abs(I_triang - I_exact))
    I_diff_trap.append(abs(I_trap - I_exact))
    I_diff_simp.append(abs(I_simp - I_exact))

plt.figure(figsize=(10, 6))
plt.plot(N_values, I_diff_triang, label='Triangle')
# plt.plot(N_values, I_diff_trap, label='Trapezoid')
plt.plot(N_values, I_diff_simp, label='Simpsons')
# plt.yscale('log')
plt.xlabel('Number of divisions (N)')
plt.ylabel('Difference from exact solution')
plt.legend()
plt.grid(True)
plt.show()
