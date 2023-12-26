# Из-за перекрытия на графике не видно левых прямоугольников

import matplotlib.pyplot as plt
import numpy as np

n = 10  # количество разбиений


def f(x):
    return (np.sin(x)) ** 5


a, b = 0, np.pi

exact_integral = 1 / 240 * (150 * np.cos(a) - 25 * np.cos(3 * a) + 3 * np.cos(5 * a) -
                            150 * np.cos(b) + 25 * np.cos(3 * b) - 3 * np.cos(5 * b))
h = (b - a) / n

x = np.linspace(a, b, n + 1)
print(x)

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

width = 10  # количество знаков после запятой
print(f'Error left :     {error_left}\n'
      f'Error right :    {error_right}\n'
      f'Error midpoint : {error_midpoint}')
print(exact_integral)

plt.title('sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()
