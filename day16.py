import heapq
f = open("data/day16.txt", "r")

grid = []
sx, sy = 0, 0
ex, ey = 0,0
for line in f:
    grid.append(line.strip())
    if 'S' in line.strip():
        sx, sy = len(grid)-1, line.strip().index('S')
    if 'E' in line.strip():
        ex, ey = len(grid)-1, line.strip().index('E')

# First puzzle
# 0: E      1: S    2: W    3: N
direction = {0:(0,1), 1:(1,0), 2:(0,-1), 3:(-1,0)}
queue = []
distance = {}
heapq.heappush(queue, (0, sx, sy, 0))
visited = set()
best = 0
while len(queue) > 0:
    point, currx, curry, facing = heapq.heappop(queue)
    if (currx, curry, facing) not in distance:
        distance[(currx, curry, facing)] = point

    if (currx, curry, facing) in visited:
        continue

    visited.add((currx, curry, facing))
    if currx == ex and curry == ey and best == 0:
        print("Highest possible score:", point)
        best = point
    
    stepx, stepy = direction[facing]
    if grid[currx+stepx][curry+stepy] != '#':
        heapq.heappush(queue,(point+1, currx+stepx, curry+stepy, facing))
    
    heapq.heappush(queue,(point+1000, currx, curry, (facing+1) % 4))
    heapq.heappush(queue,(point+1000, currx, curry, (facing+3) % 4))

# Second puzzle
queue = []
distance_ = {}
for d in range(4):
    heapq.heappush(queue, (0, ex, ey, d))
visited = set()
while len(queue) > 0:
    point, currx, curry, facing = heapq.heappop(queue)
    if (currx, curry, facing) not in distance_:
        distance_[(currx, curry, facing)] = point

    if (currx, curry, facing) in visited:
        continue

    visited.add((currx, curry, facing))
    
    stepx, stepy = direction[(facing+2) % 4]
    if grid[currx+stepx][curry+stepy] != '#':
        heapq.heappush(queue,(point+1, currx+stepx, curry+stepy, facing))
    
    heapq.heappush(queue,(point+1000, currx, curry, (facing+1) % 4))
    heapq.heappush(queue,(point+1000, currx, curry, (facing+3) % 4))

good = set()
for x, line in enumerate(grid):
    for y, seat in enumerate(line):
        if seat in ['.','S','E']:
            for d in range(4):
                if (x,y,d) in distance and (x,y,d) in distance_:
                    if distance[(x,y,d)] + distance_[(x,y,d)] == best:
                        good.add((x,y))
print("Seats with best scenes:", len(good))

f.close()
