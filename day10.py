f = open("data/day10.txt", "r")

grid = []
heads = {}
tails = []
for line in f:
    grid += [[-1] + [int(i) for i in line.strip()] + [-1]]

grid = [[-1 for i in range(len(grid[0]))]] + grid
grid += [[-1 for i in range(len(grid[0]))]]

for r, line in enumerate(grid):
    cols = [i for i in range(len(line)) if line[i] == 0 or line[i] == 9]
    for c in cols:
        if line[c] == 0:
            heads[(r,c)] = [0, 0]
        else:
            tails.append((r, c))

for tail in tails:
    queue = [tail]
    visited = set()
    while len(queue) > 0:
        x, y = queue[0]
        queue.pop(0)
        if grid[x][y] == 0:
            # First puzzle
            if (x,y) not in visited:
                heads[(x,y)][0] += 1
                visited.add((x,y))
            # Second puzzle
            heads[(x,y)][1] += 1
        else:
            if grid[x-1][y] == grid[x][y] - 1:
                queue.append((x-1,y))
            if grid[x+1][y] == grid[x][y] - 1:
                queue.append((x+1,y))
            if grid[x][y-1] == grid[x][y] - 1:
                queue.append((x,y-1))
            if grid[x][y+1] == grid[x][y] - 1:
                queue.append((x,y+1))
    
count = 0
count_ = 0
for h in heads:
    count += heads[h][0]
    count_ += heads[h][1]
print("Sum of all trails scores: ", count)
print("Sum of all trails ratings: ", count_)

f.close()
