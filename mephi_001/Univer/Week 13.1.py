import matplotlib.pyplot as plt
import csv
import numpy as np

X = []
Y = []
X_2 = []


def plot_data(file_path):
    with open(file_path, 'r') as datafile:
        data = csv.reader(datafile, delimiter=' ')

        for row in data:
            #print(row[0])
            arr_num = row[0].split(' ')
            # print(arr_num)
            # print(float(arr_num[0]) ** 2, arr_num[-1])
            X.append(float(arr_num[0]) ** 2)
            Y.append(float(arr_num[-1]))
            # X_2.append(float(arr_num[0]))
    return [X, Y]


# print(X, '\n', Y))
X, Y = plot_data('inertia_2.25_0.43.csv')
plt.plot(X, Y)
coeff = np.polyfit(X, Y, 1)
print(f"собственный момент инерции: {round(coeff[0], 6)}")
xn = np.linspace(X[1], X[-1], 2)
yn = np.poly1d(coeff)
plt.plot(xn, yn(xn), X, Y)
# plt.plot(X_2, Y)
plt.title('Line graph')
# plt.xlabel('X')
# plt.ylabel('Y')
plt.show()

