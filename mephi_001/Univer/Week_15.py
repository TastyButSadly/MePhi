import csv
import json

import matplotlib.pyplot as plt
import numpy as np


def plot_data(file_path):
    X = []
    Y = []

    with open(file_path, 'r') as datafile:
        data = csv.reader(datafile, delimiter=' ')
        for row in data:
            arr_num = row[0].split(' ')
            X.append(float(arr_num[0]))
            Y.append(float(arr_num[-1]))

    return X, Y


with open(config_file, 'r') as f:
    config1 = json.load(f)
with open(config_file, 'r') as f:
    config2 = json.load(f)
# Загрузка конфигурации для первого графика
# config = load_config('config1.json')
config = load_config('config2.json')
graph1 = config['graph1']
X, Y = plot_data(graph1['file_path'])
coeff = np.polyfit(X, Y, 2)
yn = np.poly1d(coeff)

# первый график
plt.plot(np.linspace(0, max(X), 100), yn(np.linspace(0, max(X), 100)),
         label=graph1['label'], color=graph1['color'], linestyle=graph1['line_style'])
plt.scatter(X, Y, label=graph1['label'], color=graph1['color'], marker=graph1['marker_style'], s=graph1['marker_size'])

# Загрузка конфигурации для второго графика
graph2 = config['graph2']
X1, Y1 = plot_data(graph2['file_path'])
coeff1 = np.polyfit(X1, Y1, 2)
yn1 = np.poly1d(coeff1)

#  второй графика
plt.plot(np.linspace(0, max(X1), 100), yn1(np.linspace(0, max(X1), 100)),
         label=graph2['label'], color=graph2['color'], linestyle=graph2['line_style'])
plt.scatter(X1, Y1, label=graph2['label'], color=graph2['color'], marker=graph2['marker_style'],
            s=graph2['marker_size'])

# Оформление графика
common = config['common']
plt.xlim(0, 2)
plt.title(common['title'])
plt.xlabel(common['x_label'])
plt.ylabel(common['y_label'])
plt.legend()
plt.show()
