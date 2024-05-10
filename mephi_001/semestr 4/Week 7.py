import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

alpha = 1.0
gamma = 1.0

H_eff = np.array([0.0, 0.0, 1.0])


def landau_lif(t, m):
    dmdt = -gamma * np.cross(m, H_eff) + alpha * np.cross(m, np.cross(m, H_eff))
    return dmdt


m0 = np.array([0.0, 1.0, 0.0])

t_span = [0.0, 20.0]

sol = solve_ivp(landau_lif, t_span, m0, t_eval=np.linspace(t_span[0], t_span[1], 1000))

print("Временная зависимость магнитного момента:")
print(sol.y.T)
m_norm = np.linalg.norm(sol.y, axis=0)

fig, ax = plt.subplots()
ax.plot(sol.t, m_norm)
ax.set_xlabel('Время')
ax.set_ylabel('Модуль магнитного момента')
ax.set_title('Временная зависимость модуля магнитного момента')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.quiver(0, 0, 0, sol.y[0, 0], sol.y[1, 0], sol.y[2, 0], color='r')
for i in range(len(sol.t)):
    if i % 10 == 0:
        ax.quiver(0, 0, 0, sol.y[0, i], sol.y[1, i], sol.y[2, i], color='b', alpha=0.5)


ax.set_xlim([-1.2, 1.2])
ax.set_ylim([-1.2, 1.2])
ax.set_zlim([-1.2, 1.2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()
