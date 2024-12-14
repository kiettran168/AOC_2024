import re

f = open("data/day14.txt", "r")

# First puzzle
count = [0, 0, 0, 0]
points = []
wide, tall = 101, 103
# wide, tall = 11, 7
for line in f:
    x, y, vx, vy = [int(i) for i in re.findall(r'-?[0-9]+', line.strip())]
    points.append([x,y,vx,vy])
    x = (x + 100 * vx) % wide
    y = (y + 100 * vy) % tall
    if x < wide//2:
        if y < tall//2:
            count[0] += 1
        elif y > tall//2:
            count[1] += 1
    elif x > wide//2:
        if y < tall//2:
            count[2] += 1
        elif y > tall//2:
            count[3] += 1

p = 1
for c in count:
    p *= c
print("Safety score after 100 seconds:", p)

# Second puzzle
# Found patterns repeat at 89 + 103n seconds and 11 + 101m seconds
# Easter egg for sure will appear at 89 + 103n == 11 + 101m seconds
# Loop one of the 2 and check if it's divisible by the other after minus
a = 89
# a = 11
while True:
    grid = [['.' for m in range(wide)] for n in range(tall)]
    for p in points:    
        # c = (p[0] + 6475*p[2]) % wide
        # r = (p[1] + 6475*p[3]) % tall
        c = (p[0] + a*p[2]) % wide
        r = (p[1] + a*p[3]) % tall
        grid[r][c] = '#'

    if (a - 11) % 101 == 0:
        # b = open("m.txt", "w")
        # b.write(str(a)+'\n')
        # for y in grid:
        #     for x in y:
        #         b.write(x)
        #     b.write('\n')
        # b.write('\n')
        print("Easter egg found after:", a, "seconds")
        break

    a += 103
    # a += 101

f.close()
