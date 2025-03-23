from itertools import zip_longest

class Matrix:
    '''A class representing dense matrices based on Python lists. The elements of the
    matrix are stored row by row in a list.'''

    counter = 0
    
    def __init__(self, rows=1, cols=1):
        '''Constructor.'''
        self.rows = rows
        self.cols = cols
        self.data = [0] * rows * cols
        Matrix.counter += 1

    def __repr__(self):
        '''Printing a nested list (a list of lists representing the rows of a matrix)
        representing the matrix.'''
        res = [str(self.data[i*self.cols:(i+1)*self.cols])
               for i in range(self.rows)]
        res = ', '.join(res)
        res = 'Matrix([' + res + '])'
        return res

    def __str__(self):
        '''Printing a matrix as a list row by row, each column is the width of the longest
        element in that column. Cell values ​​are right-justified. Numbers are displayed to
        3 decimal places.'''
        decimals = 3
        # column widths
        cols_digits = []
        res = '['
        for i in range(self.cols):
            col = []
            for j in range(self.rows):
                col.append(self.data[j*self.cols+i])
            lengths = [len(str(round(num, decimals))) for num in col]
            cols_digits.append(max(lengths))
        for i in range(self.rows):
            row = self.data[i*self.cols:(i+1)*self.cols]
            if i == 0:
                res += '['
            else:
                res += ' ['
            for j in range(self.cols):
                if len(str(round(row[j], decimals))) < cols_digits[j]:
                    if j > 0:
                        res += ' ' * (cols_digits[j]-len(str(round(row[j],
                                decimals)))+1) + str(round(row[j], decimals))
                    else:
                        res += ' ' * (cols_digits[j]-len(str(round(row[j],
                                decimals)))) + str(round(row[j], decimals))
                else:
                    if j > 0:
                        res += ' ' + str(round(row[j], decimals))
                    else:
                        res += str(round(row[j], decimals))
            if i < self.rows - 1:
                res += ']\n'
            else:
                res += ']]'
        return res

    def __getitem__(self, pair):
        '''Reading a matrix element m[i, j].''' 
        i, j = pair
        if i < self.rows and j < self.cols:
            return self.data[i*self.cols+j]
        else:
            raise ValueError('invalid index')

    def __setitem__(self, pair, value):
        '''Assigning a value to a given matrix element
        m[i, j] = value.'''
        i, j = pair
        if i < self.rows and j < self.cols:
            self.data[i*self.cols+j] = value
        else:
            raise ValueError('invalid index')

    def __eq__(self, other):
        '''Comparing two matrices. Two matrices are the same if they have the same
        dimensions and all of their matrix elements in each position have identical values ​
        (with full precision).'''
        if self.rows == other.rows and self.cols == other.cols:
            return all(n == m for (n, m) in zip_longest(self.data, other.data,
                                                        fillvalue=0))
        else:
            return False

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        '''Adding two matrices. Possible if the dimensions of both matrices are the same.'''
        if self.rows == other.rows and self.cols == other.cols:
            new_matrix = Matrix(self.rows, self.cols)
            new_matrix.data = [self.data[i] + other.data[i]
                               for i in range(self.rows*self.cols)]
            return new_matrix
        else:
            raise ValueError('matrices of different dimensions')       

    __iadd__ = __add__

    def __sub__(self, other):
        '''Subtracting two matrices. Possible if the dimensions of both matrices are the
        same.'''
        if self.rows == other.rows and self.cols == other.cols:
            new_matrix = Matrix(self.rows, self.cols)
            new_matrix.data = [self.data[i] - other.data[i]
                               for i in range(self.rows*self.cols)]
            return new_matrix
        else:
            raise ValueError('matrices of different dimensions')

    __isub__ = __sub__

    def __mul__(self, other):
        '''Multiplying two matrices. Possible, if the first matrix A has the same number of
        columns - dimension n x m, as the second matrix B has the number of rows - dimension
        m x p, and the resulting matrix C is of dimension n x p:
        c_ij = a_i1 * b_1j + a_i2 * b_2j + ... + a_in * b_nj = sum_{k=1}^n a_ik * b_kj.'''
        if isinstance(other, (int, float)):
            new_matrix = Matrix(self.rows, self.cols)
            new_matrix.data = [self.data[i] * other
                               for i in range(self.rows*self.cols)]
            return new_matrix
        else:
            if self.cols == other.rows:
                new_matrix = Matrix(self.rows, other.cols)
                for i in range(self.rows):
                    for j in range(other.cols):
                        for k in range(other.rows):
                            new_matrix.data[i*other.cols+j] += \
                            self.data[i*self.cols+k] * other.data[k*other.cols+j]                    
                return new_matrix
            else:
                raise ValueError('incorrect matrix dimensions')

    __rmul__ = __mul__

    __lmul__ = __mul__

    __imul__ = __mul__   

    def __pow__(self, power):
        '''Powering a square matrix. Multiplying a matrix with itself power-1 times.'''
        if self.rows == self.cols:
            if power == 0:
                return self.identity(self.rows)
            else:
                new_matrix = Matrix(self.rows, self.cols)
                new_matrix.data = self.data[:]                
                for i in range(power-1):
                    new_matrix *= self
                return new_matrix
        else:
            raise ValueError('non-square matrix')

    def __truediv__(self, other):
        '''Dividing all elements of a matrix by a given number.'''
        if isinstance(other, (int, float)):
            if other != 0:
                new_matrix = Matrix(self.rows, self.cols)
                new_matrix.data = [self.data[i] / other
                                   for i in range(self.rows*self.cols)]
                return new_matrix
            else:
                raise ZeroDivisionError('division by zero')
        else:
            raise ValueError('incorrect type')

    __rtruediv__ = __truediv__

    __itruediv__ = __truediv__

    @property  
    def transpose(self):
        '''Transpose of a matrix. Swapping rows and columns.'''
        new_matrix = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix.data[j*self.rows+i] = self.data[i*self.cols+j]
        return new_matrix

    def reshape(self, new_rows, new_cols):
        '''Changing the dimension of a matrix. Possible if the product of the new dimension
        of the matrix is ​​equal to the product of the dimensions of the original matrix
        (both matrices must have the same number of elements).'''        
        if new_rows * new_cols == self.cols * self.rows:
            new_matrix = Matrix(new_rows, new_cols)
            new_matrix.data = self.data[:]
            return new_matrix
        else:
            raise ValueError('incorrect dimensions')

    @property
    def trace(self):
        '''Trace of a square matrix. Sum of elements on the main diagonal.'''
        if self.rows == self.cols:
            tr = 0
            for i in range(self.cols):
                tr += self.data[i*self.cols+i]
            return tr            
        else:
            raise ValueError('non-square matrix')

    @property    
    def determinant(self):
        '''Determinant of a square matrix. Recursive method using the Laplace expansion
        with respect to the first (i=1) row:
        det(A) = \sum_{k=1}^n a_ik * D_ik, where: n is the dimension of the matrix,
        the rows satisfy 1 <= i <=n, where D_ij = (-1)^(i+j) det(A_ij) is the cofactor
        matrix element of element a_ij of matrix A.'''
        if self.rows == self.cols:
            if self.rows == 1:
                det = self.data[0]
            elif self.rows == 2:
                det = self.data[0]*self.data[3] - self.data[1]*self.data[2]
            else:
                # Laplace expansion
                det = 0
                for i in range(self.cols):
                    # minor
                    new_matrix = Matrix(self.rows-1, self.cols-1)
                    # with respect to the first row
                    temp_data = self.data[self.cols:]
                    k = i
                    for j in range(self.rows-1):
                        temp_data.pop(j*self.cols+k)
                        k -= 1
                    new_matrix.data = temp_data
                    # recursion
                    det += ((-1)**i) * self.data[i] * new_matrix.determinant
            return det
        else:
            raise ValueError('non-square matrix')

    def submatrix(self, i, j):
        '''Submatrix of matrix of dimensions n x m created by deleting i-th row and j-th
        column. The resulting matrix has dimensions n-1 x m-1. Columns and rows are
        labeled from 0 to n-1, m-1, respectively.'''
        if i < self.rows and j < self.cols:
            new_matrix = Matrix(self.rows-1, self.cols-1)
            # deleting i-th row
            temp_data = self.data[0:i*self.cols] + \
                        self.data[i*self.cols+self.cols:]
            new_data = [0] * (self.rows-1) * (self.cols-1)
            # deleting j-th column
            for k in range(self.rows-1):
                new_data[k*new_matrix.cols:k*new_matrix.cols+new_matrix.cols] = \
                        temp_data[k*self.cols:k*self.cols+j]+\
                        temp_data[k*self.cols+j+1:k*self.cols+self.cols]
            new_matrix.data = new_data
            return new_matrix
        else:
            raise ValueError('invalid indexes')

    @property
    def inverse(self):
        '''Inverse matrix of a square matrix. A^(-1) exists if the matrix A is nonsingular,
        has a nonzero determinant. Method using the cofactor matrix D:
        A^(-1) = (D)^T / det(A).'''
        if self.rows == self.cols and self.determinant != 0:
            inv_matrix = Matrix(self.rows, self.cols)
            if self.rows == 1:
                inv_matrix.data[0] = 1 / self.data[0]
            else:
                # cofactor matrix
                cof_matrix = []
                for i in range(self.rows):
                    for j in range(self.cols):
                        # submatrix
                        new_matrix = self.submatrix(i, j)
                        # minor
                        new_det = new_matrix.determinant
                        # cofactor matrix
                        cof_matrix.append(new_det*(-1)**(i+j))
                inv_matrix.data = cof_matrix
                # adjugate matrix
                inv_matrix = inv_matrix.transpose
                # inverse matrix
                inv_matrix /= self.determinant
            return inv_matrix
        else:
            raise ValueError('irreversible matrix')

    @classmethod
    def identity(cls, dim):
        '''Identity (square) matrix of dimension dim x dim.'''
        if isinstance(dim, int) and dim > 0:
            id_matrix = cls(dim, dim)
            for i in range(dim):
                id_matrix.data[i*dim+i] = 1
            return id_matrix
        else:
            raise ValueError('incorrect dimension')

    @classmethod
    def from_matrix(cls, mtrx):
        '''Creating a matrix directly by providing a nested list
        (a list of lists representing the rows of the matrix).'''
        rows = len(mtrx)
        cols = len(mtrx[0])
        if len(set([len(row) for row in mtrx])) == 1:
            new_matrix = cls(rows, cols)
            # flatten
            new_matrix.data = sum(mtrx, [])
            return new_matrix
        else:
            raise ValueError('incorrect dimensions')

    def copy(self):
        '''Copying a matrix.'''
        #matrix_copy = Matrix(self.rows, self.cols)
        matrix_copy = Matrix(1, 1)
        matrix_copy.rows = self.rows
        matrix_copy.cols = self.cols
        matrix_copy.data = list(self.data) # self.data[:]
        return matrix_copy

    def __del__(self):
        '''Destructor.'''
        Matrix.counter -= 1
