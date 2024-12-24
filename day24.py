import re
f = open("data/day24.txt", "r")

flag = False
gates = {}
queue = []
operations = {}
for line in f:
    if line.strip() == '':
        flag = True
        continue
    if flag:
        val = re.findall(r'[xyz][0-9]+|[a-z]{3}|AND|OR|XOR', line.strip())
        queue.append(val)
    else:
        val = re.findall(r'[xy][0-9]+|[0-9]+', line.strip())
        gates[val[0]] = int(val[1])

# First puzzle
zgates = []
while len(queue) > 0:
    a, op, b, c = queue[0]
    queue.pop(0)
    if a not in gates or b not in gates:
        queue.append([a,op,b,c])
        continue
    operations[c] = tuple((a,op,b))
    if op == 'AND':
        gates[c] = gates[a] & gates[b]
    elif op == 'OR':
        gates[c] = gates[a] | gates[b]
    elif op == 'XOR':
        gates[c] = gates[a] ^ gates[b]
    if c[0] == 'z':
        zgates.append(c)

zgates.sort()
count = 0
for i, z in enumerate(zgates):
    count += gates[z] * (2 ** i)
print("Output:", count)

# Second puzzle
# Just print everything in order and it should be very clear what is wrong
# Then manually fix it if feel like it
visited = set()
for z in zgates:
    queue = [z]
    while len(queue) > 0:
        c = queue[0]
        queue.pop(0)
        if c in visited:
            continue
        visited.add(c)
        if c[0] in ['x', 'y']:
            continue
        a, op, b = operations[c]
        queue.append(a)
        queue.append(b)
        # print(a, op, b, c)
    # print()

res = ['cmv','z17','rmj','z23','z30','rdg','btb','mwp']
res.sort()
print("Swapped wires in alphabetical order:", ','.join(res))

f.close()
