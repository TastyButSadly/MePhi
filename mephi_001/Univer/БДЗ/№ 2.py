# import sys
#
#
# # Function to return the minimum
# # number of cubes whose sum is k
# def MinOfCubedDP(k):
#     cube_list = [0] * (k + 1)
#     j = 1
#     t = 1
#     cube_list[0] = 0
#     for i in range(1, k + 1):
#         cube_list[i] = sys.maxsize
#
#         # While current perfect cube
#         # is less than current element
#         while (j <= i):
#             if (j == i):
#                 cube_list[i] = 1  # perfect cube
#             # i = (i - 1) + 1^3
#             elif (cube_list[i] > cube_list[i - j]):
#                 cube_list[i] = cube_list[i - j] + 1
#
#             # Next perfect cube
#             t += 1
#             j = t * t * t
#
#         # Re-initialization for next element
#         t = 1
#         j = 1
#     return cube_list[k]
#
#
# # Driver code
# num = 8
#
# print(MinOfCubedDP(num))
# from math import ceil
#
# def getMinCubes(n):
#     # Create a dynamic programming table
#     # to store cube and getMinCubes table
#     # for base case entries
#     dp = [0, 1, 1, 1]
#
#     # getMinCubes rest of the table
#     # using recursive formula
#     for i in range(8, n + 1):
#         # max value is i as i can always
#         # be represented as 1 * 1 * 1 + 1 * 1 * 1 + ...
#         dp.append(i)
#
#         # Go through all smaller numbers
#         # to recursively find minimum
#         for x in range(1, int(ceil(i ** (1/3))) + 1):
#             temp = x ** 3
#             if temp > i:
#                 break
#             else:
#                 dp[i] = min(dp[i], 1 + dp[i - temp])
#
#     # Store result
#     return dp[n]
#
# # Driver code
# print(getMinCubes(16))


def get_min_squares(n):

    if n <= 3:
        return n

    res = n

    for i in range(1, n + 1):
        temp = i * i
        if temp > n:
            break
        else:
            res = min(res, 1 + get_min_squares(n - temp))

    return res


print(get_min_squares(8))
