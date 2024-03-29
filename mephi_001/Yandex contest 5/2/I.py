def ship_move(points, x0):
    res = 0
    reserved = []

    for point in points:
        x = point[0]
        y = point[1]
        for dy in range(0, 100000):
            tag = 1
            for j in (-1, 1):
                if y + dy not in reserved:
                    res += abs(x - x0) + abs(dy)
                    reserved.append(dy * j)
                    tag = 0
            if not tag:
                break

        # for y_i in range(0, 10000):
        #     tag = 1
        #     for j in (-1, 1):
        #         if y_i * j not in reserved:
        #             res += abs(x - x0) + abs(y - y_i * j)
        #             reserved.append(y_i * j)
        #             tag = 0
        #             break
        #     if not tag:
        #         break
    return res


n = int(input())
points = []
x_tot = 0
for _ in range(n):
    x_i, y_i = map(int, input().split())
    points.append([x_i, y_i])
    x_tot += x_i

result = []
for i in range(min(points[0]), max(points[0]) + 1):
    result.append(ship_move(points, i))
print(result)
print(min(result))
