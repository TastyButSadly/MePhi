n = int(input())
A = []
for _ in range(0, n):
    A.append(int(input()))

res = []
for a_i in A:
    ost = a_i % 4
    if ost == 0:
        res.append(a_i // 4)
    if ost == 1:
        res.append(a_i // 4 + 1)
    if ost == 2:
        res.append(a_i // 4 + 2)
    if ost == 3:
        res.append(a_i // 4 + 1 + 1)
print(sum(res))