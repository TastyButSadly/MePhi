n = int(input())
nummers = map(int, input().split())
nummer_count = {}
for i in nummers:
    if i in nummer_count:
        nummer_count[i] += 1
    else:
        nummer_count[i] = 1

tag_0 = 1

for i in nummer_count:

    summ_i_left = nummer_count[i]
    summ_i_right = nummer_count[i]
    if i - 1 in nummer_count:
        summ_i_left += nummer_count[i - 1]
    if i + 1 in nummer_count:
        summ_i_right += nummer_count[i + 1]

    max_i = max(summ_i_left, summ_i_right)
    if tag_0:
        # i_max = i
        summ_max = max_i
        tag_0 = 0
    else:
        if max_i > summ_max:
            summ_max = max_i

print(n - summ_max)
# for i in nummer_count:
#     if nummer_count[i] > 1:
#         print(nummer_count[i])
#         print(i)