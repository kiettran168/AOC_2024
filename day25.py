f = open("data/day25.txt", "r")

keys = []
locks = []
grids = []
components = []
for line in f:
    if line.strip() == '':
        components.append(grids)
        grids = []
    else:
        grids.append(line.strip())

for com in components:
    count = [a.count('#')-1 for a in [[com[i][j] for i in range(len(com))] for j in range(len(com[0]))]]
    if '.' in com[0]:
        # Key
        keys.append(count)
    else:
        # Lock
        locks.append(count)

count = 0
for l in locks:
    for k in keys:
        flag = True
        for a, b in zip(l,k):
            if a + b > 5:
                flag = False
                break
        if flag:
            count += 1
print("Numbers of unique lock and key combinations:", count)
f.close()
