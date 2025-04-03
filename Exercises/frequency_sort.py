'''Write a function frequency_sort() that sorts numbers in array L according to
their frequency of occurrence. If two numbers have the same frequency of
occurrence, the order is determined by the index of the first occurrence of
the number in array L.'''

import random
import collections

L = [8, 9, 8, 8, 5, 6, 8, 5, 5, 8, 3, 5, 8, 1, 5, 9, 6, 8, 8, 2]
print(L)

# solution 1
def frequency_sort1(L, left, right):
    L = L[left:right+1]
    fdict = {x: L.count(x) for x in L}
    return sorted(L, key=lambda x: (-fdict[x], L.index(x)))
print(frequency_sort1(L, 0, len(L)-1))

# solution 2
def frequency_sort2(L, left, right):
    L = L[left:right+1]
    counts = collections.Counter(L)
    return sorted(L, key=lambda x:(-counts[x], L.index(x)))
print(frequency_sort2(L, 0, len(L)-1))
