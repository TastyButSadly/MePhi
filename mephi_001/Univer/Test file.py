def decomp(n, max_attempts=8):
    c = []
    r = n

    for _ in range(max_attempts):
        rt = int(r ** (1 / 3))
        cube = rt ** 3

        c.append(cube)
        r -= cube

        if r == 0:
            return c

    return None

def count_success(limit):
    count = 0

    for num in range(1, limit + 1):
        decomp_result = decomp(num)
        if decomp_result:
            count += 1

    return count

lim = 5000
success_count = count_success(lim)

print(success_count)
