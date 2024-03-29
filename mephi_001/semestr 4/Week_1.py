import matplotlib.pyplot as plt
import numpy as np

dens_arr = [[1, 1], [2, 1], [2, 3], [3, 4]]
beta = 0.05
leng = 8
fig, ax = plt.subplots(nrows=2, ncols=2)
for i in range(2):
    for j in range(2):
        pi_coeff = 0.5
        a = dens_arr[i * 2 + j][0]
        b = dens_arr[i * 2 + j][1]

        if a == 2 and b == 1:
            pi_coeff = 1

        x = [np.sin(a * t + pi_coeff * np.pi) for t in np.arange(0., leng * np.pi, 0.01)]
        y = [np.sin(b * t) for t in np.arange(0., leng * np.pi, 0.01)]
        x1 = [np.exp(-beta * t) * np.sin(a * t + pi_coeff * np.pi) for t in np.arange(0., leng * np.pi, 0.01)]
        y1 = [np.exp(-beta * t) * np.sin(b * t) for t in np.arange(0., leng * np.pi, 0.01)]
        if pi_coeff == 1:
            x, y = y, x
            x1, y1 = y1, x1
        ax[i, j].set_xlim(-1.2, 2)
        ax[i, j].plot(x, y, label='Без затухания')
        ax[i, j].plot(x1, y1, label='С затуханием')
        ax[i, j].set_xlabel(r'$x$')
        ax[i, j].set_ylabel(r'$y$')
        ax[i, j].set_title(f'Отношение частот {a}:{b}')
        ax[i, j].legend(loc='upper right')

plt.suptitle(r'Four graphs in one window', fontsize=20)
plt.tight_layout()
plt.show()
