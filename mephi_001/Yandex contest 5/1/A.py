# p, v = map(int, input().split())
# q, m = map(int, input().split())
#
# if v == 0:
#     a_v = 0
# else:
#     a_v = 1
# if m == 0:
#     a_m = 0
# else:
#     a_m = 1
# if v * m > 0:
#     if q < p:
#         expr = q + m - p + v
#         if expr < 0:
#             res = 2 * m * a_m + 2 * v * a_v + a_v + a_m
#         elif expr == 0:
#             res = 2 * m * a_m + 2 * v * a_v + a_m + a_v - 1
#         else:
#             res = 2 * m * a_m + 2 * v * a_v + a_m + a_v - 1 - expr
#     elif p < q:
#         p, q = q, p
#         v, m = m, v
#         a_v, a_m = a_m, a_v
#         expr = q + m - p + v
#         if expr < 0:
#             res = 2 * m * a_m + 2 * v * a_v + a_v + a_m
#         elif expr == 0:
#             res = 2 * m * a_m + 2 * v * a_v + a_m + a_v - 1
#         else:
#             res = 2 * m * a_m + 2 * v * a_v + a_m + a_v - 1 - expr
#     else:
#         res = max(v, m) * 2 + 1
# else:
#     res = 0
# print(res)

p, v = map(int, input().split())
q, m = map(int, input().split())

if q < p:
    expr = q + m - p + v
    if expr < 0:
        res = 2 * m + 2 * v + 2
    elif expr == 0:
        res = 2 * m + 2 * v + 1
    else:
        res = 2 * m + 2 * v + 1 - expr
elif p < q:
    p, q = q, p
    v, m = m, v
    expr = q + m - p + v
    if expr < 0:
        res = 2 * m + 2 * v + 2
    elif expr == 0:
        res = 2 * m + 2 * v + 1
    else:
        res = 2 * m + 2 * v + 1 - expr
else:
    res = max(v, m) * 2 + 1
if q + m > p + v:
	res = 2 * m + 1
print(res)