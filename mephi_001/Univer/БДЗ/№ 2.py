def decompose_into_cubes(n, max_attempts=8):
    result_list = []
    sum_remaining = n

    for _ in range(max_attempts):
        current_cube_root = int(sum_remaining ** (1 / 3))
        current_cube = current_cube_root ** 3

        result_list.append(current_cube)
        sum_remaining -= current_cube

        if sum_remaining == 0:
            return result_list

    return None


success_pop = 0
upper_lim = 5000  # до какого числа проверяем

for num in range(1, upper_lim + 1):
    decomposition = decompose_into_cubes(num)
    if decomposition:
        print(num, decomposition)
        success_pop += 1
    else:
        print(num)

print(success_pop)
