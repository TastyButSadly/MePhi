N = int(input())
s = list(map(int, input().split()))
m = max(s)
su = sum(s)
if (su - m) >= m:
    res = su
else:
    res = 2 * m - su
print(res)
