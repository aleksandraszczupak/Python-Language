import pytest
from points import Point
from triangles import Triangle

t1 = Triangle(1, 1, 3, 3, 3, 1)
t2 = Triangle(4, 2, 5, 4, 6, 1)
t3 = Triangle(2, -2, 4, 1, 5, -1)
t4 = Triangle(3, 3, 1, 1, 3, 1)
t5 = Triangle(6, 1, 5, 4, 2, 4)

def test_t():
    with pytest.raises(ValueError):
        Triangle(1, 1, 2, 2, 3, 3)
    with pytest.raises(ValueError):
        Triangle(4, 2, 6, 1, 2, 3)

def test_from_points():
    assert Triangle.from_points((Point(4, 2), Point(5, 4), Point(6, 1))) == t2
    pytest.raises(ValueError, Triangle.from_points, (Point(4, 2), Point(6, 1), Point(2, 3)))

def test_str():
    assert str(t1) == '[(1, 1), (3, 3), (3, 1)]'

def test_repr():
    assert repr(t2) == 'Triangle(4, 2, 5, 4, 6, 1)'

def test_eq():
    assert t1 == t4

def test_ne():
    assert t1 != t2

def test_area():
    assert t1.area() == 2.0
    assert t2.area() == 2.5

def test_make4():
    assert t2.make4() == (Triangle(4, 2, 9/2, 3, 5, 3/2),
                          Triangle(9/2, 3, 11/2, 5/2, 5, 3/2),
                          Triangle(5, 3/2, 11/2, 5/2, 6, 1),
                          Triangle(9/2, 3, 5, 4, 11/2, 5/2))
    assert t3.make4() == (Triangle(2, -2, 3, -1/2, 7/2, -3/2),
                          Triangle(3, -1/2, 9/2, 0, 7/2, -3/2),
                          Triangle(7/2, -3/2, 9/2, 0, 5, -1),
                          Triangle(3, -1/2, 4, 1, 9/2, 0))

def test_properties():
    assert t1.top == 3
    assert t2.left == 4
    assert t3.bottom == -2
    assert t4.right == 3
    assert t5.width == 4
    assert t1.height == 2
    assert t2.bottomleft == Point(4, 1)
    assert t3.bottomright == Point(5, -2)
    assert t4.topright == Point(3, 3)
    assert t5.topleft == Point(2, 4)

def test_center():
    assert t1.center == Point(7/3, 5/3)
    assert t3.center == Point(11/3, -2/3)
    assert t4.center == Point(7/3, 5/3)

def test_move():
    t3.move(-4, 1)
    assert t3 == Triangle(-2, -1, 0, 2, 1, 0)
    t5.move(0, -1)
    assert t5 == Triangle(6, 0, 5, 3, 2, 3)

def test_new_move():
    assert t3.new_move(-4, 1) == Triangle(-6, 0, -4, 3, -3, 1)
    assert t3 == Triangle(-2, -1, 0, 2, 1, 0)
