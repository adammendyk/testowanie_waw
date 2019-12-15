from random import randint


def div(a, b):
    return a/b


rand = randint(1, 100)
for x, y in range(50):

    if div(x, y) == x/y:
        print('PASSED')
    else:
        print('FAILED')

# print(div(5, 2) == 2.5)
