n = int(input())
a = list(map(abs, map(int, input().split())))
even = []

counter = a[0] % 2
tag = -1
res = ['+'] * (n - 1)
for i in range(0, n - 1):
    if (a[i] + a[i + 1]) % 2 == 0:  # одинаковой чётности, х
        res[i] = 'x'

    else:
        if a[i + 1] % 2 == 1:  # разной четности, +
            counter += 1
    if tag == -1 and a[i] % 2 != 0:
        tag = i

if counter % 2:  # нечётное число нч групп, все ок
    print(''.join(res))

else:
    if res[tag] == '+':
        res[tag] = 'x'  # чётное число нч групп, заменим знаки
    else:
        res[tag] = '+'
    print(''.join(res))
