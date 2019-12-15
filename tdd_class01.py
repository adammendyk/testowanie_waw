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


def add_str(a, b):
    return a + b


assert add_str('sd', 'kdj') == 'sd'+'kdj', 'FAILED'
print('PASSED')
assert add_str('sd', 4) == 'sd4', 'FAILED'
print('PASSED')
assert add_str('sd', 'kdj') == 'sd'+'kdj', 'FAILED'
print('PASSED')
