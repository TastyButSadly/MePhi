def eratosphen(n):
    num = [i for i in range(n + 1)]
    num[1] = 0
    for i in range(2, n + 1):
        if num[i] != 0:
            for j in range(i * 2, n + 1, i):
                num[j] = 0
    return [1] + [i for i in num if i != 0]


print(eratosphen(100))
