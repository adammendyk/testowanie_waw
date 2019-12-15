def add_no(a, b):
    return a+b


def product(x, y):
    return x*y


def is_palindrome(str):
    str = str.replace(' ', '').lower()
    return str == str[::-1]
