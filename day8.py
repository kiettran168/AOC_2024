f = open("data/day8.txt", "r")

names = []
grid = []
loc = {}
anti = set()
for line in f:
    grid.append([a for a in line.strip()])
    for i, a in enumerate(line.strip()):
        if a != '.':
            if a not in names:
                names.append(a)
                loc[a] = []
            loc[a] += [(len(grid)-1, i)]

def checkx(para):
    if para >= 0 and para < len(grid):
        return True
    return False

def checky(para):
    if para >= 0 and para < len(grid[0]):
        return True
    return False

# First puzzle
for a in names:
    nodes = loc[a]
    for i,n1 in enumerate(nodes):
        for n2 in nodes[(i+1):]:
            nx, ny = n2[0] - n1[0], n2[1] - n1[1]
            if checkx(n2[0]+nx) and checky(n2[1]+ny):
                anti.add((n2[0]+nx, n2[1]+ny))
            if checkx(n1[0]-nx) and checky(n1[1]-ny):
                anti.add((n1[0]-nx, n1[1]-ny))
        
print("Number of locations:", len(anti))

# Second puzzle
anti = set()
for a in names:
    nodes = loc[a]
    for i,n1 in enumerate(nodes):
        for n2 in nodes[(i+1):]:
            nx_, ny_ = n2[0] - n1[0], n2[1] - n1[1]
            anti.add(n1)
            anti.add(n2)
            n = 1
            while True:
                nx, ny = n * nx_, n * ny_
                flagx = True
                flagy = True
                if checkx(n2[0]+nx) and checky(n2[1]+ny):
                    anti.add((n2[0]+nx, n2[1]+ny))
                    flagx = False
                if checkx(n1[0]-nx) and checky(n1[1]-ny):
                    anti.add((n1[0]-nx, n1[1]-ny))
                    flagy = False
                if flagx and flagy:
                    break
                n += 1
print("Number of real locations:", len(anti))

# for a in anti:
#     if grid[a[0]][a[1]] == '.':
#         grid[a[0]][a[1]] = '#'
# for line in grid:
#     print(''.join(line))

f.close()
