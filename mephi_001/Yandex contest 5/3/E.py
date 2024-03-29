numm_dict = {}
n_i = []
list_common = []
for i in range(3):
    n_i.append(int(input()))
    list_common.append(list(set(map(int, input().split()))))


# for k in range(3):
#     n_k = len(set(list_common[k]))
#     for i in range(n_k):
#         list_i = list_common[i]
#         for j in range(len(list_i)):
#             if list_i[j] not in numm_dict:
#                 numm_dict[list_i[j]] = 1
#             else:
#                 numm_dict[list_i[j]] += 1
res_dict = {}
for i in list_common:
    for j in i:
        if j in res_dict:
            res_dict[j] += 1
        else:
            res_dict[j] = 1

print(*sorted([i for i in res_dict if res_dict[i] >= 2]))


