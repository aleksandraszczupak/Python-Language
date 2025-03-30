'''Consider a sequence, some of the elements of which may turn out to be
subsequences, and such nestings can overlap to an infinite depth. Write
a function flatten(sequence) that returns a flattened list of all the elements
of the sequence. Hint: consider a recursive version, and check whether
an element is a sequence via isinstance(item, (list, tuple)).'''

# solution 1
def flatten1(sequence):
    flat_seq = []
    for subs in sequence:
        if isinstance(subs, (list, tuple)):
            flat_seq.extend(flatten1(subs)) # recursion
        else:
            flat_seq.append(subs)
    return flat_seq

# solution 2
def flatten2(sequence, total=None):
    if total is None:
        total = []
    for subs in sequence:
        if isinstance(subs, (list, tuple)):
            flatten2(subs, total)
        else:
            total.append(subs)
    return total

# solution 3
def flatten3(sequence):
    result = []
    stack = []
    # stack
    for subs in sequence:
        stack.append(subs)
    while len(stack) > 0:
        subs = stack.pop()
        if isinstance(subs, (list, tuple)):
            for subs2 in subs:
                stack.append(subs2)
        else:
            result.append(subs)
    result.reverse()
    return result

# solution 4
def flatten4(sequence):
    for subs in sequence:
        if isinstance(subs, (list, tuple)):
            # generator
            #yield from flatten4(subs)
            for subs2 in flatten4(subs):
                yield subs2
        else:
            yield subs

s = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
assert flatten1(s) == list(range(1, 10))            
print(flatten1(s))
assert flatten2(s) == list(range(1, 10))
print(flatten2(s))
assert flatten3(s) == list(range(1, 10))
print(flatten3(s))
for i in flatten4(s):
    print(i)
