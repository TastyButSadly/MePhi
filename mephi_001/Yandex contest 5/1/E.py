n, k, d = map(int, input().split(' '))
break_flag = False
uniq_flag = 0

for i in range(0, d):
    loc_flag = 0
    if break_flag == 0 and uniq_flag == 0:
        for num in range(0, 10):
            s = 10 * n + num
            if n % k == 0:
                n = str(n) + '0' * (d - i)
                uniq_flag = 1
                break
            if s % k == 0:
                n = s
                loc_flag = 1
                break
        if loc_flag == 0:
            break_flag = 1
            break
if break_flag == 0 or uniq_flag == 1:
    print(n)

else:
    print(-1)