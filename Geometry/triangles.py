from points import Point

class Triangle:
    '''A class representing triangles on a plane. A triangle is defined by
    giving three vertices.'''

    def __init__(self, x1, y1, x2, y2, x3, y3):
        '''Constructor. A triangle is initialized:
        t = Triangle(x1, y1, x2, y2, x3, y3).'''
        if (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1):
            self.p1 = Point(x1, y1)
            self.p2 = Point(x2, y2)
            self.p3 = Point(x3, y3)
        else:
            raise ValueError('collinear points')

    @classmethod
    def from_points(cls, points):
        '''Creating a triangle from a list of three point.'''
        p1, p2, p3 = points
        triangle = cls(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y)
        return triangle

    def __str__(self):
        '''Printing points representing triangle vertices.'''
        return '[{}, {}, {}]'.format(self.p1, self.p2, self.p3)
    
    def __repr__(self):
        '''Printing an instance of a Triangle class.'''
        return 'Triangle({}, {}, {}, {}, {}, {})'.format(self.p1.x, self.p1.y,
                                                         self.p2.x, self.p2.y,
                                                         self.p3.x, self.p3.y)

    def __eq__(self, other):
        '''Comparing two triangles.'''
        return {self.p1, self.p2, self.p3} == {other.p1, other.p2, other.p3}

    def __ne__(self, other):
        return not self == other

    @property
    def center(self):
        '''Center of a triangle.'''
        return (self.p1 + self.p2 + self.p3) / 3.0

    @center.setter
    def center(self, point):
        x, y = self.center.x, self.center.y
        self.move(point[0]-x, point[1]-y)
    
    def area(self):
        return abs(((self.p1.x * (self.p2.y-self.p3.y) +\
                     self.p2.x * (self.p3.y-self.p1.y) +\
                     self.p3.x * (self.p1.y-self.p2.y))) / 2)

    def move(self, x, y):
        '''Moving an existing triangle.'''
        self.p1 += Point(x, y)
        self.p2 += Point(x, y)
        self.p3 += Point(x, y)

    def new_move(self, x, y):
        '''Creating a new triangle by moving an old one.'''
        import copy
        other = copy.deepcopy(self)
        other.p1 += Point(x, y)
        other.p2 += Point(x, y)
        other.p3 += Point(x, y)
        return other

    def make4(self):
        '''Dividing a triangle into 4 triangles of the same sizes.'''
        p4 = (self.p1 + self.p2) / 2
        p5 = (self.p2 + self.p3) / 2
        p6 = (self.p1 + self.p3) / 2
        return (Triangle(self.p1.x, self.p1.y, p4.x, p4.y, p6.x, p6.y),
                Triangle(p4.x, p4.y, p5.x, p5.y, p6.x, p6.y),
                Triangle(p6.x, p6.y, p5.x, p5.y, self.p3.x, self.p3.y),
                Triangle(p4.x, p4.y, self.p2.x, self.p2.y, p5.x, p5.y))

    @property
    def top(self):
        return max(self.p1.y, self.p2.y, self.p3.y)
    
    @property
    def left(self):
        return min(self.p1.x, self.p2.x, self.p3.x)

    @property
    def bottom(self):
        return min(self.p1.y, self.p2.y, self.p3.y)

    @property
    def right(self):
        return max(self.p1.x, self.p2.x, self.p3.x)

    @property
    def width(self):
        return self.right - self.left

    @property
    def height(self):
        return self.top - self.bottom

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def topleft(self):
        return Point(self.left, self.top)
