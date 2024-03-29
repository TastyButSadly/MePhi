a, b = map(int, input().split(':'))
c, d = map(int, input().split(':'))
tag = not bool(int(input()) - 1)
# a, b = 2, 2
# c, d = 1, 1
# tag = not bool(2 - 1)

if a + c > b + d:
    res = 0
elif a + c == b + d:
    if tag:
        diff = c - b
        if diff > 0:
            res = 0
        else:
            res = 1
    else:
        diff = c - b
        if diff > 0:
            res = 1
        else:
            res = - diff + 2

elif a + c < b + d:
    res = b + d - a - c
    c += res
    if tag:
        diff = c - b
        if diff > 0:
            res += 0
        else:
            res += - diff + 1
    else:
        diff = c - b
        if diff > 0:
            res += 1
        else:
            res += - diff + 2
else:
    res = 1
print(res)
