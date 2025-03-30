'''Create a file sparse_matrices.py and write in it functions for operations on
sparse matrices, i.e. matrices with a small number of non-zero coefficients.
The matrix will be represented by a dictionary, {(1, 2): 3, (10, 20): 30} for
matrices with non-zero coefficients M[1, 2] = 3, M[10, 20] = 30. We assume that
the matrices are square and their dimension is suitably large.'''

def add_sparse_matrix(sparse1, sparse2):
    '''
    >>> add_sparse_matrix({(1, 2): 2, (3, 2): 3, (3, 3): 4}, {})
    {(1, 2): 2, (3, 2): 3, (3, 3): 4}
    >>> add_sparse_matrix({(1, 2): 2, (3, 2): 3, (3, 3): 4}, {(1, 1): -1, (3, 3): 3})
    {(1, 2): 2, (3, 2): 3, (3, 3): 7, (1, 1): -1}
    '''
    sparse3 = dict()
    for pair in sparse1:
        sparse3[pair] = sparse3.get(pair, 0) + sparse1[pair]
    for pair in sparse2:
        sparse3[pair] = sparse3.get(pair, 0) + sparse2[pair]
    return new_sparse_matrix(sparse3)

def sub_sparse_matrix(sparse1, sparse2):
    '''
    >>> sub_sparse_matrix({}, {(1, 2): 2, (3, 2): 3, (3, 3): 4})
    {(1, 2): -2, (3, 2): -3, (3, 3): -4}
    >>> sub_sparse_matrix({(1, 1): -1, (3, 3): 3}, {(1, 1): -1, (3, 3): 3})
    {}
    '''
    sparse3 = dict(sparse1)
    for pair in sparse2:
        sparse3[pair] = sparse3.get(pair, 0) - sparse2[pair]
    return new_sparse_matrix(sparse3)  

def mul_sparse_matrix(sparse1, sparse2):
    '''
    >>> mul_sparse_matrix({(1, 1): -1, (3, 3): 3}, {(1, 2): 2, (3, 2): 3, (3, 3): 4})
    {(1, 2): -2, (3, 2): 9, (3, 3): 12}
    >>> mul_sparse_matrix({(1, 2): 2, (3, 2): 3, (3, 3): 4}, {(1, 2): 2, (3, 2): 3, (3, 3): 4})
    {(3, 2): 12, (3, 3): 16}
    '''
    sparse3 = dict()
    for (row1, col1) in sparse1:
        for(row2, col2) in sparse2:
            if col1 == row2:
                sparse3[row1, col2] = sparse3.get((row1, col2), 0) +\
                                      sparse1[row1, col1] * sparse2[row2, col2]
    return new_sparse_matrix(sparse3)

def is_diagonal(sparse):
    '''
    >>> is_diagonal({(1, 2): 2, (3, 2): 3, (3, 3): 4})
    False
    >>> is_diagonal({})
    True
    >>> is_diagonal({(1, 1): -1, (3, 3): 3})
    True
    '''
    val = True
    for (row, col) in sparse:
        if row != col:
            val = False
            break
    return val

def is_empty(sparse):
    '''
    >>> is_empty({(1, 2): 2, (3, 2): 3, (3, 3): 4})
    False
    >>> is_empty({})
    True
    >>> is_empty({(1, 1): -1, (3, 3): 3})
    False
    '''
    return False if sparse else True

def new_sparse_matrix(sparse):
    '''A function that removes unnecessary pairs, i.e. values ​​equal to zero.
    >>> new_sparse_matrix({(1, 2): 0, (22, 17): 5})
    {(22, 17): 5}
    '''
    newsparse = {(x, y): v for (x, y), v in sparse.items() if v != 0}
    return newsparse

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=2)
