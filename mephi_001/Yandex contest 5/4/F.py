def main():
    w, h, n = map(int, input().split())
    a = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append((x, y))
    a.sort()
    left, right = 1, min(w, h)

    while left < right:
        middle = (left + right) // 2
        if check(w, h, a, middle):
            right = middle
        else:
            left = middle + 1

    print(left)


def check(w, h, a, c):
    hor = vert = 0
    for x, y in a:
        if x <= c or y <= c or x + c >= w or y + c >= h:
            if x == 1 or x == w - c or y == 1 or y == h - c:
                return False
            hor += 1
        else:
            vert += 1
    return hor >= 2 and vert >= 2


main()