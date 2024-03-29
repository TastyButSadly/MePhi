from sys import exit
string_1 = [i for i in input()]
string_2 = [i for i in input()]
if len(string_1) != len(string_2):
    print('NO')
    exit()

letter_counter = {i: 0 for i in string_1}

for i, j in zip(string_1, string_2):
    letter_counter[i] += 1
    if j in letter_counter:
        letter_counter[j] -= 1
    else:
        print('NO')
        exit()

for i in letter_counter:
    if letter_counter[i] != 0:
        print('NO')
        exit()
print('YES')


