from itertools import permutations, combinations
f = open("data/day23.txt", "r")

cmp = []
adj = {}
for line in f:
    a,b = line.strip().split('-')
    if a in cmp:
        adj[a] += [b]
    else:
        cmp.append(a)
        adj[a] = [b]
    
    if b in cmp:
        adj[b] += [a]
    else:
        cmp.append(b)
        adj[b] = [a]
l = min([len(i) for i in adj.values()])

# First puzzle
visited = set()
lan = set()
i = 0
while len(visited) != len(cmp):
    a = cmp[i]
    visited.add(a)
    for b in adj[a]:
        if b in visited:
            continue
        for c in adj[b]:
            if c in visited:
                continue
            if c in adj[a] and adj[b]:
                perm = list(permutations([a,b,c]))
                flag = True
                for p in perm:
                    if tuple(p) in lan:
                        flag = False
                        break
                if flag:
                    lan.add((a,b,c))
    i += 1

count = 0
for a, b, c in lan:
    if 't' in [a[0], b[0], c[0]]:
        count += 1
print("Number of LAN parties with a computer starting with 't':", count)

# Second puzzle
party = []
for c in cmp:
    combo = []
    for i in range(len(adj[c]+[c]), l-1, -1):
    # for i in range(10, len(adj[c]+[c])+1):
        combo.extend(list(combinations(adj[c]+[c],i)))
    for co in combo:
        if set(co) in party:
            continue
        flag = True
        for a in adj[c]:
            if a not in co:
                continue
            check = [True if i in adj[a]+[a] else False for i in co]
            if len(set(check)) == 2:
                flag = False
                break
        if flag:
            party.append(set(co))

mxp = [a for a in party if len(a) == max([len(n) for n in party])]
mxp = list(mxp[0])
mxp.sort()
print("Password for the biggest LAN party:", ','.join(mxp))

f.close()
