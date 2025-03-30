'''Write a program that draws a rectangle made of small squares. Build
a full string and then print it out.'''

rows = int(input('Number of rows:\n'))
cols = int(input('Number of cols:\n'))

# solution 1
aline = '+'
bline = '|'
grid = ''
for i in range(cols):
    aline += '---+'
    bline += '   |'
for i in range(rows):
    grid += aline + '\n' + bline + '\n'
grid += aline
print(grid)

# solution 2
print()
aline = cols * '+---' + '+\n'
bline = cols * '|   ' + '|\n'
grid = rows * (aline + bline) + aline
print(grid)

# solution 3
print()
aline = '---'.join('+' * (cols+1)) + '\n'
bline = '   '.join('|' * (cols+1)) + '\n'
grid = bline.join([aline] * (rows+1))
print(grid)
