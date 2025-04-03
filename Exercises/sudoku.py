'''Find all solutions for 4 × 4 sudoku. Sudoku 4 × 4 is a special case of the
4 × 4 Latin square with additional properties. In the four 2 × 2 blocks,
no symbols can be repeated.'''

from itertools import permutations
import numpy as np

def validate(s):
    for n in range(4):
        if len(set(s[:, n])) != 4:
            return False
    if len(set(s[0:2, 0:2].flatten())) != 4:
        return False
    if len(set(s[0:2, 2:4].flatten())) != 4:
        return False
    if len(set(s[2:4, 0:2].flatten())) != 4:
        return False
    if len(set(s[2:4, 2:4].flatten())) != 4:
        return False
    return True


def sudoku():
    digits = (1, 2, 3, 4)
    rows = permutations(digits)
    sudokus = permutations(rows, 4)
    for sudoku in sudokus:
        s = np.array(sudoku)
        if validate(s):
            yield s

for i, j in enumerate(sudoku()):
    print('Solution {}:'.format(i+1))
    print(j)
    print()
