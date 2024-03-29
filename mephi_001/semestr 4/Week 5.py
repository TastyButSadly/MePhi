import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

omega = 2
initial_cond = [0, 1]


def oscill(t, yz, omega):
    y = yz[0]
    z = yz[1]
    return [z, -omega ** 2 * y]  # y' = z, z' = -omega^2 * y
def exact_energy(y, z, omega):
    return 0.5 * (z**2 + omega**2 * y**2)


t = np.linspace(0, 100, 100)
sol = solve_ivp(oscill, t_span=[0, max(t)], y0=initial_cond, args=(omega,), t_eval=t, rtol=1 * 10 ** -5)
plt.plot(sol.t, sol.y[0])
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.title('')
plt.show()


