k = int(input())
tag = 1
for i in range(k):
    x_i, y_i = map(int, input().split(' '))
    if tag:
        x_min = x_i
        x_max = x_i
        y_min = y_i
        y_max = y_i
        tag = 0
    if x_i < x_min:
        x_min = x_i
    if x_i > x_max:
        x_max = x_i
    if y_i < y_min:
        y_min = y_i
    if y_i > y_max:
        y_max = y_i
print(x_min, y_min, x_max, y_max)