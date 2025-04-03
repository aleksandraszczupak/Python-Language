'''Find the number of ways to cover a 4 × 4 board with identical 2 × 1 tiles.'''

from itertools import combinations

def flatten(x):
    return sum(x, [])

def validate(g):
    if len(set(flatten(g))) != 16:
        return False
    return True

def tiles():
    places = [i for i in range(16)]
    tiles = [list(t) for t in combinations(places, 2) if (t[1] == t[0] + 1 or t[1] == t[0] + 4)]
    grids = [list(g) for g in combinations(tiles, 8)]
    for grid in grids:
        if validate(grid):
            yield grid

def print_solution(g):
    board = [i for i in range(16)]
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    solution = board
    for letter, tile in enumerate(g):
        solution[tile[0]] = letters[letter]
        solution[tile[1]] = letters[letter]
    solution_board = []
    while solution != []:
        solution_board.append(solution[:4])
        print(solution[:4])
        solution = solution[4:]
    
for i, sol in enumerate(tiles()):
    print('Solution {}:'.format(i+1))
    print_solution(sol)
    print()
