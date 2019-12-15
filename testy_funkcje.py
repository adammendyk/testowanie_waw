import funkcje
from math import pi
import pytest


def test_add_no():
    assert funkcje.add_no(7, 3) == 10, 'FAILED'
    assert funkcje.add_no(7, -1) == 6, 'FAILED'
    assert round(funkcje.add_no(4.3, 5.6), 1) == 9.9, 'FAILED'


def test_product():
    assert funkcje.product(3, 3) == 3*3, 'FAILED'
    assert funkcje.product(5, 4) == 5*4, 'FAILED'
    assert funkcje.product(0, 3) == 0*3, 'FAILED'


def test_is_palindrome():
    assert funkcje.is_palindrome('kajak'), 'FAILED'
    assert funkcje.is_palindrome('anna'), 'FAILED'
    assert funkcje.is_palindrome('akllka'), 'FAILED'


def test_circle_ares():
    assert funkcje.circle_area(1) == pi
    assert funkcje.circle_area(0) == 0
    assert funkcje.circle_area(3) == pi*3**2


def test_value():
    with pytest.raises(ValueError):
        funkcje.circle_area(-2)


def test_type():
    with pytest.raises(TypeError):
        funkcje.circle_area('asd')


# test_add_no()
# test_product()
# test_is_palindrome()
