n, k = map(int, input().split())
nummers = list(map(int, input().split()))
repeat = {}
for i in range(n):
    numm = nummers[i]
    if numm not in repeat:
        repeat[numm] = [i]
    else:
        repeat[numm] = repeat[numm] + [i]
    list_i = repeat[numm]
    if len(list_i) >= 2:
        if list_i[-1] - list_i[-2] <= k:
            print('YES')
            exit()

print('NO')
