import sympy as sp
import time
from sympy import pi
import matplotlib.pyplot as plt

k_B, T, h, c = sp.symbols('k_B T h c')
koeff = (2 * sp.pi * k_B ** 4) / (h ** 3 * c ** 2)

constants = {k_B: 1.380649e-23, h: 6.62607015e-34, c: 299792458}


def stefan_boltzmann(terms):
    u = sp.symbols('u', positive=True)

    exp_series = sp.series(1 / (1 - sp.exp(-u)), sp.exp(-u), n=terms).removeO()

    integral = sp.integrate(exp_series * u ** 3 * sp.exp(-u), (u, 0, sp.oo))
    # print(exp_series)
    # print(integral)

    theoretical_value = pi ** 4 / 15
    error = abs(integral - theoretical_value)
    return integral.evalf(), error.evalf()


def convergence_research(precision):
    theoretical_value = sp.pi ** 4 / 15
    terms = 1
    while True:
        start_time = time.time()
        sigma, error = stefan_boltzmann(terms)
        end_time = time.time()

        if error < 10 ** (-precision):
            break
        terms += 1
    return sigma, error, terms, end_time - start_time


precisions = [2, 3]
results = {}
for prec in precisions:
    sigma, error, terms, timing = convergence_research(prec)
    results[prec] = (sigma, error, terms, timing)
    print(
        f"Precision: {prec} digits,  Sigma: {sigma * koeff.evalf(subs=(constants))}, Error: {error}, Terms: {terms}, Time: {timing:.3f} sec")

# print(pi ** 4 / 15)

# terms = [6, 13, 27, 58]
# digits = [2, 3, 4, 5]
# plt.plot(terms, digits)
# plt.show()
