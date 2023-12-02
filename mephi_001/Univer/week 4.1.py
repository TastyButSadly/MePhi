import random
import string


def password_g(n):
    pass_el = string.ascii_letters + string.punctuation + string.digits

    password = ''.join(random.choice(pass_el) for _ in range(n))
    return (password)


# n = int(input("Введите желаемую длину пароля\n"))

n = 10
print(password_g(n))
