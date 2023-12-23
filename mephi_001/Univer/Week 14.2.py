import numpy as np

data = np.loadtxt('Week 14.2 data.txt')

def triangle_rule(f, a, b, N):
    h = (b - a) / N
    return h * sum(f(a + i * h) for i in range(N))

time = data[:, 0]
position = data[:, 1]
force = data[:, 2]

work = triangle_rule()
work = np.trapz(force, position)

average_power = work / (time[-1] - time[0])

print(f'Работа силы: {work}\n'
      f'Эталон:      0.4008387372')
print(f'Средняя мощность: {average_power}')
