import unittest
from fracs import Frac
import math

class TestFrac(unittest.TestCase):
    def setUp(self):
        self.f1 = Frac(1, 2)
        self.f2 = Frac(4, 8)
        self.f3 = Frac(0, 3)
        self.f4 = Frac(1, 4)
        self.f5 = Frac(-5, 1)
        self.f6 = Frac(0, 1)
        self.f7 = Frac(-3, -2)
        self.f8 = Frac(2, -3)
        with self.assertRaises(ZeroDivisionError):
            self.err = Frac(2, 0)

    def test_str(self):
        self.assertEqual(str(self.f1), '1/2')
        self.assertEqual(str(self.f3), '0')
        self.assertEqual(str(self.f5), '-5')
        self.assertEqual(str(self.f7), '3/2')
        self.assertEqual(str(self.f8), '-2/3')

    def test_repr(self):
        self.assertEqual(repr(self.f2), 'Frac(1, 2)')
        self.assertEqual(repr(self.f3), 'Frac(0)')

    def test_eq(self):
        self.assertTrue(self.f1 == self.f1)
        self.assertTrue(self.f1 == self.f2)
        self.assertTrue(self.f3 == self.f6)
        self.assertFalse(self.f1 == self.f4)
        self.assertTrue(self.f5 == -5)

    def test_ne(self):
        self.assertFalse(self.f1 != self.f1)
        self.assertFalse(self.f1 != self.f2)
        self.assertFalse(self.f3 != self.f6)
        self.assertTrue(self.f1 != self.f4)

    def test_lt(self):
        self.assertTrue(self.f4 < self.f1)
        self.assertTrue(self.f5 < self.f6)
        self.assertFalse(self.f1 < self.f2)
        self.assertTrue(self.f1 < 0.75)

    def test_le(self):
        self.assertTrue(self.f4 <= self.f1)
        self.assertTrue(self.f1 <= self.f2)
        self.assertFalse(self.f4 <= self.f5)

    def test_gt(self):
        self.assertTrue(self.f1 > self.f4)
        self.assertTrue(self.f6 > self.f5)
        self.assertFalse(self.f1 > self.f2)
        self.assertTrue(self.f7 > 1)

    def test_ge(self):
        self.assertTrue(self.f1 >= self.f4)
        self.assertTrue(self.f1 >= self.f2)
        self.assertFalse(self.f5 >= self.f4)

    def test_add(self):
        self.assertEqual(self.f1 + self.f4, Frac(3, 4))
        self.assertEqual(self.f1 + self.f2, Frac(1, 1))
        self.assertEqual(self.f3 + self.f7, self.f7)
        self.assertEqual(self.f5 + 1, Frac(-4, 1))
        self.assertEqual(1.5 + self.f5, Frac(-7, 2))

    def test_sub(self):
        self.assertEqual(self.f4 - self.f1, Frac(-1, 4))
        self.assertEqual(self.f1 - self.f2, Frac(0, 1))
        self.assertEqual(self.f1 - self.f6, Frac(1, 2))
        self.assertEqual(self.f5 - 2, Frac(-7, 1))
        self.assertEqual(10 - self.f5, Frac(15, 1))

    def test_mul(self):
        self.assertEqual(self.f1 * self.f2, Frac(1, 4))
        self.assertEqual(self.f7 * self.f8, Frac(-1, 1))
        self.assertEqual(5 * self.f3 * 10, Frac(0, 3))

    def test_truediv(self):
        self.assertEqual(self.f1 / self.f2, Frac(1, 1))
        self.assertEqual(self.f1 / self.f8, Frac(-3, 4))
        self.assertEqual(self.f1 / self.f8, Frac(3, -4))
        self.assertEqual(self.f4 / 0.25, Frac(1, 1))
        self.assertEqual(1 / self.f4, ~self.f4)

    def test_floordiv(self):
        self.assertEqual(self.f1 // self.f2, Frac(1))
        self.assertEqual(self.f1 // self.f4, Frac(2))
        self.assertEqual(self.f2 // self.f8, Frac(-1))
        self.assertEqual(self.f4 // self.f1, Frac(0))
        with self.assertRaises(ZeroDivisionError):
            self.f1 // self.f3

    def test_mod(self):
        self.assertEqual(self.f1 % self.f2, Frac(0))
        self.assertEqual(self.f1 % self.f5, Frac(-9, 2))
        self.assertEqual(self.f4 % self.f1, Frac(1, 4))
        with self.assertRaises(ZeroDivisionError):
            self.f2 % self.f6

    def test_pos(self):
        self.assertEqual(+self.f1, self.f1)
        self.assertEqual(+self.f6, self.f6)

    def test_neg(self):
        self.assertEqual(-self.f1, Frac(-1, 2))
        self.assertEqual(-self.f5, Frac(5, 1))

    def test_invert(self):
        self.assertEqual(~self.f2, Frac(8, 4))

    def test_float(self):
        self.assertEqual(float(self.f1), 1/2)

    def test_hash(self):
        aset = set()
        aset.add(self.f3)
        aset.add(self.f6)
        self.assertEqual(len(aset), 1)
        aset.add(self.f1)
        aset.add(self.f2)
        self.assertEqual(len(aset), 2)

    def tearDown(self):
        pass
        
if __name__=='__main__':
    unittest.main()
