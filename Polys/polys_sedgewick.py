from itertools import zip_longest
#from functools import reduce

class Poly:
    '''A class representing polynomials. A polynomial needs its degree n and a
    coefficient a_n.'''

    def __init__(self, c=0, n=0):
        '''Constructor. A polynomial is initailized: p = Poly(a_n, n).'''
        if n < 0:
            raise ValueError('invalid degree')
        if n > 0 and c == 0:
            raise ValueError('invalid coefficient')
        self.size = n + 1
        self.poly = self.size * [0]
        self.poly[self.size-1] = c
        #self.poly[n] = c

    @classmethod
    def from_iterable(cls, iterable):
        '''Creating a polynomial from an iterable with coefficients in order:
        a_0, a_1, ..., a_n.'''
        polyit = cls()
        polyit.poly = list(iterable)
        polyit.size = len(polyit.poly)
        return polyit

    def __str__(self):
        '''Printing a polynomial.'''
        #return str(Poly.cutzeros(self).poly)
        return str(self.poly)

    def __repr__(self):
        '''Printing a polynomial class instance.'''
        #self = Poly.cutzeros(self)
        if self.size == 1:
            return 'Poly({}, {})'.format(self.poly[-1], 0)
        else:
            r = '('
            for n, c in enumerate(self.poly):
                if c != 0:
                    r += 'Poly({}, {}), '.format(c, n)
            r = r[:-2]
            r += ')'
            return r

    def __getitem__(self, idx):
        '''Accessing an item.'''
        if isinstance(idx, int) and (idx < self.size):
            return self.poly[idx]
        else:
            raise IndexError('niepoprawny indeks')

    def __setitem__(self, idx, val):
        '''Setting an item.'''
        if isinstance(idx, int) and val != 0:
            if idx >= self.size:
                self.poly.extend([0] * (idx - self.size))
                self.poly.append(val)
                self.size = idx + 1
            else:
                self.poly[idx] = val
        else:
            raise ValueError('niepoprawne dane')

    def __add__(self, other):
        '''Adding two polynomials.'''
        polysum = Poly()
        if isinstance(other, Poly):
            polysum.poly = [sum(t) for t in zip_longest(self.poly, other.poly,
                                                        fillvalue=0)]
            polysum.size = max(self.size, other.size)
        else:
            polysum.poly = self.poly
            polysum.poly[0] += other
            polysum.size = self.size
        return Poly.cutzeros(polysum)

    __radd__ = __add__

    def __sub__(self, other):
        '''Subtracting two polynomials.'''
        polysub = Poly()
        if isinstance(other, Poly):
            polysub.poly = [t1-t2 for t1, t2 in zip_longest(self.poly,
                                                            other.poly,
                                                            fillvalue=0)]
            polysub.size = max(self.size, other.size)
        else:
            polysub.poly = self.poly
            polysub.poly[0] -= other
            polysub.size = self.size
        return Poly.cutzeros(polysub)

    def __rsub__(self, other):
        polyrsub = Poly()
        polyrsub.poly = [-coeff for coeff in self.poly]
        polyrsub.poly[0] += other
        polyrsub.size = self.size
        return Poly.cutzeros(polyrsub)       

    def __mul__(self, other):
        '''Multiplying two polynomials.'''
        polymul = Poly()
        if isinstance(other, Poly):
            poly1 = self.poly
            poly2 = other.poly
            polymul.size = self.size + other.size - 1
            polymul.poly = [0] * polymul.size
            for i, c1 in enumerate(poly1):
                for j, c2 in enumerate(poly2):
                    polymul.poly[i + j] += c1 * c2
        else:
            polymul.poly = self.poly
            polymul.size = self.size
            for i in range(self.size):
                polymul.poly[i] *= other
        return Poly.cutzeros(polymul)

    __rmul__ = __mul__

    def __pos__(self):
        '''A +polynomial.'''
        return Poly.cutzeros(self)

    def __neg__(self):
        '''A -polynomial.'''
        polyneg = Poly()
        polyneg.poly = [-coeff for coeff in self.poly]
        polyneg.size = self.size
        return Poly.cutzeros(polyneg)
    
    def is_zero(self):
        '''Checking if all coeffcients are zero.'''
        return all(c == 0 for c in self.poly)

    def __eq__(self, other):
        '''Comparing two polynomials.'''
        poly1 = Poly.cutzeros(self).poly
        poly2 = Poly.cutzeros(other).poly
        return all(c1 == c2 for (c1, c2) in zip_longest(poly1, poly2,
                                                        fillvalue=0))

    def __ne__(self, other):
        return not self == other

    def eval(self, x):
        '''Evaluating a polynomial.'''
        result = 0
        for c in reversed(self.poly):
            result = result * x + c
        return result
        #return reduce(lambda a, b: a * x + b, reversed(self.poly))

    def __pow__(self, n):
        '''Powering a polynomial.'''
        polypow = Poly(c=1, n=0)
        for i in range(n):
            polypow *= self
        #polypow.size = (self.size-1) * n
        return Poly.cutzeros(polypow)

    def combine(self, other):
        '''Combining two polynomials.'''
        polycomb = Poly(c=0, n=0)
        for c in reversed(self.poly):
            polycomb = polycomb * other + Poly(c)
        polycomb.size = (self.size-1) * (other.size-1) + 1
        return Poly.cutzeros(polycomb)

    def differentiate(self):
        '''Differentiating a polynomial.'''
        polydiff = Poly()
        polydiff.poly = [self.poly[i] * i for i in range(1, self.size)]
        polydiff.size = self.size - 1
        return Poly.cutzeros(polydiff)  

    def integrate(self):
        '''Integrating a polynomial.'''
        polyint = Poly()
        polyint.poly = [self.poly[i] / (i+1) for i in range(self.size)]
        polyint.poly = [0] + polyint.poly
        polyint.size = self.size + 1
        return Poly.cutzeros(polyint)

    def __len__(self):
        '''Length of a polynomial.'''
        return self.size

    def __call__(self, x):
        '''Evaluating a polynomial or combining two polynomials.'''
        if isinstance(x, (int, float)):
            return self.eval(x)
        if isinstance(x, Poly):
            return self.combine(x)

    def __iter__(self):
        return self

    def __next__(self):
        if self.size == 0:
            raise StopIteration
        self.size -= 1
        return self.poly[-self.size-1]

    def __reversed__(self):
        polyrev = Poly()
        polyrev.poly = list(reversed(self.poly))
        polyrev.size = self.size
        return polyrev

    def cutzeros(self):
        while self.poly[-1] == 0 and self.size > 1:
            self.poly.pop()
            self.size -= 1
        return self
