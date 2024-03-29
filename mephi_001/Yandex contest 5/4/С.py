n, m = map(int, input().split())
orks_list = list(map(int, input().split()))

pr_sums = [0] * (n + 1)
for i in range(1, n + 1):
    pr_sums[i] = pr_sums[i - 1] + orks_list[i - 1]


def search(l, s):
    left, right = 0, n - l + 1
    while left < right:
        mid = (left + right) // 2
        total_orcs = pr_sums[mid + l] - pr_sums[mid]
        if total_orcs < s:
            left = mid + 1
        else:
            right = mid

    if left < n - l + 1 and pr_sums[left + l] - pr_sums[left] == s:
        return left + 1
    else:
        return -1


for _ in range(m):
    l, s = map(int, input().split())
    result = search(l, s)
    print(result)
