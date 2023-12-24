from math import trunc


def solve_cube_sum(n, result_list, max_attempts):
    sum = n
    attempts_cur = max_attempts  # оставшееся количество попыток

    while sum > 0:  # пока число не разложено
        if attempts_cur > 0:
            current_cube_root = trunc(float((sum ** (1 / 3)))) - 1
            attempts_cur -= 1
        else:
            current_cube_root = trunc(float((sum ** (1 / 3))))

        if current_cube_root <= 1:
            current_cube_root = trunc(float((sum ** (1 / 3))))

        if attempts_cur > current_cube_root:
            return 0

        result_list.append(current_cube_root ** 3)
        sum -= current_cube_root ** 3

        if len(result_list) > 7:
            result_list.clear()
            solve_cube_sum(n, result_list, max_attempts + 1)

    return result_list


result_list = []
max_attempts = 8
input_number = int(input())
print(solve_cube_sum(input_number, result_list, max_attempts))
# count_num = 0
# for i in range(1, 5001):
#     if solve_cube_sum(i, result_list, 8):
#         count_num += 1
#
# print(count_num)
