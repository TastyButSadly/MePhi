def bin_search(arr, num):
    l_p = 0
    r_p = len(arr) - 1
    while l_p <= r_p:
        mid = (l_p + r_p) // 2
        if arr[mid] == num:
            return mid
        if arr[mid] < num:
            l_p = mid
        else:
            r_p = mid
print(bin_search([1,2,3,4,5,6,7,8], 3))