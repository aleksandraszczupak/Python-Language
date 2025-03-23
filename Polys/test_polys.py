import unittest
from polys import Poly

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = Poly(1, 2, 0, -3, 5, 0, -7) # W(x) = 1 + 2x - 3x^3 + 5x^4 - 7x^6
        self.p2 = Poly(2, 0, -3) # W(x) = 2 - 3x^2
        self.p3 = Poly(0, 5, 0, -7) # W(x) = 5x - 7x^3
        self.p4 = Poly(5, 0, 0, -7) # W(x) = 5 - 7x^3
        self.p5 = Poly(0, 0, 0) # W(x) = 0
        self.p6 = Poly(2, 1, 0) # W(x) = 2 + x

    def test_str(self):
        self.assertEqual(str(self.p1), '[1, 2, 0, -3, 5, 0, -7]')
        self.assertEqual(str(self.p3), '[0, 5, 0, -7]')
        self.assertEqual(str(self.p5), '[0]')
        self.assertEqual(str(self.p6), '[2, 1]')

    def test_add(self):
        self.assertEqual(self.p1 + self.p2, Poly(3, 2, -3, -3, 5, 0, -7))
        self.assertEqual(self.p3 + self.p4, Poly(5, 5, 0, -14))
        self.assertEqual(self.p5 + self.p6, Poly(2, 1))

    def test_sub(self):
        self.assertEqual(self.p3 - self.p1, Poly(-1, 3, 0, -4, -5, 0, 7))
        self.assertEqual(self.p6 - self.p5, Poly(2, 1))

    def test_mul(self):
        self.assertEqual(self.p1 * self.p2,
                         Poly(2, 4, -3, -12, 10, 9, -29, 0, 21))
        self.assertEqual(self.p1 * self.p4,
                         Poly(5, 10, 0, -22, 11, 0, -14, -35, 0, 49))
        self.assertEqual(self.p2 * self.p6,
                         Poly(4, 2, -6, -3))
        self.assertEqual(self.p1 * self.p6,
                         Poly(2, 5, 2, -6, 7, 5, -14, -7))

    def test_pos(self):
        self.assertEqual(+self.p1, self.p1)
        self.assertEqual(+self.p2, self.p2)

    def test_neg(self):
        self.assertEqual(-self.p2, Poly(-2, 0, 3))
        self.assertEqual(-self.p5, Poly(0))

    def test_eq(self):
        self.assertTrue(self.p1 == self.p1)
        self.assertFalse(self.p1 == self.p2)
        self.assertTrue(self.p6 == Poly(2, 1, 0, 0))
        self.assertTrue(self.p5 == Poly(0))

    def test_ne(self):
        self.assertFalse(self.p3 != self.p3)
        self.assertTrue(self.p3 != self.p4)

    def test_eval(self):
        self.assertEqual(self.p1.eval(-2), -347)
        self.assertEqual(self.p2.eval(-2), -10)
        self.assertEqual(self.p3.eval(6), -1482)
        self.assertEqual(self.p5.eval(10), 0)

    def test_combine(self):
        self.assertEqual(self.p1.combine(self.p2),
        Poly(-387, 0, 3654, 0, -14202, 0, 29241, 0, -33615, 0, 20412, 0, -5103))
        self.assertEqual(self.p2.combine(self.p3),
        Poly(2, 0, -75, 0, 210, 0, -147))

    def test_pow(self):
        self.assertEqual(self.p2 ** 4,
                         Poly(16, 0, -96, 0, 216, 0, -216, 0, 81))
        self.assertEqual(self.p4 ** 3,
                         Poly(125, 0, 0, -525, 0, 0, 735, 0, 0, -343))
        
    def test_differentiate(self):
        self.assertEqual(self.p1.differentiate(), Poly(2, 0, -9, 20, 0, -42))
        self.assertEqual(self.p4.differentiate(), Poly(0, 0, -21))
        self.assertEqual(self.p6.differentiate(), Poly(1))

    def test_integrate(self):
        self.assertAlmostEqual(self.p1.integrate(),
                               Poly(0, 1, 1, 0, -3/4, 1, 0, -1), places=2)
        self.assertAlmostEqual(self.p4.integrate(),
                               Poly(0, 5, 0, 0, -7/4), places=2)

    def test_is_zero(self):
        self.assertEqual(self.p3.is_zero(), False)
        self.assertEqual(self.p5.is_zero(), True)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
