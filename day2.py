f = open("data/day2.txt", "r")

def analyze(line):
    if line[0] < line[1]:
        flag = True     # Increase
    else:
        flag = False

    check = True
    prev = line[0]
    for i in range(1, len(line)):
        if flag and line[i] - prev in [1,2,3]:
            prev = line[i]
        elif not flag and prev - line[i] in [1,2,3]:
            prev = line[i]
        else:
            check = False
            break
    return check

safe = 0
safe_ = 0
unsafe = []

# First puzzle
for line in f:
    line.strip()
    line = [int(i) for i in line.split()]
    if analyze(line): safe += 1
    else:
        unsafe += [line]
print("Number of safe reports: ", safe)

# Second puzzle
for line in unsafe:
    check = 0
    for i in range(len(line)):
        line_ = [a for a in line]
        line_.pop(i)
        if analyze(line_):
            safe_ += 1
            break
print("Number of actual safe reports: ", safe + safe_)

f.close()
