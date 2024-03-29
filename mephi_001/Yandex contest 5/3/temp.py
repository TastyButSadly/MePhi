n = int(input())

d_0 = 1
d_end = 1
while n > d_end:
    d_0 += 1
    d_end += d_0

d_pos = n - (d_end - d_0)
numerator = d_0 - d_pos + 1
denominator = d_pos
if d_0 % 2 == 0:
    numerator, denominator = denominator, numerator

print(f"{denominator}/{numerator}")

n = int(input())

diagonal_start = int(((8 * n - 7) ** 0.5 + 1) / 2)
diagonal_position = n - (diagonal_start * (diagonal_start - 1)) // 2
numerator = diagonal_start - diagonal_position + 1
denominator = diagonal_position
if diagonal_start % 2 == 0:
    numerator, denominator = denominator, numerator

print(f"{denominator}/{numerator}")
