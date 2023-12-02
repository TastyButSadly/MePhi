import math

x1, x2 = map(float, input("Введите x1, x2\n").split())


# def par_len(x1, x2, a=1, b=1):
#     return abs(math.sqrt(1 + (2 * a * x2 + b) ** 2) - math.sqrt(1 + (2 * a * x1) ** 2))

def par_len(x1, x2):
    return abs((1 + x2 ** 2) ** 0.5 * x2 / 2 + 0.5 * math.log(abs((1 + x2 ** 2) ** 0.5 + x2)) - \
               (1 + x1 ** 2) ** 0.5 * x1 / 2 + 0.5 * math.log(abs((1 + x1 ** 2) ** 0.5 + x1)))


print(round(math.sqrt((x2 - x1) ** 2 + (x2 ** 2 - x1 ** 2) ** 2), 3))

print(round(par_len(x1, x2), 3))
