# First puzzle
f = open("data/day1.txt", "r")
left = []
right = []
for line in f:
    line.strip()
    line = line.split('   ')
    left += [int(line[0])]
    right += [int(line[1])]

left.sort()
right.sort()
print("Total distance between the lists: ", sum([abs(left[i]-right[i]) for i in range(len(left))]))

# Second puzzle
print("Similarity score: ", sum([left[i] * right.count(left[i]) for i in range(len(left))]))

f.close()
