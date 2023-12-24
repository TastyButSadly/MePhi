with open('Week 14.2 data.txt', 'r') as file:
    data = [line.split() for line in file]

work = 0
total_time = float(data[-1][0]) - float(data[0][0])

for i in range(1, len(data) - 1):
    time_i = float(data[i][0])
    time_next = float(data[i + 1][0])
    delta_t = time_next - time_i

    x_i = float(data[i][1])
    force_i = float(data[i][2])
    work += force_i * (x_i - float(data[i - 1][1]))

average_power = work / total_time

width = 10  # количество знаков
print(f'Общая работа :     {work:{width}f}\n'
      f'Эталонная работа :   0.400838\n'
      f'Средняя мощность : {average_power:{width}f}')
