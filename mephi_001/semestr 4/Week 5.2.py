import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

m = 1.0
M = 2.0
L = 10.0
l = 0.5
g = 9.81
alpha_0 = np.pi / 12
alpha_vel = 1
y0 = [alpha_0, alpha_vel]

J = M * (L - l) ** 2 + 1 / 12 * m * L ** 2 + m * L ** 2 / 4
N = lambda alpha: M * g * (L - l) * np.sin(alpha) + m * g / (2 * L) * np.sin(alpha) * (l ** 2 + (L - l) ** 2)


def pendulum(t, y):
    alpha, alpha_dot = y
    alpha_dot_dot = -N(alpha) / J
    return alpha_dot, alpha_dot_dot

num_degr = 10000
# aplha2 = [pendulum(t, y)[1] for t in np.linspace(0, 20, num_degr)]

sol = solve_ivp(pendulum, [0, 20], y0, t_eval=np.linspace(0, 20, num_degr))

E_pot = M * g * (L - l) * (1 - np.cos(sol.y[0])) + m * g * (L / 2 - l) * (1 - np.cos(sol.y[0]))
E_kin = 0.5 * J * sol.y[1] ** 2

# E_tot = M * g * (L - l) * (1 - np.cos(y0[0])) + m * g * (L / 2 - l) ** 2 / L * (1 - np.cos(y0[0]))
E_max = max(E_pot)
E_tot = [E_max for i in range(num_degr)]  # E_tot =
plt.subplot(2, 2, 1)

plt.plot(sol.t, sol.y[0])
plt.title('Угол отклонения')
plt.grid()
plt.subplot(2, 2, 3)

plt.plot(sol.t, sol.y[1])
plt.grid()
# plt.plot(sol.t, E_pot)
plt.title('Угловая скорость')

plt.subplot(2, 2, 2)

plt.plot(sol.t, E_tot)
plt.grid()
plt.title('Полная энергия')

# plt.subplot(2, 2, 4)
# plt.plot(sol.t, aplha2)
# plt.title('')

plt.tight_layout()
plt.show()
