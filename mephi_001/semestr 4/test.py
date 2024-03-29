import random

import matplotlib.pyplot as plt
import numpy as np

size = 0.5
n_defects = 10
alpha = 0.01
xi = 2

nx, ny = 100, 100
x = np.linspace(0, size, nx)
y = np.linspace(0, size, ny)
X, Y = np.meshgrid(x, y)

defect_x = [random.uniform(0, size) for _ in range(n_defects)]
defect_y = [random.uniform(0, size) for _ in range(n_defects)]
# defect_r = 0.02  # Радиус дефектов (мкм)

potential = np.zeros_like(X)
def_coord = [[random.randint(0, nx), random.randint(0, ny)] for _ in range(n_defects)]
for dx, dy in zip(x, y):
    r = np.sqrt(X ** 2 + Y ** 2)
    for i in range(n_defects):
        x_i = def_coord[i][0]
        y_i = def_coord[i][1]
        r_i = np.sqrt((x_i - dx) ** 2 + (x_i - dy) ** 2)
        potential += -alpha * np.exp(-2 * r_i / xi) / (r_i / xi + 1)



fig, ax = plt.subplots(figsize=(8, 8))
cs = ax.contourf(X, Y, potential, levels=200, cmap='RdBu_r')
ax.scatter(defect_x, defect_y, s=50, c='k', marker='o')
ax.scatter(defect_x, defect_y, s=50, c='k')

stable_x = defect_x[0]
stable_y = defect_y[0]
unstable_x = defect_x[1]
unstable_y = defect_y[1]
# ax.scatter([stable_x, unstable_x], [stable_y, unstable_y], s=100, c=['g', 'r'], marker='x')
ax.scatter([stable_x, unstable_x], [stable_y, unstable_y], s=100, c=['g', 'r'])
ax.contour(X, Y, potential, cmap='RdBu_r', linewidths=1, levels=30)

ax.set_xlabel('X (мкм)')
ax.set_ylabel('Y (мкм)')
ax.set_title('Профиль потенциала дефектов')
fig.colorbar(cs)
plt.savefig('potential_profile.pdf')
plt.show()
