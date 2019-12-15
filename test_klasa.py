from klasa import Car


def test_car_init():
    car = Car('bmw', 'black')
    assert car.name == 'bmw'


def test_car_change_color():
    car = Car('bmw', 'black')
    assert car.color == 'red'
