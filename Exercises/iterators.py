'''Create the following infinite iterators:
(a) returning 0, 1, 0, 1, 0, 1, ...,
(b) randomly returning one value from ("N", "E", "S", "W") - random walk on a 2D
    square lattice,
(c) returning 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... - day of the week
    numbers.'''

import itertools
import random

n = 10

# (a)
# solution 1
def it_a1(n):
    '''Prints the pair '0, 1' n times.'''
    it = itertools.repeat('0, 1')
    for i in range(n):
        print(next(it), end=', ')
it_a1(n)

# solution 2
def it_a2(n):
    '''Prints 0, 1 n times in succession.'''
    #it = itertools.cycle([0, 1])
    #it = itertools.cycle(range(2))
    #it = itertools.chain.from_iterable(['0', '1'] * n)
    it = (y for x in iter(int, 1) for y in range(2))
    for i in range(n):
        print(next(it), end=', ')
print()
it_a2(n)

# solution 3
def it_a3():
    while True:
        yield 0
        yield 1
it = it_a3()
print()
print(list(itertools.islice(it, n)))

# (b)
# solution 1
def it_b1(n):
    #it = iter(lambda: random.choice(['N', 'E', 'S', 'W']), 1)
    #it = iter(lambda: random.choice('NESW'), 'X')
    it = (random.choice(['N', 'E', 'S', 'W']) for _ in iter(str, 1))
    for i in range(n):
        print(next(it), end=', ')
print()
it_b1(n)

# solution 2
def it_b2(sequence):
    while True:
        yield random.choice(sequence)
it = it_b2('NESW')
print()
print(list(itertools.islice(it, n)))

# (c)
# solution 1
def it_c1(n):
    '''Prints n times all weekdays.'''
    #for j, i in enumerate(itertools.repeat('0, 1, 2, 3, 4, 5, 6')):
    for j, i in enumerate(itertools.repeat(', '.join(str(d) for d in
                                                     list(range(7))))):
        if j >= n:
            break
        else:
            print(i, end=', ')
print()
it_c1(n)

# solution 2
def it_c2(n):
    '''Prints n weekdays in succession.'''
    #for j, i in enumerate(itertools.chain.from_iterable(list(str(d) for d in
    #                                                         range(7)) * n)):
    for j, i in enumerate(itertools.cycle(range(7))):
        if j >= n:
            break
        else:
            print(i, end=', ')
print()
it_c2(n)

# solution 3
def it_c3(sequence):
    while True:
        for item in sequence:
            yield item
it = it_c3(range(7))
print()
print(list(itertools.islice(it, n)))
