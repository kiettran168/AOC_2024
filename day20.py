f = open("data/day20.txt", "r")

grid = []
sx, sy = 0, 0
ex, ey = 0, 0
for line in f:
    grid.append([i for i in line.strip()])
    if 'S' in line.strip():
        sx, sy = (len(grid)-1, line.strip().index('S'))
    if 'E' in line.strip():
        ex, ey = (len(grid)-1, line.strip().index('E'))

directions = [(0,1), (0,-1), (1,0), (-1,0)]

def race(grid):
    path = [(sx,sy)]
    x, y = sx, sy
    while x != ex or y != ey:
        for dx, dy in directions:
            if grid[x+dx][y+dy] != '#' and (x+dx,y+dy) not in path:
                x += dx
                y += dy
                path.append((x,y))
                break
    return path

def check(n):
    if n >= 0 and n < len(grid):
        return True
    return False

path = race(grid)
# print(len(path))

# First puzzle
shortcut = {}
for x, y in path:
    a = path.index((x,y))
    for dx, dy in directions:
        if check(x+2*dx) and check(y+2*dy):
            if (x+2*dx, y+2*dy) in path:
                b = path.index((x+2*dx,y+2*dy))
                if a < b:
                    n = b - a - 2
                    if n >= 100:
                    # if n >= 50:
                        if n in shortcut:
                            shortcut[n] += 1
                        else:
                            shortcut[n] = 1
count = 0
for s in shortcut:
    # print(shortcut[s], s)
    count += shortcut[s]
print("Cheats that saves more than at least 100ps:", count)

# Second puzzle
shortcut = {}
for a, p in enumerate(path):
    x, y = p
    for b in range(a+100, len(path)):
    # for b in range(a+50, len(path)):
        dx, dy = path[b]
        if (abs(x-dx) + abs(y-dy)) <= 20:
            n = b - a - (abs(x-dx) + abs(y-dy))
            if n < 100:
            # if n < 50:
                continue
            if n in shortcut:
                shortcut[n] += 1
            else:
                shortcut[n] = 1
        if dx == ex and dy == ey:
            break

count = 0
for s in shortcut:
    # print(shortcut[s], s)
    count += shortcut[s]
print("More cheats that saves more than at least 100ps:", count)

f.close()
