


class Square(object):
    def __init__(self, side):
        self._side = side

    @property
    def area(self):
        return self._side * self._side

    @property
    def perimeter(self):
        return self._side * 4


if __name__ == "__main__":
    s1 = Square(5)
    assert s1.area == 25
    assert s1.perimeter == 20
