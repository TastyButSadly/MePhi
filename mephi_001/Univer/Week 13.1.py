import matplotlib.pyplot as plt
import csv
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


X, Y = plot_data('inertia_2.25_0.43.csv')
X1, Y1 = plot_data('inertia_1.98_0.36.csv')

coeff = np.polyfit(X, Y, 2)
coeff1 = np.polyfit(X1, Y1, 2)

print(f"собственный момент инерции: {round(coeff[0], 6)}")
print(f"собственный момент инерции: {round(coeff1[0], 6)}")

xn = np.linspace(0, max(X), 100)
xn1 = np.linspace(0, max(X1), 100)
yn = np.poly1d(coeff)
yn1 = np.poly1d(coeff1)

plt.plot(xn, yn(xn), label=' 2')
plt.scatter(X, Y, label='Data 1', s=10)
plt.xlim(0, 2)
plt.plot(xn1, yn1(xn1), label=' 2')
plt.scatter(X1, Y1, label='Data 2', s=10)
plt.title('Line graph')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()