import numpy as np
from scipy.integrate import quad
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

data = np.loadtxt("data2.txt")
E_values = data[:, 0]
T_values = data[:, 1]

m = 0.2


def integr(x, E, A, alpha):
    return np.sqrt(2 * m /  (E - A * np.abs(x) ** alpha))


def period(E, A, alpha):
    extr_point = (E / A) ** (1 / alpha)
    integral, _ = quad(integr, 0, extr_point, args=(E, A, alpha))
    return integral * 4


def fit_function(E, A, alpha):
    return np.array([period(e, A, alpha) for e in E])


fitted, _ = curve_fit(fit_function, E_values, T_values)
A_fit, alpha_fit = fitted

print("A =", A_fit)
print("alpha =", alpha_fit)

E_range = np.linspace(min(E_values), max(E_values), 100)
T_fit = fit_function(E_range, A_fit, alpha_fit)

plt.plot(E_values, T_values, 'o', label='Data')
plt.plot(E_range, T_fit, '-', label='Fitted')
plt.xlabel("Energy (E)")
plt.ylabel("Period (T)")
plt.legend()
plt.show()
