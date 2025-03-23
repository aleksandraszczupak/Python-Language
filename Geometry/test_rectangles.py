import pytest
from points import Point
from rectangles import Rectangle

@pytest.fixture
def r1():
    return Rectangle(-1, 1, 2, 3)

@pytest.fixture
def r2():
    return Rectangle(1, 2, 5, 5)

@pytest.fixture
def r3():
    return Rectangle(4, 3, 6, 6)

'''def test_r(r1, r2, r3):
    pytest.raises(ValueError, Rectangle, 5, 5, 1, 2)
    pytest.raises(ValueError, Rectangle, 1, 2, 1, 2)'''

def test_from_points(r1, r2, r3):
    assert Rectangle.from_points((Point(-1, 1), Point(2, 3))) == r1
    pytest.raises(ValueError, Rectangle.from_points, (Point(2, 3), Point(-1, 1),
                                                      Point(1, 1)))

def test_str(r1, r2, r3):
    assert str(r1) == '[(-1, 1), (2, 3)]'
    assert str(r2) == '[(1, 2), (5, 5)]'

def test_repr(r1, r2, r3):
    assert repr(r2) == 'Rectangle(1, 2, 5, 5)'

def test_eq(r1, r2, r3):
    assert (r1 == r2) == False
    assert (r1 == r1) == True

def test_area(r1, r2, r3):
    assert r1.area() == 6
    assert r2.area() == 12

def test_intersection(r1, r2, r3):
    assert r1.intersection(r2) == Rectangle(1, 2, 2, 3)
    assert r3.intersection(r2) == Rectangle(4, 3, 5, 5)
    with pytest.raises(ValueError):
        r1.intersection(Rectangle(3, 3, 5, 4))
    with pytest.raises(ValueError):
        r1.intersection(Rectangle(4, 3, 6, 6))

def test_cover(r1, r2, r3):
    assert r1.cover(r2) == Rectangle(-1, 1, 5, 5)
    assert r2.cover(r1) == Rectangle(-1, 1, 5, 5)

def test_make4(r1, r2, r3):
    assert r1.make4() == (Rectangle(-1, 2.0, 0.5, 3),
                          Rectangle(0.5, 2.0, 2, 3),
                          Rectangle(-1, 1, 0.5, 2.0),
                          Rectangle(0.5, 1, 3, 2.0))
    assert r2.make4() == (Rectangle(1, 3.5, 3, 5),
                          Rectangle(3, 3.5, 5, 5),
                          Rectangle(1, 2, 3, 3.5),
                          Rectangle(3, 2, 5, 3.5))

def test_properties(r1, r2, r3):
    assert r1.top == 3
    assert r1.left == -1
    assert r2.bottom == 2
    assert r2.right == 5
    assert r3.width == 2
    assert r3.height == 3
    assert r2.bottomleft == Point(1, 2)
    assert r2.bottomright == Point(5, 2)
    assert r1.topright == Point(2, 3)
    assert r1.topleft == Point(-1, 3)

def test_center(r1, r2, r3):
    assert r1.center == Point(0.5, 2)
    assert r2.center == Point(3, 3.5)
    r2.center = (4, 0.5)
    assert r2 == Rectangle(2, -1, 6, 2) 

def test_move(r1, r2, r3):
    r3.move(2, -3)
    assert r3 == Rectangle(6, 0, 8, 3)

def test_new_move(r1, r2, r3):
    assert r1.new_move(-1, 1) == Rectangle(-2, 2, 1, 4)
    assert r1 == Rectangle(-1, 1, 2, 3)
