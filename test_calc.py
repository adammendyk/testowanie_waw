import unittest


class testAdd(unittest.TestCase):
    '''
    Tests the add and subtract function from calc lib
    '''

    def test_plus_int(self):
        assert calc.plus(3, 6) == 3 + 6
        assert calc.plus(-2, 4) == -2 + 4
        assert calc.plus(0, 0) == 0 + 0
        assert calc.plus(-5, -5) == -5 + (-5)
        assert calc.plus(-2, 0) == -2 + 0

    def test_minus(self):
        assert calc.minus(3, 6) == 3 - 6
        assert calc.minus(-2, 4) == -2 - 4
        assert calc.minus(0, 0) == 0 - 0
        assert calc.minus(-5, -5) == -5 - (-5)
        assert calc.minus(-2, 0) == -2 - 0


if __name__ == 'main':
    unittest.main()
