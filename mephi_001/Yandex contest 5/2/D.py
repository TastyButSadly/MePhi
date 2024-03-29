N = int(input())
coord = []
for i in range(N):
    coord.append(list(map(int, input().split())))

counter = 0
for cell in coord:
    # up
    x = cell[0]
    y = cell[1]
    if not [x, y + 1] in coord:
        counter += 1
    if not [x, y - 1] in coord:
        counter += 1
    if not [x + 1, y] in coord:
        counter += 1
    if not [x - 1, y] in coord:
        counter += 1
print(counter)
