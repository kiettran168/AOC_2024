f = open("data/day9.txt", "r")

class Node():
    def __init__(self, id, size, free):
        self.id = id
        self.size = size
        self.free = free
        return

    def __str__(self):
        return "id: %s, size: %s, free: %s" % (self.id, self.size, self.free)

files = []
for line in f:
    line = line.strip()
    i = 0
    for sz, fr in zip(line[0::2], line[1::2]):
        files.append(Node(i, int(sz), int(fr)))
        i += 1
    if len(line) % 2 != 0:
        files.append(Node(i, int(line[-1]), 0))

files_ = [Node(i.id, i.size, i.free) for i in files]

# First puzzle
fw = 0  # forward
bw = -1 # backward
while True:
    if fw >= len(files) + bw or fw >= len(files) + 1 + bw or fw >= len(files) or abs(bw) >= len(files):
        break
    if files[fw].free == 0:
        fw += 1
        continue
    if files[bw].size == 0:
        bw -= 1
        continue
    if files[fw].free >= files[bw].size:
        files[fw].free -= files[bw].size
        files[bw].free += files[bw].size
        files.insert(fw+1, Node(files[bw].id, files[bw].size, files[fw].free))
        files[fw].free = 0
        files[bw].size = 0
        fw += 1
        bw -= 1
    else:
        files[bw].size -= files[fw].free
        files.insert(fw+1, Node(files[bw].id, files[fw].free, 0))
        files[fw].free = 0
        fw += 1

pos = -1
count = 0
for i in files:
    n = i.size
    while n > 0:
        pos += 1
        n -= 1
        count += i.id * pos
print("Checksum: ", count)

# Second puzzle
bw = -1 # backward
while abs(bw) < len(files_):
    for fw,i in enumerate(files_):
        if i.free == 0:
            continue
        if i.free >= files_[bw].size and fw < len(files_) + bw:
            files_[fw].free -= files_[bw].size
            files_[bw].free += files_[bw].size
            files_.insert(fw+1, Node(files_[bw].id, files_[bw].size, files_[fw].free))
            files_[fw].free = 0
            files_[bw].size = 0
            break
        elif fw >= len(files_) + bw:
            break
    bw -= 1

pos = -1
count = 0
for i in files_:
    n = i.size
    while n > 0:
        pos += 1
        n -= 1
        count += i.id * pos
    m = i.free
    while m > 0:
        pos += 1
        m -= 1
print("Defragmentation Checksum: ", count)

f.close()
