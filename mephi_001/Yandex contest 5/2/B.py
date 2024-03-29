N, k = map(int, input().split(' '))

price = list(map(int, input().split()))

res = [0]
for i in range(N):
    if i + k <= N:
        res.append(- price[i] + max(price[i:i + k + 1]))
    else:
        res.append(- price[i] + max(price[i:]))
print(max(res))
