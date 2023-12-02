arr = [-2, -1, 0, 2, 4, 5, 7, 7]
left = 0
right = len(arr) - 1
result = []

while left <= right:
    if arr[left] ** 2 < arr[right] ** 2:
        result.append(arr[right] ** 2)
        right -= 1
    else:
        result.append(arr[right] ** 2)
        left += 1
result.reverse()
print(result)

# arr = [-5, -3, 0, 1, 3, 6]
#
# left = 0
# right = len(arr) - 1
#
# res = []
# while left <= right:
#     if arr[left]**2 > arr[right]**2:
#         res.append(arr[left]**2)
#         left += 1
#     else:
#         res.append(arr[right]**2)
#         right -= 1
#
# res.reverse()
#
# print(res)
