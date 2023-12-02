import math


def summ_1(alpha=0.00001):
    result = 0
    k = 1
    a_n = lambda k: 1 / (k * (4 * k ** 2 - 1))
    while a_n(k + 1) >= alpha:
        result += a_n(k)
        k += 1

    return k, result, 2 * math.log(2) - 1


def summ_2(alpha=0.00001):
    result = 0
    k = 1
    a_n = lambda k: 1 / (k * (9 * k ** 2 - 1))
    while a_n(k + 1) >= alpha:
        result += a_n(k)
        k += 1
    return k, result, 3 / 2 * (math.log(3) - 1)


def summ_3(alpha=0.00001):
    result = 0
    k = 1
    a_n = lambda k: k / (4 * k ** 2 - 1) ** 2
    while a_n(k + 1) >= alpha:
        result += a_n(k)
        k += 1
    return k, result, 1 / 8


print(summ_1(0.000_000_01), summ_2(0.000_000_01), summ_3(0.000_000_01), sep='\n')
