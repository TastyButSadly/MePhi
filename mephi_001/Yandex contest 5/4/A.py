# n = int(input())
# nummers = list(map(int, input().split()))
# k = int(input())
# L_R = []
# for i in range(k):
#     L_R.append(map(int, input().split()))

from bisect import bisect_left, bisect_right


N = int(input())


arr = list(map(int, input().split()))


arr.sort()


K = int(input())


for _ in range(K):

    L, R = map(int, input().split())


    l = bisect_left(arr, L)
    r = bisect_right(arr, R)

    count = r - l


    print(count, end=' ')
