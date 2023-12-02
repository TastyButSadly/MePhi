
def collatz(n):
    if type(n) == 'int':
        return None

    sequence = [n]

    def collatz_rec(x):
        if x == 1:
            return
        elif x % 2 == 0:
            n_value = x // 2
        else:
            n_value = 3 * x + 1
        sequence.append(n_value)
        collatz_rec(n_value)
    collatz_rec(n)
    return sequence


n = int(input())

print(collatz(n))
