'''Find all 1 x 1, 2 x 2, 3 × 3 and 4 × 4 Latin squares.'''

from itertools import permutations
import numpy as np

def validate(n, s):
    for i in range(n):
        if len(set(s[:, i])) != n:
            return False
    return True

def latin_square(n):
    digits = [i for i in range(1, n+1)]
    rows = permutations(digits)
    squares = permutations(rows, n)
    for square in squares:
        s = np.array(square)
        if validate(n, s):
            yield s

for n in range(1, 5):
    for i, j in enumerate(latin_square(n)):
        print('n = {}, sol = {}:'.format(n, i+1))
        print(j)
        print()
