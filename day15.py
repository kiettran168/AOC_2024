f = open("data/day15.txt", "r")

flag = False
grid = []
grid_ = []
direction = {'^':(-1,0), 'v':(1,0), '<':(0,-1), '>':(0,1)}
robot = []
robot_ = []

def movable(x, y, d):
    if grid_[x][y] == '.':
        return True
    if grid_[x][y] == '#':
        return False
    if grid_[x][y] == '[':
        leftx, lefty = x, y
        rightx, righty = x, y+1
    elif grid_[x][y] == ']':
        leftx, lefty = x, y-1
        rightx, righty = x, y

    sx, sy = direction[d]        
    if d == '<':
        return movable(leftx+sx, lefty+sy, d)
    elif d == '>':
        return movable(rightx+sx, righty+sy, d)
    else:
        return movable(leftx+sx, lefty+sy, d) and movable(rightx+sx, righty+sy, d)

def move(x, y, d):
    if grid_[x][y] == '[':
        leftx, lefty = x, y
        rightx, righty = x, y+1
    elif grid_[x][y] == ']':
        leftx, lefty = x, y-1
        rightx, righty = x, y
    else:
        return
    
    sx, sy = direction[d]        
    if d == '<':
        while grid_[leftx+sx][lefty+sy] != '.':
            move(leftx+sx, lefty+sy, d)
        
        grid_[leftx+sx][lefty+sy] = '['
        grid_[rightx+sx][righty+sy] = ']'
        grid_[rightx][righty] = '.'

    elif d == '>':
        while grid_[rightx+sx][righty+sy] != '.':
            move(rightx+sx, righty+sy, d)

        grid_[leftx+sx][lefty+sy] = '['
        grid_[rightx+sx][righty+sy] = ']'
        grid_[leftx][lefty] = '.'

    else:
        while grid_[leftx+sx][lefty+sy] != '.' or grid_[rightx+sx][righty+sy] != '.':
            move(leftx+sx, lefty+sy, d)
            move(rightx+sx, righty+sy, d)

        grid_[leftx+sx][lefty+sy] = '['
        grid_[rightx+sx][righty+sy] = ']'
        grid_[leftx][lefty] = '.'
        grid_[rightx][righty] = '.'


for line in f:
    if line.strip() == '':
        flag = True
        continue
    if flag:
        # First puzzle
        for d in line.strip():
            sx, sy = direction[d]
            x, y = robot
            if grid[x+sx][y+sy] == '.':
                grid[x+sx][y+sy] = '@'
                grid[x][y] = '.'
                robot = [x+sx, y+sy]
            elif grid[x+sx][y+sy] == 'O':
                tempx, tempy = x+sx, y+sy
                while grid[tempx][tempy] == 'O':
                    tempx += sx
                    tempy += sy
                if grid[tempx][tempy] == '.':
                    grid[tempx][tempy] = 'O'
                    grid[x+sx][y+sy] = '@'
                    grid[x][y]= '.'
                    robot = [x+sx, y+sy]
        # Second puzzle
        for d in line.strip():
            sx, sy = direction[d]
            x, y = robot_
            if grid_[x+sx][y+sy] == '.':
                grid_[x+sx][y+sy] = '@'
                grid_[x][y] = '.'
                robot_ = [x+sx, y+sy]
            elif grid_[x+sx][y+sy] in ['[',']']:
                if movable(x+sx, y+sy, d):
                    move(x+sx, y+sy, d)
                    grid_[x+sx][y+sy] = '@'
                    grid_[x][y] = '.'
                    robot_ = [x+sx, y+sy]

    else:
        grid.append([a for a in line.strip()])
        if "@" in line:
            robot = [len(grid)-1, line.index('@')]

        temp = []
        for a in line.strip():
            if a == 'O':
                temp += ['[', ']']
            elif a == '@':
                temp += ['@', '.']
            else:
                temp += [a, a]

        grid_.append(temp)  
        if "@" in temp:
            robot_ = [len(grid_)-1, temp.index('@')]

count = 0
for x, line in enumerate(grid):
    for y, char in enumerate(line):
        if char == 'O':
            count += 100*x + y
    # print(''.join(line))
print("Sum of boxes GPS:", count)

count = 0
for x, line in enumerate(grid_):
    for y, char in enumerate(line):
        if char == '[':
            count += 100*x + y
    # print(''.join(line))
print("Sum of big boxes GPS:", count)

f.close()

# ##########
# ......[]..
# .....[]...
# ...[A[B...
# ....[]....
# .....@....
# ..........
# For the big boxes
# Have to move boxes from the leaf of the tree first and then to the root, but to do that
# Need to check whether the whole tree is movable
# If B can't be moved than A also can't be moved even though A "can" be moved
