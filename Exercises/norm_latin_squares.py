'''Find all normalized 1 x 1, 2 x 2, 3 x 3 and 4 x 4 Latin squares, that is,
those whose first column and first row are arranged in ascending order.'''

from itertools import permutations
import numpy as np

def validate(n, s):
    for i in range(n):
        if len(set(s[:, i])) != n:
            return False
    is_sorted = lambda a: np.all(a[:-1] <= a[1:])
    if not is_sorted(s[0]):
        return False
    if not is_sorted(np.transpose(s)[0]):
        return False
    return True

def norm_latin_square(n):
    digits = [i for i in range(1, n+1)]
    rows = permutations(digits)
    squares = permutations(rows, n)
    for square in squares:
        s = np.array(square)
        if validate(n, s):
            yield s
                          
for n in range(1, 5):
    for i, j in enumerate(norm_latin_square(n)):
        print('n = {}, sol. = {}:'.format(n, i+1))
        print(j)
        print()
