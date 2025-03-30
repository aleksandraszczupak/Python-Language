'''Create a dictionary that translates Roman numerals (with the letters I, V, X,
L, C, D, M) into Arabic numerals.'''

# [1, 3, 4, 7, 12, 49, 66, 99, 947]
rlist = ['I', 'III', 'IV', 'VII', 'XII', 'XLIX', 'LXVI', 'XCIX', 'CMXLVII']
dt = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# solution 1
def roman2int1(roman, dt):
    a, i = 0, 0
    while i < len(roman):
        if i < len(roman) - 1:
            if dt[roman[i+1]] > dt[roman[i]]:
                  a += dt[roman[i+1]] - dt[roman[i]]
                  i += 2
            else:
                 a += dt[roman[i]]
                 i += 1
        else:
            a += dt[roman[i]]
            i += 1
    print(a)

for roman in rlist:
    roman2int1(roman, dt)

# solution 2
print()
def roman2int2(roman, dt):
    a = 0
    for i in range(len(roman)):
        if i == 0 or dt[roman[i]] <= dt[roman[i-1]]:
            a += dt[roman[i]] 
        else:
            a += dt[roman[i]]
            a -= 2 * dt[roman[i-1]]
    print(a)
    
for roman in rlist:
    roman2int2(roman, dt)

# solution 3
print()
def roman2int3(roman, dt):
    a = 0
    prev = 0
    for i in reversed(roman):
        val = dt[i]
        if val >= prev:
            a += val
        else:
            a -= val
        prev = val
    print(a)
            
for roman in rlist:
    roman2int3(roman, dt)
