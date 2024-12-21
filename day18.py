import heapq
f = open("data/day18.txt", "r")

# size = 7
size = 71
obstacles = []
for line in f:
    x,y = [int(i) for i in line.strip().split(',')]
    obstacles.append((x, y))

directions = [(0,1), (0,-1), (1,0), (-1,0)]

def check(n):
    if n >= 0 and n < size:
        return True
    return False

queue = []
heapq.heappush(queue, (0,0,0))
visited = set()
path = []
s = 0
# First puzzle
while len(queue) > 0:
    dis, x, y = heapq.heappop(queue)
    if (x,y) in visited:
        continue
    if x == size-1 and y == size-1:
        print("Shortest path:", dis)
        break
    if s == dis:
        path += [(x,y)]
        s += 1
    visited.add((x,y))
    for sx, sy in directions:
        if check(x+sx) and check(y+sy) and (x+sx,y+sy) not in obstacles[:1024]:
            heapq.heappush(queue, (dis+1,x+sx,y+sy))

# Second puzzle
for i in range(1025, len(obstacles)):
    if obstacles[i-1] not in path:
        continue
    queue = []
    heapq.heappush(queue, (0,0,0))
    visited = set()
    path = []
    s = 0
    flag = True
    while len(queue) > 0:
        dis, x, y = heapq.heappop(queue)
        if (x,y) in visited:
            continue
        if x == size-1 and y == size-1:
            # print(dis)
            flag = False
            break
        if s == dis:
            path += [(x,y)]
            s += 1
        visited.add((x,y))
        for sx, sy in directions:
            if check(x+sx) and check(y+sy) and (x+sx,y+sy) not in obstacles[:i]:
                heapq.heappush(queue, (dis+1,x+sx,y+sy))
    
    if flag:
        print("Found obstacl:", obstacles[i-1])
        break

f.close()
