# Из-за перекрытия на графике не видно левых прямоугольников

import matplotlib.pyplot as plt
import numpy as np

n = 100


def f(x):
    return np.sin(x)


a, b = 0, np.pi / 2

exact_integral = np.cos(a) - np.cos(b)  # точное значение интеграла

h = (b - a) / n

x = np.linspace(a, b, n + 1)

plt.plot(x, f(x), label='sin(x)')

# Левые прямоугольники
left_rectangles = h * np.sum(f(x[:-1]))
plt.bar(x[:-1], f(x[:-1]), width=h, align='edge', label='Left rectangles')

# Правые прямоугольники
right_rectangles = h * np.sum(f(x[1:]))
plt.bar(x[1:], f(x[1:]), width=-h, align='edge', label='Right rectangles')

# Средние прямоугольники
midpoints = (x[:-1] + x[1:]) / 2
midpoint_rectangles = h * np.sum(f(midpoints))
plt.bar(midpoints, f(midpoints), width=h, align='center', label='Midpoint rectangles')

error_left = np.abs(left_rectangles - exact_integral)
error_right = np.abs(right_rectangles - exact_integral)
error_midpoint = np.abs(midpoint_rectangles - exact_integral)

width = 5  # количество знаков после запятой
print(f'Error left :     {error_left:{width}f}\n'
      f'Error right :    {error_right:{width}f}\n'
      f'Error midpoint : {error_midpoint:{width}f}')

plt.title('sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()
