m = []
coord = []
start_m = []
debug = 0
for i in range(8):
    start_m.append(input())

for i in range(0, 8):
    m.append([])
    for j in range(0, 8):
        f = start_m[i][j]
        m[i].append(f)
        if f != '*':
            coord.append([i, j])

counter = 0
points = []
# print(coord)
qw = 0
for i in coord:

    y = i[0]
    x = i[1]

    if m[y][x] == 'B':  # слон
        qw += 1
        x1 = x
        y1 = y

        # вверх вправо
        #
        while not [x1 + 1, y1 + 1][::-1] in coord and 0 <= x1 + 1 <= 7 and 0 <= y1 + 1 <= 7:
            x1 += 1
            y1 += 1
            points.append([y1, x1])
            if debug:
                print(1)
                print(x1, y1)
        #
        # вверх влево
        x1 = x
        y1 = y
        while not [x1 - 1, y1 + 1][::-1] in coord and 0 <= x1 - 1 <= 7 and 0 <= y1 + 1 <= 7:
            x1 -= 1
            y1 += 1
            points.append([y1, x1])
            if debug:
                print(2)
                print(x1, y1)

        # вниз вправо
        x1 = x
        y1 = y
        #
        while not [x1 + 1, y1 - 1][::-1] in coord and 0 <= x1 + 1 <= 7 and 0 <= y1 - 1 <= 7:
            x1 += 1
            y1 -= 1
            points.append([y1, x1])
            if debug:
                print(3)
                print(x1, y1)
        # вниз влево
        x1 = x
        y1 = y
        #
        while not [x1 - 1, y1 - 1][::-1] in coord and 0 <= x1 - 1 <= 7 and 0 <= y1 - 1 <= 7:
            x1 -= 1
            y1 -= 1
            points.append([y1, x1])
            if debug:
                print(4)
                print(x1, y1)

    if m[y][x] == 'R':  # ладья
        x1 = x
        y1 = y

        # вверх
        while not [x1, y1 + 1][::-1] in coord and 0 <= y1 + 1 <= 7:
            y1 += 1
            points.append([y1, x1])

        # влево
        x1 = x
        y1 = y
        while not [x1 - 1, y1][::-1] in coord and 0 <= x1 - 1 <= 7:
            x1 -= 1
            points.append([y1, x1])

        # вправо
        x1 = x
        y1 = y
        while not [x1 + 1, y1][::-1] in coord and 0 <= x1 + 1 <= 7:
            x1 += 1
            points.append([y1, x1])

        # вниз
        x1 = x
        y1 = y
        while not [x1, y1 - 1][::-1] in coord and 0 <= y1 - 1 <= 7:
            y1 -= 1
            points.append([y1, x1])
points += coord
# summa = 0
# print(set(tuple(i) for i in points))
# for i in range(0, 8):
#     print()
#     for j in range(0, 8):
#         if not [i, j] in points:
#             print('-', end='')
#             summa += 1
#         else:
#             print('х', end='')
# print('через матрицу', summa)
# print(len(set(tuple(i) for i in points)))
print(64 - len(set(tuple(i) for i in points)))
