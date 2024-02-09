import matplotlib.pyplot as plt
import numpy as np

dens_arr = [[1, 1], [2, 1], [2, 3], [3, 4]]
beta = 0.05
leng = 8
fig, ax = plt.subplots(nrows=2, ncols=2)

counter = 0
for i in (0, 1):
    for j in (0, 1):
        a = dens_arr[counter][0]
        b = dens_arr[counter][1]
        x = [np.sin(a * t + 0.5 * np.pi) for t in np.arange(0., leng * np.pi, 0.01)]
        y = [np.sin(b * t) for t in np.arange(0., leng * np.pi, 0.01)]
        x1 = [np.exp(-beta * t) * np.sin(a * t + 0.5 * np.pi) for t in np.arange(0., leng * np.pi, 0.01)]
        y1 = [np.exp(-beta * t) * np.sin(b * t) for t in np.arange(0., leng * np.pi, 0.01)]
        ax[i, j].plot(x, y)

        ax[i, j].plot(x1, y1)
        ax[i, j].set_xlabel(r'$x$')
        ax[i, j].set_ylabel(r'$y$')
        counter += 1

plt.suptitle(r'Four graphs in one window', fontsize=20)
plt.tight_layout()
plt.show()
