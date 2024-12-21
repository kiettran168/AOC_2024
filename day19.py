from functools import lru_cache

f = open("data/day19.txt", "r")

flag = False
towels = []
count = 0

# First puzzle
# Second puzzle
@lru_cache
def check(pattern):
    count = 0
    if len(pattern) == 0:
        return 1
    for t in towels:
        if pattern.startswith(t):
            count += check(pattern.removeprefix(t))
    return count

count = 0
count_ = 0
for line in f:
    if line.strip() == '':
        flag = True
        towels.sort()
        towels_ = towels[::-1]
        continue
    if flag:
        pattern = line.strip()
        n = check(pattern)
        if n > 0:
            count += 1
        count_ += n
    else:
        towels = [i for i in line.strip().split(', ')]
print("Patterns that can be arranged:", count)
print("All possible ways to arrange patterns:", count_)

f.close()



