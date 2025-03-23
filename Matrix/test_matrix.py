import unittest
from matrix import *

class TestMatrix(unittest.TestCase):

    def setUp(self):
        self.m1 = Matrix(4, 3)
        self.m1[0, 0] = 1
        self.m1[0, 1] = 1.5
        self.m1[0, 2] = 4
        self.m1[1, 0] = -1
        self.m1[1, 1] = 2
        self.m1[2, 0] = 2.75
        self.m1[2, 1] = 4
        self.m1[2, 2] = -5
        self.m1[3, 0] = 1.125
        self.m1[3, 1] = 9
        self.m1[3, 2] = 3

        self.m2 = Matrix.from_matrix([[1, 1.5, 4], [-1, 2, 0],
                                     [2.755, 4, -5], [1.12, 9, 3]])

        self.m3 = Matrix.from_matrix([[1, 2, 3, 8], [4, 0, 5, 0],
                                     [-7, 9, -2, -6]])

        self.m4 = Matrix(5, 5)
        self.m4[0, 3] = 3
        self.m4[0, 4] = 4
        self.m4[1, 0] = -1
        self.m4[1, 4] = 7
        self.m4[2, 1] = 6
        self.m4[2, 2] = 15
        self.m4[3, 3] = 1.5
        self.m4[3, 4] = 4
        self.m4[4, 0] = 1.5
        self.m4[4, 2] = -2
        self.m4[4, 3] = 1

        self.m5 = Matrix(2, 2)
        self.m5[0, 0] = 1
        self.m5[0, 1] = 2
        self.m5[1, 0] = 3
        self.m5[1, 1] = 4

        self.m6 = Matrix(1, 1)
        self.m6[0, 0] = 5

        self.m7 = Matrix.from_matrix([[1, 2.0004], [3, 4.0004]])

        self.m8 = Matrix(2, 2)
        self.m8[0, 1] = 1
        self.m8[1, 1] = -1

    def tearDown(self):
        pass

    def test_setitem(self):
        self.m8[0, 0] = 7
        self.assertEqual(self.m8[0, 0], 7)
        self.assertEqual(self.m8[0, 1], 1)        
        with self.assertRaises(ValueError):
            self.m5[3, 3] = 4
        with self.assertRaises(ValueError):
            self.m6[1, 2] = -2

    def test_getitem(self):
        self.assertEqual(self.m8[0, 0], 0)
        self.assertEqual(self.m8[1, 1], -1)
        self.assertEqual(self.m3[1, 2], 5)
        self.assertEqual(self.m4[4, 4], 0)       
        with self.assertRaises(ValueError):
            self.m1[2, 3]
        with self.assertRaises(ValueError):
            self.m4[5, 1]

    def test_repr(self):
        self.assertEqual(repr(self.m1),
        'Matrix([[1, 1.5, 4], [-1, 2, 0], [2.75, 4, -5], [1.125, 9, 3]])')
        self.assertEqual(repr(self.m7),
        'Matrix([[1, 2.0004], [3, 4.0004]])')

    def test_str(self):
        self.assertEqual(str(self.m6), '[[5]]')        
        strm3_1 = '[[ 1 2  3  8]\n [ 4 0  5  0]\n [-7 9 -2 -6]]'
        strm3_2 = str(self.m3)
        self.assertMultiLineEqual(strm3_1, strm3_2)

    def test_eq(self):
        self.assertTrue(self.m1 == self.m1)
        self.assertFalse(self.m1 == self.m2)
        self.assertFalse(self.m5 == self.m6)

    def test_ne(self):
        self.assertFalse(self.m1 != self.m1)
        self.assertTrue(self.m1 != self.m2)
        self.assertTrue(self.m5 != self.m6)

    def test_add(self):
        self.assertEqual(repr(self.m1 + self.m2),
        'Matrix([[2, 3.0, 8], [-2, 4, 0], [5.505, 8, -10], [2.245, 18, 6]])')
        self.assertEqual(repr(self.m8 + self.m8 + self.m8),
        'Matrix([[0, 3], [0, -3]])')        
        with self.assertRaises(ValueError):
            self.m1 + self.m3
        with self.assertRaises(ValueError):   
            self.m4 + self.m6

    def test_iadd(self):
        self.m5 += self.m5
        self.assertEqual(repr(self.m5),
        'Matrix([[2, 4], [6, 8]])')        
        self.m8 += self.m7
        self.assertEqual(repr(self.m8),
        'Matrix([[1, 3.0004], [3, 3.0004]])')        
        with self.assertRaises(ValueError):
            self.m2 += self.m7
        with self.assertRaises(ValueError):    
            self.m6 += self.m4

    def test_sub(self):
        self.assertEqual((self.m1 - self.m2)[0, 0], 0)
        self.assertAlmostEqual((self.m1 - self.m2)[2, 0], -0.00499, 4)
        self.assertEqual(round((self.m1 - self.m2)[3, 0], 3), 0.005)
        self.assertEqual((self.m1 - self.m2)[3, 2], 0)
        self.assertEqual(repr(self.m5 - self.m8),
        'Matrix([[1, 1], [3, 5]])')        
        with self.assertRaises(ValueError):
            self.m2 - self.m4
        with self.assertRaises(ValueError):    
            self.m7 - self.m6

    def test_isub(self):
        self.m5 -= self.m5
        self.assertEqual(repr(self.m5),
        'Matrix([[0, 0], [0, 0]])')        
        with self.assertRaises(ValueError):
            self.m2 -= self.m7
        with self.assertRaises(ValueError):    
            self.m6 -= self.m4

    def test_mul(self):
        self.assertEqual((self.m1 * self.m3)[0, 0], -21.0)
        self.assertEqual((self.m1 * self.m3)[1, 2], 7)
        self.assertEqual((self.m1 * self.m3)[2, 3], 52.0)
        self.assertEqual((self.m1 * self.m3)[3, 2], 42.375)        
        self.assertTrue((self.m1 * self.m3) != (self.m3 * self.m1))        
        self.assertEqual(repr(self.m5 * self.m8),
        'Matrix([[0, -1], [0, -1]])')        
        self.assertAlmostEqual((self.m2 * 10)[2, 0], 27.55, 2)
        self.assertEqual((self.m2 * 10)[0, 0], 10)
        self.assertEqual((10 * self.m2)[2, 2], -50)
        self.assertAlmostEqual((10 * self.m2)[3, 0], 11.2, 1)
        self.assertEqual((self.m2 * 10)[2, 0], (10 * self.m2)[2, 0])
        self.assertEqual((self.m2 * 10)[0, 1], (10 * self.m2)[0, 1])        
        with self.assertRaises(ValueError):
            self.m1 * self.m2
        with self.assertRaises(ValueError):    
            self.m3 * self.m8

    def test_imul(self):
        self.m5 *= self.m5
        self.assertEqual(repr(self.m5),
        'Matrix([[7, 10], [15, 22]])')        
        with self.assertRaises(ValueError):
            self.m2 *= self.m7
        with self.assertRaises(ValueError):    
            self.m6 *= self.m4

    def test_pow(self):
        self.assertEqual(self.m5 ** 0, Matrix.identity(2))
        self.assertTrue(self.m5 ** 1 == self.m5)
        self.assertEqual(repr(self.m5 ** 2),
        'Matrix([[7, 10], [15, 22]])')
        self.assertEqual(repr(self.m5 ** 3),
        'Matrix([[37, 54], [81, 118]])')        
        self.assertEqual(repr(self.m5 ** 4),
        'Matrix([[199, 290], [435, 634]])')
        with self.assertRaises(ValueError):
            self.m1 ** 2
        with self.assertRaises(ValueError):
            self.m2 ** 5

    def test_truediv(self):
        self.assertEqual((self.m5 / 5)[0, 0], 0.2)
        self.assertEqual((self.m5 / 5)[0, 1], 0.4)
        self.assertEqual((self.m5 / 0.5)[1, 0], 6)
        self.assertEqual((self.m5 / 0.5)[1, 1], 8)
        self.m5 /= 5
        self.assertEqual(repr(self.m5),
        'Matrix([[0.2, 0.4], [0.6, 0.8]])')
        with self.assertRaises(ValueError):
            self.m5 / self.m1
        with self.assertRaises(ZeroDivisionError):
            self.m2 / 0

    def test_transpose(self):
        self.assertEqual(self.m3.transpose[1, 0], 2)
        self.assertEqual(self.m3.transpose[1, 0], self.m3[0, 1])
        self.assertEqual(self.m3.transpose[2, 0], self.m3[0, 2])

    def test_reshape(self):
        self.assertEqual(self.m3.reshape(4, 3)[1, 0], 8)
        self.assertEqual(self.m3.reshape(2, 6)[1, 0], 5)
        self.assertEqual(self.m8.reshape(4, 1)[3, 0], -1)
        with self.assertRaises(ValueError):
            self.m1.reshape(2, 2)
        with self.assertRaises(ValueError):    
            self.m2.reshape(4, 4)

    def test_trace(self):
        self.assertEqual(self.m4.trace, 16.5)
        self.assertEqual(self.m7.trace, 5.0004)
        with self.assertRaises(ValueError):
            self.m2.trace
        with self.assertRaises(ValueError):    
            self.m3.trace

    def test_determinant(self):
        self.assertEqual(self.m4.determinant, 72)
        self.assertEqual(self.m5.determinant, -2)
        self.assertEqual(self.m8.determinant, 0)
        with self.assertRaises(ValueError):
            self.m2.determinant
        with self.assertRaises(ValueError):    
            self.m3.determinant

    def test_submatrix(self):
        self.assertEqual(self.m4.submatrix(0, 0).rows, 4)
        self.assertEqual(self.m4.submatrix(0, 0).cols, 4)
        self.assertEqual(self.m4.submatrix(0, 0)[1, 0], 6)
        self.assertEqual(self.m4.submatrix(0, 0)[2, 3], 4)
        self.assertEqual(self.m1.submatrix(2, 1)[0, 1], 4)
        self.assertEqual(self.m1.submatrix(2, 1)[2, 1], 3)
        with self.assertRaises(ValueError):
            self.m2.submatrix(4, 3)
        with self.assertRaises(ValueError):    
            self.m4.submatrix(1, 5)

    def test_inverse(self):
        self.assertEqual(repr(self.m5.inverse),
        'Matrix([[-2.0, 1.0], [1.5, -0.5]])')
        self.assertEqual(str(self.m6.inverse), '[[0.2]]')
        self.assertEqual(self.m4.inverse[0, 0], -1.75)
        self.assertEqual(self.m4.inverse[3, 0], -self.m4.inverse[3, 3])
        self.assertAlmostEqual(self.m4.inverse[1, 3], -5.729, 3)
        self.assertEqual(self.m4.inverse[4, 4], 0)
        with self.assertRaises(ValueError):
            self.m1.inverse
        with self.assertRaises(ValueError):    
            self.m8.inverse

    def test_identity(self):
        self.assertTrue(Matrix.identity(5) == Matrix.identity(5).inverse)
        self.assertEqual(Matrix.identity(5).trace, 5)
        self.assertEqual(str(Matrix.identity(1)), '[[1]]')
        with self.assertRaises(ValueError):
            Matrix.identity(0)
        with self.assertRaises(ValueError):    
            Matrix.identity(-1)
        with self.assertRaises(ValueError):    
            Matrix.identity(0.5)

    def test_from_matrix(self):
        self.assertEqual(repr(Matrix.from_matrix([[1, 2], [3, 4]])),
        'Matrix([[1, 2], [3, 4]])')
        self.assertEqual(Matrix.from_matrix([[0, 1], [0, -1]]), self.m8)
        with self.assertRaises(ValueError):
            Matrix.from_matrix([[1, 2, 3, 4], [5, 6, 7]])

    def test_copy(self):
        self.assertEqual(self.m1.copy().data, self.m1.data)

if __name__ == '__main__':
    unittest.main(verbosity=2)
