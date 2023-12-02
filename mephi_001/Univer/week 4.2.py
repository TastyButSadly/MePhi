import random
import math

x1 = 2
y1 = 4
z1 = 6
x2 = 4
y2 = 2
z2 = 7

# x1 = random.uniform(0, 10)
# y1 = random.uniform(0, 10)
# z1 = random.uniform(0, 10)
# x2 = random.uniform(0, 10)
# y2 = random.uniform(0, 10)
# z2 = random.uniform(0, 10)
print("Точка 1", round(x1, 1), round(y1, 1), round(z1, 1))
print("Точка 2", round(x2, 1), round(y2, 1), round(z2, 1))
v1 = (x1, y1, z1)
v2 = (x2, y2, z2)

det = (
    v1[1] * v2[2] - v1[2] * v2[1],
    -v1[2] * v2[0] + v1[0] * v2[2],
    v1[0] * v2[1] - v1[1] * v2[0]
)

m_a = math.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2)
m_b = math.sqrt(x2 ** 2 + y2 ** 2 + z2 ** 2)

ang = math.acos((x1 * x2 + y1 * y2 + z1 * z2) / (m_a * m_b)) / math.pi * 180

par_area = math.sqrt(det[0] ** 2 + det[1] ** 2 + det[2] ** 2)
tr_area = 0.5 * par_area

print("\nПлощадь параллелограмма:", round(par_area, 1))
print("Площадь треугольника:   ", round(tr_area, 1))
print("Угол ", round(ang, 1))
