import pytest
from points import Point
from circles import Circle
import math

class TestSets:

    @pytest.fixture(scope='class')
    def c1(self):
        return Circle(2, 1, 2)

    @pytest.fixture(scope='class')
    def c2(self):
        return Circle(5, 1, 1)

    def test_c(self):
        pytest.raises(ValueError, Circle, 1, 1, -1)

    def test_from_points(self, c1, c2):
        assert Circle.from_points((Point(0, 1), Point(2, -1), Point(4, 1))) \
               == c1
        assert Circle.from_points((Point(4, 1), Point(5, 2), Point(5, 0))) \
               == c2

    def test_repr(self, c1, c2):
        assert repr(c1) == 'Circle(2, 1, 2)'
        assert repr(c2) == 'Circle(5, 1, 1)'

    def test_eq(self, c1, c2):
        assert c1 == c1

    def test_ne(self, c1, c2):
        assert c1 != c2

    def test_area(self, c1, c2):
        assert c1.area() == 4 * math.pi
        assert c2.area() == math.pi

    def test_cover(self, c1, c2):
        assert c1.cover(c2) == Circle(3, 1, 3)

    def test_new_properties(self, c1, c2):
        assert c1.top == 3
        assert c2.left == 4
        assert c1.bottom == -1
        assert c2.right == 6
        assert c1.width == 4
        assert c2.height == 2
        assert c1.bottomleft == Point(0, -1)
        assert c2.bottomright == Point(6, 0)
        assert c1.topright == Point(4, 3)
        assert c2.topleft == Point(4, 2)

    def test_move(self, c1, c2):
        assert c1.move(5, 5) == Circle(7, 6, 2)

    def test_new_move(self, c1, c2):
        assert c2.new_move(-1, 0) == Circle(4, 1, 1)
        assert c2 == Circle(5, 1, 1)
