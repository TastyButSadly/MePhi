import numpy as np
import matplotlib.pyplot as plt

R = 4.56 / 100  # cm to m
rho = 2700  # density of aluminium
I_exact = 0.4 * rho * (4 / 3) * np.pi * R ** 5  # exact moment of inertia


def f(theta):
    return rho * R ** 2 * (R * np.sin(theta)) ** 2 * np.sin(theta)


def triangle_rule(f, a, b, N):
    h = (b - a) / N
    return h * sum(f(a + i * h) for i in range(N))


def trapezoid_rule(f, a, b, N):
    h = (b - a) / N
    return h * (0.5 * f(a) + 0.5 * f(b) + sum(f(a + i * h) for i in range(1, N - 1)))


def simpsons_rule(f, a, b, N):
    h = (b - a) / N
    return h / 3 * (f(a) + f(b) + 4 * sum(f(a + i * h) for i in range(1, N, 2)) + 2 * sum(
        f(a + i * h) for i in range(2, N - 1, 2)))


N_values = np.arange(10, 1001)

I_diff_triang = []
I_diff_trap = []
I_diff_simp = []

for N in N_values:
    I_rect = 2*  triangle_rule(f, 0, np.pi / 2, N)
    I_trap =2 * trapezoid_rule(f, 0, np.pi / 2, N)
    I_simp = 2 * simpsons_rule(f, 0, np.pi / 2, N)
    I_diff_triang.append(abs(I_rect - I_exact))
    I_diff_trap.append(abs(I_trap - I_exact))
    I_diff_simp.append(abs(I_simp - I_exact))

# Plotting
# plt.figure(figsize=(10, 6))
plt.plot(N_values, I_diff_triang, label='Triangle Rule')
plt.plot(N_values, I_diff_trap, label='Trapezoid Rule')
plt.plot(N_values, I_diff_simp, label="Simpson's Rule")
plt.yscale('log')  # Use logarithmic scale for better visualization
plt.xlabel('Number of divisions (N)')
plt.ylabel('Difference from exact solution')
plt.legend()
plt.grid(True)
plt.show()
