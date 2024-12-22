from functools import lru_cache
from itertools import permutations, product

f = open("data/day21.txt", "r")

passcode = []
for line in f:
    passcode += [[i for i in line.strip()]]

numpad = (
    ('#', '#', '#', '#', '#'),
    ('#', '7', '8', '9', '#'),
    ('#', '4', '5', '6', '#'),
    ('#', '1', '2', '3', '#'),
    ('#', '#', '0', 'A', '#'),
    ('#', '#', '#', '#', '#')
)
numbers = {
    '7': (1,1), '8': (1,2), '9': (1,3),
    '4': (2,1), '5': (2,2), '6': (2,3),
    '1': (3,1), '2': (3,2), '3': (3,3),
    '0': (4,2), 'A': (4,3)
}

dirpad = (
    ('#', '#', '#', '#', '#'),
    ('#', '#', '^', 'A', '#'),
    ('#', '<', 'v', '>', '#'),
    ('#', '#', '#', '#', '#')
)
dirs = {
    '^': (1,2), 'A': (1,3),
    '<': (2,1), 'v': (2,2), '>': (2,3)
}

directions = {'>': (0,1), '<': (0,-1), 'v': (1,0), '^': (-1,0)}

@lru_cache
def move(start, end, pad):
    if pad:
        pad = numpad
    else:
        pad = dirpad
    sx, sy = start
    ex, ey = end
    visited = set()
    queue = [('', sx, sy)]
    res = ''
    while len(queue) > 0:
        path, x, y = queue[0]
        queue.pop(0)
        if x == ex and y == ey:
            res = path
            break
        if (x,y) in visited:
            continue
        visited.add((x,y))
        for d in directions:
            dx, dy = directions[d]
            if pad[x+dx][y+dy] != '#':
                queue.append((path+d, x+dx, y+dy))
    
    combos = list(set(permutations(res)))
    res = []
    for combo in combos:
        x, y = sx, sy
        flag = True
        for c in combo:
            cx, cy = directions[c]
            x += cx
            y += cy
            if pad[x][y] == '#':
                flag = False
                break
        if flag:
            res.append(combo)

    return res
        
@lru_cache
def get_path(start, end):
    path = [''.join(i)+'A' for i in move(start, end, False)]
    return path

@lru_cache(None)
def get_cost(start, end, depth):
    if depth == 0:
        return min([len(x) for x in get_path(start, end)])
    
    paths = get_path(start, end)
    best_cost = 1<<60
    for path in paths:
        prev = dirs['A']
        cost = 0
        for p in path:
            cost += get_cost(prev, dirs[p], depth-1)
            prev = dirs[p]
        best_cost = min(best_cost, cost)
    
    return best_cost

count = 0
count_ = 0
for code in passcode:
    prev = numbers['A']
    path1 = []
    for c in code:
        path1.append([''.join(i)+'A' for i in move(prev, numbers[c], True)])
        prev = numbers[c]
    path1 = list(set(''.join(i) for i in product(*path1)))

    # First puzzle
    best_cost = 1<<60
    for path in path1:
        cost = 0
        prev = dirs['A']
        for p in path:
            cost += get_cost(prev, dirs[p], 1)
            prev = dirs[p]
        best_cost = min(best_cost, cost)
    # print(best_cost)
    count += best_cost * int(''.join(code[:-1]))

    # Second puzzle
    best_cost = 1<<60
    for path in path1:
        cost = 0
        prev = dirs['A']
        for p in path:
            cost += get_cost(prev, dirs[p], 24)
            prev = dirs[p]
        best_cost = min(best_cost, cost)
    # print(best_cost)
    count_ += best_cost * int(''.join(code[:-1]))

print('Complexity:', count)
print('25 more robots complexity:', count_)

f.close()
