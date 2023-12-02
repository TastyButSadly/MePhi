import random

m, n, k = map(int, input().split())
st_d = {"m": m, "n": n, "k": k}


def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)


def comb(n, k):  # n! / (k! * (n - k)!
    return (fact(n) / (fact(k) * fact(n - k)))


def prob(st_d):
    m = st_d['m']
    n = st_d['n']
    k = st_d['k']

    tot = comb(m, n + k)
    com = comb(m - k - n, k)

    return (com / tot)


def real_prob(st_d):
    m = st_d['m']
    n = st_d['n']
    k = st_d['k']

    att = 1000  # число попыток
    count = 0  # счетчик

    for _ in range(att):
        number = random.choices(range(10), k=m)  # генерация

        if number.count(0) == k and number.count(1) == n:  # проверка
            count += 1

    return count / att


# print("Точное решение:       ", round(prob(st_d), 6),
#       "\nВычисленное значение: ", round(real_prob(st_d), 6))
print("Точное решение:       ", prob(st_d),
      "\nВычисленное значение: ", real_prob(st_d))
