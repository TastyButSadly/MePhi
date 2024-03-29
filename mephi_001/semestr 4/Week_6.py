import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


k_prime = 1.5
m_prime = 0.1
d_prime = 0.4
l_prime = 1.0
g_prime = 9.81

# Параметры после обезразмеривания
k = k_prime
m = m_prime

l = l_prime
g = g_prime

omega0 = np.sqrt(g/l)
d = d_prime / omega0 ** 2

def pendulum_system(t, y):
    return [y[1], -omega0 ** 2 * y[0] + d * (y[0] + y[2]), y[3], -omega0 ** 2 * y[2] + d * (y[0] + y[2])]


initial_conditions = [
    (0.1, 0, 0.1, 0),   # ϕ1(0) = ϕ2(0) = ϕ0
    (0.1, 0, -0.1, 0),  # ϕ1(0) = −ϕ2(0)
    (0, 0, 0.1, 0)      # ϕ1(0) = 0, ϕ2(0) = ϕ0
]

t_span = [0, 10 * omega0]

for i, y0 in enumerate(initial_conditions):
    sol = solve_ivp(pendulum_system, t_span, y0, t_eval=np.linspace(*t_span, 500))

    plt.figure(figsize=(10, 5))
    plt.plot(sol.t / omega0, sol.y[0], label='ϕ1(t)')
    plt.plot(sol.t / omega0, sol.y[2], label='ϕ2(t)')
    plt.xlabel('Time (s)')
    plt.ylabel('Angle (rad)')
    plt.title(f'Solution for initial conditions {i + 1}')
    plt.legend()
    plt.grid(True)
    plt.show()

sol = solve_ivp(pendulum_system, t_span, initial_conditions[1], t_eval=np.linspace(*t_span, 500))
frequencies = np.fft.fftfreq(len(sol.t), sol.t[1] - sol.t[0])
fft = np.fft.fft(sol.y[0])
frequency = abs(frequencies[np.argmax(np.abs(fft))]) * omega0
print(f'Calculated frequency for the case ϕ1(0) = −ϕ2(0): {frequency:.15f}')

theoretical_frequency = np.sqrt(g + 2 * d) * omega0
print(f'Theoretical frequency: {theoretical_frequency:.15f}')
