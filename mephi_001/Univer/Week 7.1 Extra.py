import matplotlib.pyplot as plt
import math


def collatz(n):
    if type(n) == 'int':
        return None

    sequence = [n]

    def collatz_rec(x):
        if x == 1:
            return
        elif x % 2 == 0:
            n_value = x // 2
        else:
            n_value = 3 * x + 1
        sequence.append(n_value)
        collatz_rec(n_value)

    collatz_rec(n)
    return sequence


def coll_plot_count(n):
    x = [i for i in range(1, n)]
    y = [len(collatz(i)) for i in range(1, n)]
    plt.plot(x, y)
    plt.grid()
    plt.show()


def coll_plot_max(n):
    x = [i for i in range(1, n)]
    y = [max(collatz(i)) for i in range(1, n)]
    plt.plot(x, y)
    plt.show()


def coll_plot_n(n, tp=0):
    x = [i for i in range(len(collatz(n)))]
    y = collatz(n)
    if tp:
        plt.semilogy()
    plt.plot(x, y)
    plt.show()


n = int(input())
# print(collatz(n))
# coll_plot_count(n)
# coll_plot_max(n)
coll_plot_n(n, 1)
