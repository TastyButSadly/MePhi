import json
import matplotlib.pyplot as plt
import numpy as np
import csv


def load_config(file_path):
    with open(file_path, 'r') as config_file:
        config = json.load(config_file)
    return config


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


def plot_graph(data_files, degree, plot_params, axes_limits, titles):
    plt.figure()

    for file_path in data_files:
        X, Y = plot_data(file_path)
        coeff = np.polyfit(X, Y, degree)
        xn = np.linspace(axes_limits["x_min"], axes_limits["x_max"], 100)
        yn = np.poly1d(coeff)

        plt.plot(xn, yn(xn),
                 label=f'Degree {degree} - {file_path.split("_")[1]}_{file_path.split("_")[2].split(".")[0]}',
                 color=plot_params["line_color"], linestyle=plot_params["line_style"],
                 marker=plot_params["marker_style"])
        plt.scatter(X, Y, s=10)

    plt.xlim(axes_limits["x_min"], axes_limits["x_max"])
    plt.title(titles["graph_title"])
    plt.xlabel(titles["x_label"])
    plt.ylabel(titles["y_label"])
    plt.legend()

    if plot_params["log_scale"]:
        plt.yscale('log')

    plt.show()


# Загрузка параметров из конфиг-файла
config = load_config('config.json')

# Построение графика с использованием параметров из конфиг-файла
plot_graph(config["data_files"], config["degree"], config["plot_params"], config["axes_limits"], config["titles"])
