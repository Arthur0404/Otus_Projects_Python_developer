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


def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def filter_numbers(new_list, new_type):
    if new_type == "odd":
        return list(filter(new_odd, new_list))
    elif new_type == "even":
        return list(filter(new_even, new_list))
    elif new_type == "prime":
        return list(filter(IsPrime, new_list))
