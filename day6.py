f = open("data/day6.txt", "r")

grid = []
x, y = 0, 0

for line in f:
    grid += [[a for a in line.strip()]]
    if '^' in line:
        x, y = len(grid) - 1, line.index('^')
sx, sy = x, y

def check(x,y):
    if x > 0  and x < len(grid)-1 and y > 0 and y < len(grid[0])-1:
        return True
    return False

# First puzzle
direction = {0:(-1, 0), 1:(0, 1), 2:(1, 0), 3:(0, -1)}
visited = []
curr = 0
visited.append((x,y))
before = {}
while check(x,y):
    i, j = direction[curr]
    if grid[x+i][y+j] == '#':
        curr = (curr + 1) % 4
    else:
        x += i
        y += j
        if (x,y) not in visited:
            visited.append((x,y))
            before[(x,y)] = (x-i,y-j,curr)
print("The guard visited: ", len(visited))

# Second puzzle
count = 0    
reset = (sx,sy,0)
for m, n in visited[1:]:
    if grid[m][n] != '^': 
        grid[m][n] = "#"
    x, y, curr = before[(m,n)]
    visited_ = set()
    visited_.add((x,y,curr))
    while check(x,y):
        i, j = direction[curr]
        if grid[x+i][y+j] == '#':
            curr = (curr + 1) % 4
            i, j = direction[curr]
            if (x+i, y+j, curr) in visited_:
                count += 1
                break
        else:
            x += i
            y += j
            visited_.add((x,y,curr))
            
    if grid[m][n] != '^': 
        grid[m][n] = "."

print("Places for obstruction: ", count)

f.close()
