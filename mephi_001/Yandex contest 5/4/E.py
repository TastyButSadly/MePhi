def nth_fraction(n):
    row = 1
    while (row * (row + 1)) // 2 < n:
        row += 1
    col = n - (row * (row - 1)) // 2

    if row == col:
        return row, row

    if row > col:
        return col + 1, row

    return row, col + 1


n = int(input())

numerator, denominator = nth_fraction(n)

print(f"{numerator}/{denominator}")
