def min_points(points):
    point_set = set(points)
    added_points = []
    for p1 in point_set:
        for p2 in point_set:
            if p1 == p2:
                continue
            dx, dy = p2[0] - p1[0], p2[1] - p1[1]
            p3 = (p1[0] - dy, p1[1] + dx)
            p4 = (p2[0] - dy, p2[1] + dx)
            if p3 in point_set and p4 in point_set:
                return 0, []
            if p3 not in point_set and p4 not in point_set:
                continue
            if p3 not in point_set:
                added_points.append(p3)
            else:
                added_points.append(p4)
            return 1, added_points
    return 2, [(p1[0] + dx, p1[1] + dy), (p2[0] - dy, p2[1] + dx)]

N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

K, added_points = min_points(points)
print(K)
for point in added_points:
    print(*point)
