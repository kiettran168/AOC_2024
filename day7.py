f = open("data/day7.txt", "r")

# First puzzle
def check(lhs, rhs):
    if len(rhs) == 1:
        if rhs[0] == lhs: return lhs
        else: return 0
    rhsa = [rhs[0] + rhs[1]]
    rhsm = [rhs[0] * rhs[1]]
    if len(rhs) > 2:
        rhsa += rhs[2:]
        rhsm += rhs[2:]
    add = check(lhs, rhsa)
    mul = check(lhs, rhsm)
    if add == lhs or mul == lhs:
        return lhs
    else:
        return 0

# Second puzzle
def check_(lhs, rhs):
    if len(rhs) == 1:
        if rhs[0] == lhs: return lhs
        else: return 0
    rhsa = [rhs[0] + rhs[1]]
    rhsm = [rhs[0] * rhs[1]]
    rhsc = [int(str(rhs[0])+str(rhs[1]))]
    if len(rhs) > 2:
        rhsa += rhs[2:]
        rhsm += rhs[2:]
        rhsc += rhs[2:]
    add = check_(lhs, rhsa)
    mul = check_(lhs, rhsm)
    comb = check_(lhs, rhsc)
    if add == lhs or mul == lhs or comb == lhs:
        return lhs
    else:
        return 0

total = 0
total_ = 0
for line in f:
    line = line.strip()
    lhs = int(line.split(':')[0])
    rhs = [int(a) for a in line.split(':')[1].split()]
    total += check(lhs, rhs)
    total_ += check_(lhs, rhs)

print("Total calibration result: ", total)
print("Total calibration result for real this time:", total_)

f.close()
