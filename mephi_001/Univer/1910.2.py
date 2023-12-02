import math

p = float(input("Введите значение параметра р: "))
q = p / 3
r = 9 / 27

delta = (q ** 3) + (r ** 2)
sqrt_delta = math.sqrt(abs(delta))
u = ((sqrt_delta - r) ** (1/3)) if delta >= 0 else ((-sqrt_delta - r) ** (1/3))

y1 = u - q/u
y2 = (-0.5 * (u + q/u)) + ((math.sqrt(3) / 2) * (u - q/u))
y3 = (-0.5 * (u + q/u)) - ((math.sqrt(3) / 2) * (u - q/u))

# подстановка корней
equation1 = y1 ** 3 + p * y1 + 9
equation2 = y2 ** 3 + p * y2 + 9
equation3 = y3 ** 3 + p * y3 + 9

print(f"Корень y1 = {y1:.3f}")
print(f"Корень y2 = {y2:.3f}")
print(f"Корень y3 = {y3:.3f}")

print(f"Результат подстановки y1: {equation1:.3f}")
print(f"Результат подстановки y2: {equation2:.3f}")
print(f"Результат подстановки y3: {equation3:.3f}")
