import matplotlib.pyplot as plt
import numpy as np

a = 1e-6
T = 300
k = 1.38e-23
v_avg = 1e3

file = '10.8.txt'
data = np.loadtxt(file)
t_steps = data[:, 1]
x = data[:, 0]
dx = data[:, 2]  #

lambda_val= float(file.split('_')[-1].split('.')[0])


t = t_steps * lambda_val * 1e-6 / v_avg


# interpolate_func = UnivariateSpline(t, x, s=20, k=1)


coefficients = np.polyfit(t, x, 1)
line_func = np.poly1d(coefficients)
t_interp = np.linspace(t[0], 2 * t[-1], 50)
x_line = line_func(t_interp)


t0 = 0.45
t_max = 2 * t[-1]
x0_line = line_func(t0)
# x0_interp = interpolate_func(t0)
x_max_line = line_func(t_max)

#
plt.figure(figsize=(12, 12))
plt.subplot(2, 2, 1)
plt.errorbar(t, x, yerr=dx, marker='o')
plt.xlabel('t, с')
plt.ylabel('x, м')
plt.grid(True)
plt.title('Зависимость смещения от времени')
plt.legend()

plt.subplot(2, 2, 2)

coefficients = np.polyfit(t, np.log(x), 1)
line = np.poly1d(coefficients)


plt.plot(t, line(t), label='Линейная аппроксимация')

plt.errorbar(t, np.log(x), marker='o')
plt.ylabel('log(x), log(м)')
plt.xlabel('log(t), log(с)')
plt.grid(True)
plt.title('Логарифмическая зависимость смещения от времени')
plt.legend()

plt.subplot(2, 2, 3)
coefficients = np.polyfit(t, x ** 0.5, 1)
line = np.poly1d(coefficients)


plt.plot(t, line(t), label='Линейная аппроксимация')
plt.errorbar(t, x ** 0.5, yerr=dx ** 0.5, fmt='-o')
plt.title('x^0.5 (t)')
plt.grid(True)

plt.show()

plt.figure(figsize=(8, 6))

plt.plot(t, x, 'o', label='Исходные данные')
plt.plot(t_interp, x_line, '--', label='Линейная аппроксимация')
plt.xlabel('Время')
plt.ylabel('Квадрат координаты')
plt.title('График зависимости квадрата координаты от времени')
plt.legend()
plt.grid(True)
plt.show()

print(f"Смещение через время, в два раза большее времени наблюдения: {x_max_line/10e6:.0f} 10^6")
print(f"Смещение в момент времени 0.45 с: {x0_line/10e6:.0f} 10^6")
# print(x**2)


eta = k * T * x_line *10e12/ (np.pi * a *  x_line ** 2)
print(f"вязкость жидкости: {eta.mean()*10e9:.3f} МПа*с")