import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

m = 1.0
M = 2.0
L = 2.0
l = 1.0
g = 9.81


def theta_d(t, state):
    theta, omega = state
    alpha = -(g / L) * np.sin(theta)
    return [omega, alpha]


initial_state = [np.radians(30), 0]

T = 10.0
dt = 0.01
times = np.arange(0, T, dt)

solution = solve_ivp(theta_d, [0, T], initial_state, t_eval=times)

theta_values = solution.y[0]
omega_values = solution.y[1]
alpha_values = -(g / L) * np.sin(theta_values)

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(times, np.degrees(theta_values))
plt.title('Угол отклонения от времени')
plt.ylabel('Угол')
plt.grid()

plt.subplot(2, 2, 2)
plt.plot(times, omega_values)
plt.title('Угловая скорость от времени')
plt.ylabel('Угловая скорость')
plt.grid()

plt.subplot(2, 2, 3)
plt.plot(times, alpha_values)
plt.title('Ускорение от времени')
plt.ylabel('Ускорение')
plt.grid()

plt.tight_layout()
plt.show()
