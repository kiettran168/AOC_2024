import re
import time
f = open("data/day17.txt", "r")

instr = []
for line in f:
    if line.strip() == "":
        continue
    instr.append([int(i) for i in re.findall(r'[0-9]+', line.strip())])

A = instr[0][0]
B = instr[1][0]
C = instr[2][0]
instr = instr[3]
pointer = 0
program = {}
for opcode, operand in zip(instr[0::2],instr[1::2]):
    program[pointer] = (opcode, operand)
    pointer += 2
end = pointer

def interpret(A, B, C):
    pointer = 0
    output = []
    while pointer < end:
        opcode, operand = program[pointer]
        if opcode in [0, 2, 5, 6, 7]:
            if operand == 4:
                operand = A
            elif operand == 5:
                operand = B
            elif operand == 6:
                operand = C

        if opcode == 0:        
            v = A // (2**operand)
            A = v
        elif opcode == 1:
            v = B ^ operand
            B = v
        elif opcode == 2:
            v = operand % 8
            B = v
        elif opcode == 3:
            if A != 0:
                pointer = operand
                continue
        elif opcode == 4:
            v = B ^ C
            B = v
        elif opcode == 5:
            v = operand % 8
            output.append(v)
        elif opcode == 6:
            B = A // (2**operand)
        elif opcode == 7:
            C = A // (2**operand)
        pointer += 2

    return ','.join([str(i) for i in output])

# First puzzle
print("Output: ", interpret(A,B,C))

# Second puzzle
prev_ = [0]
for x in range(16):
    prev = [i for i in prev_]
    prev_ = []
    for p in prev:
        for n in range(8):
            A = p*8+n
            if interpret(A,B,C) == ','.join([str(i) for i in instr[(15-x):]]):
                prev_.append(A)
print("RegA: ", min(prev_))

f.close()
