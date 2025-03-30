'''Write a function rev(L, left, right) that reverses the order of elements in
a list from left to right inclusive. The list is modified in place. Consider
iterative and recursive versions.'''

# solution 1
def rev(L, left, right):
    try:
        if left > right:
            left, right = right, left
        subL = L[left:(right+1)]
        subL.reverse()
        L[left:(right+1)] = subL
        return L
    except TypeError:
        return('invalid index')

print(rev([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
print(rev([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 'ola', 2))
print(rev([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 7))

# solution 2
def rev_iter1(L, left, right):
    try:
        if left == right:
            pass
        else:
            if left > right:
                left, right = right, left
            for i in range(left, right//2+2):
                L[i], L[right] = L[right], L[i]
                right -= 1
        return L
    except TypeError:
        return('invalid index')

print()
print(rev_iter1([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
print(rev_iter1([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4, 2))
print(rev_iter1([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 7))

# solution 3
def rev_iter2(L, left, right):
    left += len(L) if left < 0 else 0
    right += len(L) if right < 0 else 0
    if left > right:
        left, right = right, left
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
    return L

print()
print(rev_iter2([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
print(rev_iter2([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4, 2))
print(rev_iter2([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 7))

# solution 4
def rev_rek1(L, left, right):
    try:
        if left == right:
            return L
        else:
            if left >= right:
                left, right = right, left
            L[left], L[right] = L[right], L[left]
            return rev_rek1(L, left+1, right-1)
    except TypeError:
        return('invaild index')

print()
print(rev_rek1([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
print(rev_rek1([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4, 2))
print(rev_rek1([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 7))

# solution 5
def rev_rek2(L, left, right):
    left += len(L) if left < 0 else 0
    right += len(L) if right < 0 else 0
    if left > right:
        left, right = right, left
    if left < right:
        L[left], L[right] = L[right], L[left]
        rev_rek2(L, left+1, right-1)
    return L

print()
print(rev_rek2([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
print(rev_rek2([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4, 2))
print(rev_rek2([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 7))
