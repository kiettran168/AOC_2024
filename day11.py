import copy

f = open("data/day11.txt", "r")

stones = {}
for line in f:
    for s in [int(i) for i in line.strip().split()]:
        stones[s] = 1

# First puzzle
# Second puzzle
n = 0
while n < 75:
    queue = {}
    for s in stones:
        loads = stones[s]
        if s == 0:
            if 1 in queue:
                queue[1] += loads
            else:
                queue[1] = loads
        elif len(str(s)) % 2 == 0:
            l = len(str(s)) // 2
            left = int(str(s)[:l])
            right = int(str(s)[l:])
            if left in queue:
                queue[left] += loads
            else:
                queue[left] = loads
            if right in queue:
                queue[right] += loads
            else:
                queue[right] = loads
        else:
            if (2024*s) in queue:
                queue[2024*s] += loads
            else:
                queue[2024*s] = loads

    stones = copy.deepcopy(queue)
    n += 1

    if n in [25, 75]:
        count = 0
        for s in stones:
            count += stones[s]
        print("Stones after blinking", n, "times: ", count)
    
f.close()
