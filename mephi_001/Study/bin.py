def bin_search(arr, value):
    l_p = 0
    r_p = len(arr) - 1
    while l_p <= r_p:
        mid = int((l_p + r_p) / 2)
        if value == arr[mid]:
            return mid
        if value > arr[mid]:
            l_p = mid
        else:
            r_p = mid


print(bin_search(arr, 3))
