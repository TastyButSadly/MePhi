import numpy as np

data = np.loadtxt('Week 14.2 data.txt')

time = data[:, 0]
position = data[:, 1]
force = data[:, 2]

work = np.trapz(force, position)

average_power = work / (time[-1] - time[0])

print(f'Работа силы: {work}\n'
      f'Эталон:      0.4008387372')
print(f'Средняя мощность: {average_power}')
