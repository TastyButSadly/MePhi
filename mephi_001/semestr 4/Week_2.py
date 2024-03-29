import matplotlib.pyplot as plt
import numpy as np

L = 0.5e-6
N = 10
alpha = 0.01
xi = 2e-7

N_x = 400
N_y = 400

dx = dy = L / N_x

x, y = np.meshgrid(np.arange(0, L, dx), np.arange(0, L, dy))

defects = np.random.rand(N, 2) * L

U = np.zeros((N_x, N_y))

for i in range(N_x):
    for j in range(N_y):
        for defect in defects:
            r = np.sqrt((x[i, j] - defect[0]) ** 2 + (y[i, j] - defect[1]) ** 2)
            # if r <= xi:
            U[i, j] += alpha * np.exp(-2 * r / xi) / (r / xi + 1)

plt.pcolormesh(x, y, U, cmap="plasma")
plt.colorbar()

plt.contour(x, y, U, cmap='plasma', linewidths=1, levels=30)
plt.xlabel("x ")
plt.ylabel("y")
plt.title('Профиль потенциала дефектов')
plt.show()
plt.savefig("potential.pdf")
