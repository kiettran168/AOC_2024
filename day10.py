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

direction = [(1,0), (-1,0), (0,1), (0,-1)]
for tail in tails:
    stack = [tail]
    visited = set()
    while len(stack) > 0:
        x, y = stack[-1]
        stack.pop()
        if grid[x][y] == 0:
            # First puzzle
            if (x,y) not in visited:
                heads[(x,y)][0] += 1
                visited.add((x,y))
            # Second puzzle
            heads[(x,y)][1] += 1
        else:
            for i, j in direction:
                if grid[x+i][y+j] == grid[x][y] - 1:
                    stack.append((x+i,y+j))
    
count = 0
count_ = 0
for h in heads:
    count += heads[h][0]
    count_ += heads[h][1]
print("Sum of all trails scores: ", count)
print("Sum of all trails ratings: ", count_)

f.close()
