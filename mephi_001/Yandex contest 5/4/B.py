# from decimal import Decimal

n = int(input())
k = 0
# occupied_cells = lambda x: Decimal(1) / Decimal(6) * k * (k + Decimal(1)) * (k + Decimal(2)) + (
#             Decimal(1) + k) / Decimal(2) * k - Decimal(1)

occupied = lambda x: k * (k + 1) * (k + 2 )+ (1 + k) * 3 * k - 6

max_k = 0
while True:
    if round(occupied(k), 9) <= 6* n:
        max_k = k
        k += 1

    else:
        # if n > 11705576588885779:
        #     for i in range(5):

        break
print(int(max_k))
