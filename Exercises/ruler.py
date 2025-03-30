'''Write a program that draws a "ruler" of a given length. Numbers consisting
of several digits must be handled correctly (the last digit of the number must
be under the vertical bar). A full string has to be constructed and then
printed.

|....|....|....|....|....|....|....|....|....|....|....|....|
0    1    2    3    4    5    6    7    8    9   10   11   12'''

n = int(input('Length of a ruler [cm]:\n'))

# solution 1
top = '|'
bottom = '0'
ruler = ''
for i in range(n):
    top +=  '....|'
    bottom += (' ' * (5 - len(str(i+1)))) + str(i+1) 
ruler = top + '\n' + bottom
print(ruler)

# solution 2
print()
x = 12; row = []
row.extend('|....' for i in range(x))
row.append('|\n0')
row.extend(str(i+1).rjust(5) for i in range(x))
row.append('\n')
print(''.join(row))
