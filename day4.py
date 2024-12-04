f = open("data/day4.txt", "r")
grid = []
for line in f:
    line = line.strip()
    grid += [line]
    
for _ in range(3):
    grid += [''.join('.' for i in range(len(grid[0])))]
    grid = [''.join('.' for i in range(len(grid[0])))] + grid
grid = ['...' + grid[i] + '...\n' for i in range(len(grid))]

b = open('m.txt', "w")
xmap = []
amap = []
for i, line in enumerate(grid):
    b.write(line)
    xmap += [(i, j) for j, ltr in enumerate(line) if ltr == 'X']
    amap += [(i, j) for j, ltr in enumerate(line) if ltr == 'A']

# First puzzle
count = 0
for i, j in xmap:
    if ''.join([grid[i+n][j] for n in range(4)]) == 'XMAS': count += 1
    if ''.join([grid[i-n][j] for n in range(4)]) == 'XMAS': count += 1
    if ''.join([grid[i][j+n] for n in range(4)]) == 'XMAS': count += 1
    if ''.join([grid[i][j-n] for n in range(4)]) == 'XMAS': count += 1
    if ''.join([grid[i+n][j+n] for n in range(4)]) == 'XMAS': count += 1
    if ''.join([grid[i-n][j-n] for n in range(4)]) == 'XMAS': count += 1
    if ''.join([grid[i+n][j-n] for n in range(4)]) == 'XMAS': count += 1
    if ''.join([grid[i-n][j+n] for n in range(4)]) == 'XMAS': count += 1
print("Number of XMASs: ", count)

# Second puzzle
count = 0
for i, j in amap:
    if ''.join([grid[i-1][j-1], grid[i][j], grid[i+1][j+1]]) in ['MAS', 'SAM'] and ''.join([grid[i-1][j+1], grid[i][j], grid[i+1][j-1]]) in ['MAS', 'SAM']: count += 1
print("Number of X-MASs: ", count)

