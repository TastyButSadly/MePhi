from math import log


def par_len(l1, l2):
    kant = lambda y: y * (1 + 4 * y ** 2) ** 0.5 / 2 + \
                     0.25 * log(abs((1 + 4 * y ** 2) ** 0.5 + 2 * y))
    return kant(l2) - kant(l1)


l1, l2 = map(int, input().split())
print(round(par_len(l1, l2), 3))
print(round(((l2 - l1) ** 2 + (l2 ** 2 - l1 ** 2) ** 2) ** 0.5, 3))
