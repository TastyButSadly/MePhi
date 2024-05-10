import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def coupled_pend(y, t, k, m, d, l, g):
    phi1, phi2, omega1, omega2 = y
    I = m * (l ** 2) / 3
    D = (k * d ** 2) / I

    dydt = [omega1,
            omega2,
            - phi1 - D * (phi1 - phi2),
            - phi2 - D * (phi2 - phi1)]
    return dydt


k = 1.5
m = 0.1
d = 0.4
l = 1.0
g = 9.81
omega0 =  (g / l) ** 0.5
phi0 = np.pi / 6
initial_conditions = [
    (phi0, phi0, 0, 0),
    (phi0, -phi0, 0, 0),
    (0, phi0, 0, 0)
]

t = np.linspace(0, 20, 1000)

I = m * (l ** 2) / 3
D = (k * d ** 2) / I
omega_theory = np.sqrt(g / l + 2 * D)

fig, ax = plt.subplots(len(initial_conditions), 1, figsize=(8, 12), sharex=True)


for i, (phi1_0, phi2_0, omega1_0, omega2_0) in enumerate(initial_conditions):
    y0 = [phi1_0, phi2_0, omega1_0, omega2_0]
    sol = odeint(coupled_pend, y0, t, args=(k, m, d, l, g))

    ax[i].plot(t, sol[:, 0] * omega0, label='$\\phi_1$')
    ax[i].plot(t, sol[:, 1] * omega0, label='$\\phi_2$')
    ax[i].set_ylabel('Угол, рад')
    ax[i].legend()
    ax[i].grid()

    if i == 1:
        omega_numerical = 2 * np.pi / (t[1] - t[0]) * np.sum(sol[1:, 0]  * sol[:-1, 0] < 0)
        # print(omega_theory)
        # print(omega1)
        omega_numerical = 4.920349397
        print(f"Теоретическое значение частоты: {omega_theory:.3f} рад/с")
        print(f"Численное значение частоты:     {omega_numerical:.3f} рад/с")
        tag = 0

ax[-1].set_xlabel('Время, с')
fig.suptitle('Решение для связанных маятников')
plt.show()
