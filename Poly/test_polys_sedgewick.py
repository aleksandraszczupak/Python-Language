import unittest
from polys_sedgewick import Poly

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = Poly(-7, 6) # W(x) = 1 + 2x - 3x^3 + 5x^4 - 7x^6
        self.p1[0], self.p1[1], self.p1[3], self.p1[4] = 1, 2, -3, 5
        self.p2 = Poly(-3, 2) # W(x) = 2 - 3x^2
        self.p2[0] = 2
        self.p3 = Poly(-7, 3) # W(x) = 5x - 7x^3
        self.p3[1] = 5
        self.p4 = Poly(-7, 3) # W(x) = 5 - 7x^3
        self.p4[0] = 5
        self.p5 = Poly(0, 0) # W(x) = 0
        self.p6 = Poly(1, 1) # W(x) = 2 + x
        self.p6[0] = 2
        with self.assertRaises(ValueError):
            self.err1 = Poly(9, -1)
        with self.assertRaises(ValueError):
            self.err2 = Poly(0, 5)

    def test_from_iterable(self):
        self.assertEqual(Poly.from_iterable([0, 5, 0, -7]).poly, self.p3.poly)

    def test_str(self):
        self.assertEqual(str(self.p1), '[1, 2, 0, -3, 5, 0, -7]')
        self.assertEqual(str(self.p3), '[0, 5, 0, -7]')
        self.assertEqual(str(self.p5), '[0]')
        self.assertEqual(str(self.p6), '[2, 1]')

    def test_repr(self):
        self.assertEqual(repr(self.p1),
        '(Poly(1, 0), Poly(2, 1), Poly(-3, 3), Poly(5, 4), Poly(-7, 6))')
        self.assertEqual(repr(self.p3),
        '(Poly(5, 1), Poly(-7, 3))')
        self.assertEqual(repr(self.p5), 'Poly(0, 0)')
        self.assertEqual(repr(self.p6), '(Poly(2, 0), Poly(1, 1))')
        self.assertEqual(repr(self.p2.combine(self.p3)),
        '(Poly(2, 0), Poly(-75, 2), Poly(210, 4), Poly(-147, 6))')

    def test_getitem(self):
        self.assertTrue(self.p1[0] == 1)
        self.assertTrue(self.p2[2] == -3)
        with self.assertRaises(IndexError):
            self.p3[4]
        with self.assertRaises(IndexError):
            self.p5[0.5]
        with self.assertRaises(IndexError):
            self.p6[3]

    def test_setitem(self):
        self.p1[1] = 5
        self.p2[4] = 6
        self.assertTrue(self.p1.poly, [5, 2, 0, -3, 5, 0, -7])
        self.assertTrue(self.p2.poly, [2, 0, -3, 6])
        self.p6[2] = -7
        self.assertTrue(self.p6.poly, [2, 1, -7])
        self.p6[6] = 11
        self.assertTrue(self.p6.poly, [2, 1, -7, 0, 0, 0, 11])
        self.assertTrue(self.p6.size, 7)
        with self.assertRaises(ValueError):
            self.p1[0.6] = 1
        with self.assertRaises(ValueError):
            self.p1[9] = 0

    def test_add(self):
        self.assertEqual((self.p1+self.p2).poly, [3, 2, -3, -3, 5, 0, -7])
        self.assertEqual((self.p1+self.p2).size, 7)
        self.assertEqual((self.p3+self.p4).poly, [5, 5, 0, -14])
        self.assertEqual((self.p5+self.p6).poly, [2, 1])
        self.assertEqual((self.p2+3).poly, [5, 0, -3])
        self.assertEqual((6+self.p4).poly, [11, 0, 0, -7])
        self.assertEqual((10+self.p3).poly, [10, 5, 0, -7])
        self.assertEqual((10+self.p3).size, 4)

    def test_sub(self):
        self.assertEqual((self.p3-self.p1).poly, [-1, 3, 0, -4, -5, 0, 7])
        self.assertEqual((self.p3-self.p1).size, 7)
        self.assertEqual((self.p6-self.p5).poly, [2, 1])
        self.assertEqual((self.p1-self.p1).poly, [0])
        self.assertEqual((self.p1-self.p1).size, 1)
        self.assertEqual((self.p3-1).poly, [-1, 5, 0, -7])
        self.assertEqual((1-self.p4).poly, [-4, 0, 0, 7])
        
    def test_mul(self):
        self.assertEqual((self.p1*self.p2).poly,
                         [2, 4, -3, -12, 10, 9, -29, 0, 21])
        self.assertEqual((self.p1*self.p4).poly,
                         [5, 10, 0, -22, 11, 0, -14, -35, 0, 49])
        self.assertEqual((self.p1*self.p4).size, 10)
        self.assertEqual((self.p2*self.p6).poly,
                         [4, 2, -6, -3])
        self.assertEqual((self.p1*self.p6).poly,
                         [2, 5, 2, -6, 7, 5, -14, -7])
        self.assertEqual((self.p1*1).poly, self.p1.poly)
        self.assertEqual((self.p2*0.5).poly, [1, 0, -3/2])
        self.assertEqual((self.p2*0.5).size, 3)
        self.assertEqual((-1*self.p6).poly, [-2, -1])
        
    def test_pos(self):
        self.assertEqual(+self.p1, self.p1)
        self.assertEqual((+self.p1).size, self.p1.size)
        self.assertEqual(+self.p2, self.p2)

    def test_neg(self):
        self.assertEqual((-self.p2).poly, [-2, 0, 3])
        self.assertEqual((-self.p5).poly, [0])
        self.assertEqual((-self.p6).poly, [-2, -1])
        self.assertEqual((-self.p6).size, 2)

    def test_eq(self):
        self.assertTrue(self.p1 == self.p1)
        self.assertFalse(self.p1 == self.p2)
        self.assertTrue(self.p6.poly == [2, 1])
        self.assertTrue(self.p5.poly == [0])

    def test_ne(self):
        self.assertFalse(self.p3 != self.p3)
        self.assertTrue(self.p3 != self.p4)

    def test_eval(self):
        self.assertEqual(self.p1.eval(-2), -347)
        self.assertEqual(self.p2.eval(-2), -10)
        self.assertEqual(self.p3.eval(6), -1482)
        self.assertEqual(self.p5.eval(10), 0)

    def test_combine(self):
        self.assertEqual((self.p1.combine(self.p2)).poly,
        [-387, 0, 3654, 0, -14202, 0, 29241, 0, -33615, 0, 20412, 0, -5103])
        self.assertEqual((self.p1.combine(self.p2)).size, 13)
        self.assertEqual((self.p2.combine(self.p3)).poly,
        [2, 0, -75, 0, 210, 0, -147])
        self.assertEqual((self.p2.combine(self.p3)).size, 7)

    def test_pow(self):
        self.assertEqual((self.p2**4).poly,
                         [16, 0, -96, 0, 216, 0, -216, 0, 81])
        self.assertEqual((self.p2**4).size, 9)
        self.assertEqual((self.p4**3).poly,
                         [125, 0, 0, -525, 0, 0, 735, 0, 0, -343])
        self.assertEqual((self.p4**3).size, 10)
        
    def test_differentiate(self):
        self.assertEqual((self.p1.differentiate()).poly, [2, 0, -9, 20, 0, -42])
        self.assertEqual((self.p1.differentiate()).size, 6)
        self.assertEqual((self.p4.differentiate()).poly, [0, 0, -21])
        self.assertEqual((self.p4.differentiate()).size, 3)

    def test_integrate(self):
        self.assertEqual((self.p1.integrate()).poly,
                               [0, 1, 1, 0, -3/4, 1, 0, -1])
        self.assertEqual((self.p1.integrate()).size, 8)
        self.assertEqual((self.p4.integrate()).poly,
                               [0, 5, 0, 0, -7/4])
        self.assertEqual((self.p4.integrate()).size, 5)

    def test_is_zero(self):
        self.assertEqual(self.p3.is_zero(), False)
        self.assertEqual(self.p5.is_zero(), True)

    def test_len(self):
        self.assertTrue(len(self.p1) == 7)
        self.assertTrue(len(self.p5) == 1)
        self.assertTrue(len(self.p6) == 2)
        self.assertTrue(len(self.p1.combine(self.p2)) == 13)

    def test_call(self):
        self.assertEqual(self.p1(-2), -347)
        self.assertEqual((self.p2(self.p3)).poly,
                         [2, 0, -75, 0, 210, 0, -147])

    def test_next(self):
        self.assertEqual(list(self.p1), [1, 2, 0, -3, 5, 0, -7])
        self.assertEqual(list(self.p4.integrate()), [0, 5, 0, 0, -7/4])

    def test_reversed(self):
        self.assertEqual(reversed(self.p1).poly, [-7, 0, 5, -3, 0, 2, 1])
        self.assertEqual(reversed(self.p4.integrate()).poly, [-7/4, 0, 0, 5, 0])
        
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
