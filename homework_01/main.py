"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    return [elem * elem for elem in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def new_odd(y):
    return y % 2 != 0


def new_even(x):
    return x % 2 == 0


def is_prime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def filter_numbers(new_list, new_type):
    if new_type == ODD:
        return list(filter(new_odd, new_list))
    elif new_type == EVEN:
        return list(filter(new_even, new_list))
    elif new_type == PRIME:
        return list(filter(is_prime, new_list))
