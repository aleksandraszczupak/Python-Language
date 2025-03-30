'''Write a function sum_seq(sequence) that computes the sum of the numbers
contained in a sequence that may contain nested subsequences. Hint: consider
the recursive version, and check if an item is a sequence using
isinstance(item, (list, tuple)).'''

# solution 1
def sum_seq1(sequence):
    s = 0
    for subs in sequence:
        if isinstance(subs, (list, tuple)):
            s += sum_seq1(subs) # recursion
        else:
            s += subs
    return s

print(sum_seq1([1, (2, 3, 1), [5, 2, 2], [], [0, 2, 3], 5, 3, (1, 1), [3]]))
print(sum_seq1([1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]))

# solution 2
def sum_seq2(sequence):
    if isinstance(sequence, (list, tuple)):
        return sum(map(sum_seq2, sequence))
    else:
        return sequence

print()
print(sum_seq2([1, (2, 3, 1), [5, 2, 2], [], [0, 2, 3], 5, 3, (1, 1), [3]]))
print(sum_seq2([1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]))

# solution 3
def flatten(sequence):
    flat_seq = []
    for subs in sequence:
        if isinstance(subs, (list, tuple)):
            flat_seq.extend(flatten(subs)) # recursion
        else:
            flat_seq.append(subs)
    return flat_seq

def sum_seq3(sequence):
    return sum(flatten(sequence))

print()
print(sum_seq3([1, (2, 3, 1), [5, 2, 2], [], [0, 2, 3], 5, 3, (1, 1), [3]]))
print(sum_seq3([1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]))

# solution 4
def sum_seq4(sequence):
    return sum((sum_seq4(subs) if isinstance(subs, (list, tuple)) else subs)
               for subs in sequence)

print()
print(sum_seq4([1, (2, 3, 1), [5, 2, 2], [], [0, 2, 3], 5, 3, (1, 1), [3]]))
print(sum_seq4([1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]))
