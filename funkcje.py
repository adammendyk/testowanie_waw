from math import pi


def add_no(a, b):
    return a+b


def product(x, y):
    return x*y


def is_palindrome(str):
    str = str.replace(' ', '').lower()
    return str == str[::-1]


def circle_area(r):
    if r < 0:
        raise Exception('The radius cannot be negative')
    if type(r) not in [int, float]:
        raise TypeError('The radius is a non-negative real number')
