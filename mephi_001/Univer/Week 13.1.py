import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = np.array()

x = data[:, 0]
I = data[:, 1]


plt.plot(x, I, marker='o', linestyle='-', color='b')
plt.title('График зависимости момента инерции от расстояния')
plt.xlabel('Расстояние, м')
plt.ylabel('Момент инерции')
plt.grid(True)
plt.show()
