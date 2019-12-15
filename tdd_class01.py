from random import randint


# def div(a, b):
#     return a/b


# x = randint(1, 50)
# y = randint(1, 20)

# # for el in range(5):
# #     if div(x, y) == x/y:
# #         print('PASSED')
# #     else:
# #         raise Exception('FAILED')

# # print(div(x, y)

# assert div(10, 2) == 5, 'FAILED'
# print('PASSED')
# assert div(10, 5) == 2, 'FAILED'
# print('PASSED')

# --- assertion

# def sum_square(x, y):
#     return (x+y)**2


# assert sum_square(3, 2) == (3+2)**2, 'FAILED'
# print('PASSED')
# assert sum_square(3.5, 8) == (3.5+8)**2, 'FAILED'
# print('PASSED')
# assert sum_square(-6, 2) == (-6+2)**2, 'FAILED'
# print('PASSED')
# assert sum_square(0, 0) == (0+0)**2, 'FAILED'
# print('PASSED')


# assercje nie sluza tylko do testowania

# def div(x, y):
#     try:
#         return x / y
#     except ZeroDivisionError:
#         print('can\'t divide by zero')


# def div(x, y):
#     assert y != 0, 'can\'t divide by zero'
#     return x / y


# def add_str(a, b):
#     return a + b


# assert add_str('sd', 'kdj') == 'sd'+'kdj', 'FAILED'
# print('PASSED')
# # assert add_str('sd', 4) == 'sd4', 'FAILED'
# # print('PASSED')
# assert add_str('sd', 'kdj') == 'sd'+'kdj', 'FAILED'
# print('PASSED')

# --- unit testing

def add_no(a, b):
    return a+b


def product(x, y):
    return x*y


def test_add_no():
    assert add_no(7, 3) == 10, 'FAILED'
    assert add_no(7, -1) == 6, 'FAILED'
    assert round(add_no(4.3, 5.6), 1) == 9.9, 'FAILED'


def test_product():
    assert product(3, 3) == 3*3, 'FAILED'
    assert product(5, 4) == 5*4, 'FAILED'
    assert product(0, 3) == 0*3, 'FAILED'


test_add_no()
test_product()
