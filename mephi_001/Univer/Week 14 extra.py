import matplotlib.pyplot as plt
import numpy as np

n = 100

def f(x):
    return np.sin(x)


a, b = 0, np.pi / 2


h = (b - a) / n

x = np.linspace(a, b, n + 1)

plt.plot(x, f(x), label='sin(x)')

left_rectangles = h * np.sum(f(x[:-1]))  # left
plt.bar(x[:-1], f(x[:-1]), label='Left Rectangles')

right_rectangles = h * np.sum(f(x[1:]))  # right
plt.bar(x[1:], f(x[1:]),  label='Right Rectangles')

midpoints = (x[:-1] + x[1:]) / 2  # mid
midpoint_rectangles = h * np.sum(f(midpoints))
plt.bar(midpoints, f(midpoints),  label='Midpoint Rectangles')

exact_integral = np.cos(a) - np.cos(b)  # exact

error_left = np.abs(left_rectangles - exact_integral)
error_right = np.abs(right_rectangles - exact_integral)
error_midpoint = np.abs(midpoint_rectangles - exact_integral)

print(f'Error left : {error_left}')
print(f'Error right : {error_right}')
print(f'Error mid : {error_midpoint}')

plt.title('Numerical Integration Methods for sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()
