from math import pi

L, x1, v1, x2, v2 = map(int, input().split(' '))

p1_0 = x1 * 2 * pi / L
p2_0 = x2 * 2 * pi / L
if v1 == v2 == 0 and (p1_0 != p2_0 or p1_0 != - p2_0):
    print('NO')
if p1_0 == p2_0:
    print('YES')
    print(f'{0:.{10}f}')

res = []
for a1 in [-1, 1]:
    for a2 in [-1, 1]:
        res.append((a1 * x1 + a2 * x2) / (a2 * v2 + a1 * v1))

print('YES')
print(f'{min(res):.{10}f}')
# p1 = 2 * pi / L * (x1 + v1 * t)
# p2 = 2 * pi / L * (x2 + v2 * t)
