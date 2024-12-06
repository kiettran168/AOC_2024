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
while check(x,y):
    i, j = direction[curr]
    if grid[x+i][y+j] == '#':
        curr = (curr + 1) % 4
    else:
        x += i
        y += j
        if (x,y) not in visited:
            visited.append((x,y))
print("The guard visited: ", len(visited))

# Second puzzle
count = 0
obs = set()
for m, n in visited:    
    if grid[m][n] != '^': 
        grid[m][n] = "#"
    visited_ = set()
    curr = 0
    x, y = sx, sy

    visited_.add((x,y,curr))
    while check(x,y):
        i, j = direction[curr]
        if grid[x+i][y+j] == '#':
            curr = (curr + 1) % 4
        else:
            x += i
            y += j
            if (x, y, curr) in visited_:
                if (m, n) not in obs:
                    obs.add((m, n))
                    count += 1
                    break
            else:
                visited_.add((x,y,curr))
            
    if grid[m][n] != '^': 
        grid[m][n] = "."

print("Places for obstruction: ", count)

f.close()
