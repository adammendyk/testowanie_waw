from math import pi


# def circle_area(r):
#     if type(r) not in [int, float]:
#         return 'podales nieprawidlowy typ warteosci. wpisz liczbe'
#     elif r < 0:
#         return 'kolo o takim promieniu nie istnieje'
#     else:
#         return pi*r**2


# print(circle_area(1))
# print(circle_area(-0))
# print(circle_area(-1))
# print(circle_area(2+5j))
# print(circle_area(True))
# print(circle_area('asd'))


def circle_area(r):
    try:
        if r < 0:
            raise Exception('promien nie moze byc ujemny')
        return pi*r**2
    except:  # tu nalezy wpisac np. TypeError, ValueError itd.
        return 'cos poszlo nie tak'


print(circle_area(1))
print(circle_area(-0))
print(circle_area(-1))
print(circle_area(2+5j))
print(circle_area(True))
print(circle_area('asd'))
