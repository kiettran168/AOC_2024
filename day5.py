f = open("data/day5.txt", "r")

flag = True
incorrect = []
before = {}
count = 0

def check(seq):
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if seq[i] in before:
                if seq[j] in before[seq[i]]:
                    return True
    return False

#   First puzzle
for line in f:
    line = line.strip()
    if line == "": flag = False
    else:
        if flag:
            line = [int(i) for i in line.split('|')]
            if line[1] in before:
                before[line[1]] += [line[0]]
            else:
                before[line[1]] = [line[0]]
        else:
            seq = [int(i) for i in line.split(',')]
            if not check(seq):
                count += seq[int(len(seq)/2)]
            else:
                incorrect += [seq]
print("Middle page number total of correct updates: ", count)

# Second puzzle
# Thought I had to implement some kind of sort 
# but I tried swapping around to see what would happen
# and turns out just swapping around worked so...
# weird...
count_ = 0
for seq in incorrect:
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if seq[i] in before:
                if seq[j] in before[seq[i]]:
                    seq[i], seq[j] = seq[j], seq[i]
    count_ += seq[int(len(seq)/2)]
print("Middle page number total of incorrect updates: ", count_)


f.close()
        
