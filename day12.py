f = open("data/day12.txt", "r")

garden = []
for line in f:
    garden.append(''.join('.' + line.strip() + '.'))

size = len(garden) * (len(garden[0]) - 2)
garden = [''.join('.' for i in range(len(garden[0])))] + garden + [''.join('.' for i in range(len(garden[0])))]
visited = set()
direction = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}

count = 0
count_ = 0
# First puzzle
for x, line in enumerate(garden):
    for y, plot in enumerate(line):
        if (x,y) in visited:
            continue
        if x in [0, len(garden)-1] or y in [0, len(line)-1]:
            continue

        area = 1
        peri = 0
        side = 0
        queue = [(x,y)]
        visited.add((x,y))
        while len(queue) > 0:
            i, j = queue[0]
            queue.pop(0)
            flag = 0
            x1, x2 = 0, 0
            for d in direction:
                a, b = direction[d]
                if garden[i+a][j+b] == plot:
                    flag += 1
                    x1 += a
                    x2 += b
                    if (i+a,j+b) not in visited:
                        queue.append((i+a,j+b))
                        visited.add((i+a,j+b))
                        area += 1
                elif garden[i+a][j+b] != plot:
                    peri += 1
            
            # Second puzzle
            # -1 0 +1 would be more confusing to me
            u1, u2 = direction['U']
            d1, d2 = direction['D']
            l1, l2 = direction['L']
            r1, r2 = direction['R']

            if flag == 0:
                side += 4
            elif flag == 1:
                side += 2
            elif flag == 2:
                if not(garden[i+l1][j+l2] == garden[i+r1][j+r2] == plot or garden[i+u1][j+u2] == garden[i+d1][j+d2] == plot):
                    side += 1
                    if garden[i+x1][j+x2] != plot:
                        side += 1
            elif flag == 3:
                nd = 0
                for d in direction:
                    a, b = direction[d]
                    if garden[i+a][j+b] != plot:
                        nd = d
                if nd == 'U':
                    if garden[i+d1+l1][j+d2+l2] != plot:
                        side += 1
                    if garden[i+d1+r1][j+d2+r2] != plot:
                        side += 1
                elif nd == 'D':
                    if garden[i+u1+l1][j+u2+l2] != plot:
                        side += 1
                    if garden[i+u1+r1][j+u2+r2] != plot:
                        side += 1
                elif nd == 'L':
                    if garden[i+u1+r1][j+u2+r2] != plot:
                        side += 1
                    if garden[i+d1+r1][j+d2+r2] != plot:
                        side += 1
                elif nd == 'R':
                    if garden[i+u1+l1][j+u2+l2] != plot:
                        side += 1
                    if garden[i+d1+l1][j+d2+l2] != plot:
                        side += 1
            elif flag == 4:
                if garden[i+d1+l1][j+d2+l2] != plot:
                        side += 1
                if garden[i+d1+r1][j+d2+r2] != plot:
                        side += 1
                if garden[i+u1+l1][j+u2+l2] != plot:
                        side += 1
                if garden[i+u1+r1][j+u2+r2] != plot:
                        side += 1
           
        count += area * peri
        count_ += area * side
                    

print("Total price of fences by perimeter:", count)
print("Total price of fences by sides:", count_)

f.close()

# Count corners which should equal to sides
# .....
# ..2..
# .121.
# .101.
# .....
# .202.
# .....
# ..2..
# ..2..
# .....
# ..2..
# ..22.
# .....
