import re

f = open("data/day3.txt", "r")

res = 0
res_ = 0    
flag = True
for line in f:
    # First puzzle
    ops = re.findall(r'mul\([0-9]+,[0-9]+\)', line)
    for op in ops:
        nums = [int(a) for a in re.findall(r'\d+', op)]
        if nums[0] < 1000 and nums[1] < 1000:
            res += nums[0] * nums[1]

    # Second puzzle
    ops_ = re.findall(r'don\'t\(\)|do\(\)|mul\([0-9]+,[0-9]+\)', line)
    for op in ops_:
        if op == "don't()":
            flag = False
            continue
        elif op == "do()":
            flag = True
            continue
        elif flag:
            nums = [int(a) for a in re.findall(r'\d+', op)]
            if nums[0] < 1000 and nums[1] < 1000:
                res_ += nums[0] * nums[1]

    # print(ops_)

print("The results of the operations: ", res)
print("The better results of the operations: ", res_)

f.close()
