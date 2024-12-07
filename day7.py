f = open("data/day7.txt", "r")

# First puzzle
# def check(lhs, rhs):
#     if rhs[0] > lhs: return False
#     if len(rhs) == 1:
#         if rhs[0] == lhs: return True
#         else: return False
#     rhsa = [rhs[0] + rhs[1]]
#     rhsm = [rhs[0] * rhs[1]]
#     if len(rhs) > 2:
#         rhsa += rhs[2:]
#         rhsm += rhs[2:]
#     add = check(lhs, rhsa)
#     mul = check(lhs, rhsm)
#     return add or mul    

def check(lhs, rhs):
    if len(rhs) == 0 or lhs <= 0:
        return False
    if lhs == rhs[0]:
        return True
    a = lhs - rhs[-1]
    b = 0
    if lhs % rhs[-1] == 0:
        b = lhs // rhs[-1]
    return check(a, rhs[:-1]) or check(b, rhs[:-1])

# Second puzzle
# def check_(lhs, rhs):
#     if rhs[0] > lhs: return False
#     if len(rhs) == 1:
#         if rhs[0] == lhs: return True
#         else: return False
#     rhsa = [rhs[0] + rhs[1]]
#     rhsm = [rhs[0] * rhs[1]]
#     rhsc = [int(str(rhs[0])+str(rhs[1]))]
#     # rhsc = [rhs[0]*(10**math.ceil(math.log(rhs[1], 10)))+rhs[1]]
#     if len(rhs) > 2:
#         rhsa += rhs[2:]
#         rhsm += rhs[2:]
#         rhsc += rhs[2:]
#     add = check_(lhs, rhsa)
#     mul = check_(lhs, rhsm)
#     comb = check_(lhs, rhsc)
#     return add or mul or comb

def check_(lhs, rhs):
    if len(rhs) == 0 or lhs <= 0:
        return False
    if len(rhs) == 1:
        if lhs == rhs[0]:
            return True
    a = lhs - rhs[-1]
    b = 0
    if lhs % rhs[-1] == 0:
        b = lhs // rhs[-1]
    c = int((str(lhs)[:(len(str(lhs))-len(str(rhs[-1])))])+'0') // 10
    d = int((str(lhs)[(len(str(lhs))-len(str(rhs[-1]))):])+'0') // 10   
    if d != rhs[-1]:
        c = 0
    return check_(a, rhs[:-1]) or check_(b, rhs[:-1]) or check_(c, rhs[:-1])

total = 0
total_ = 0
for line in f:
    line = line.strip()
    lhs = int(line.split(':')[0])
    rhs = [int(a) for a in line.split(':')[1].split()]
    if check(lhs, rhs):
        total += lhs
        total_ += lhs
    else:
        if check_(lhs, rhs):
            total_ += lhs

print("Total calibration result: ", total)
print("Total calibration result for real this time:", total_)

f.close()
