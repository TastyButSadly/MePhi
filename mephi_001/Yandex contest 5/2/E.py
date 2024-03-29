n = int(input())
berries = []
good_b = []
for i in range(n):
    s_i = list(map(int, input().split()))
    if s_i[0] > s_i[1]:
        good_b.append(str(i + 1))
    berries.append(s_i)
max_b = max(berries)

tag = bool(str(berries.index(max_b) + 1) not in good_b)

res_ind = (' '.join(good_b)+ ' ' + (str(berries.index(max_b) + 1) + ' ') * tag + ' '.join(
    [str(i + 1) for i in range(len(berries)) if
     i + 1 != berries.index(max_b) + 1 and str(i + 1) not in good_b])).strip()
# print(' '.join(good_b)[1:])
# print(list(res_ind))
res_sum = sum([berries[int(i) - 1][0] for i in list(res_ind.split())])
print(res_sum)
print(res_ind)
# not_in_good_or_max_b = [str(i + 1) for i in range(len(berries)) if
#                         i + 1 != berries.index(max_b) + 1 and str(i + 1) not in good_b]
# print(' '.join(good_b) + ' ' + (str(berries.index(max_b) + 1) + ' ') * tag + ' '.join(not_in_good_or_max_b))
