import re
# import sympy as sp
# from sympy.abc import x, y
# from sympy.solvers import solve
f = open("data/day13.txt", "r")

info = []
count = 0
count_ = 0
for line in f:
    line = line.strip()
    if line == '':
        # button_A = [int(i) for i in re.findall(r'[0-9]+', info[0])]
        # button_B = [int(i) for i in re.findall(r'[0-9]+', info[1])]
        # prize = [int(i) for i in re.findall(r'[0-9]+', info[2])]

        # First puzzle
        ax, ay = [int(i) for i in re.findall(r'[0-9]+', info[0])]
        bx, by = [int(i) for i in re.findall(r'[0-9]+', info[1])]
        px, py = [int(i) for i in re.findall(r'[0-9]+', info[2])]

        # nb = (pxay - axpy) / (bxay - axby)
        # na = (pxby - bxpy) / (axby - bxay)
        nb = (px*ay - ax*py) / (bx*ay - ax*by)
        na = (px*by - bx*py) / (ax*by - bx*ay)

        if na % 1 == 0 and nb % 1 == 0:
            count += 3 * round(na) + round(nb)
        
        # Second puzzle
        px += 10000000000000
        py += 10000000000000

        nb = (px*ay - ax*py) / (bx*ay - ax*by)
        na = (px*by - bx*py) / (ax*by - bx*ay)

        if na % 1 == 0 and nb % 1 == 0:
            count_ += 3 * round(na) + round(nb)

        # eq1 = sp.Eq(button_A[0]*x+button_B[0]*y, prize[0]) 
        # eq2 = sp.Eq(button_A[1]*x+button_B[1]*y, prize[1]) 
        # output = solve([eq1,eq2],dict=True)
        # a = output[0][x]
        # b = output[0][y]
        # if a % 1 == 0 and b % 1 == 0:
        #     count += 3*a + b

        # eq1 = sp.Eq(button_A[0]*x+button_B[0]*y, 10000000000000 + prize[0]) 
        # eq2 = sp.Eq(button_A[1]*x+button_B[1]*y, 10000000000000 + prize[1]) 
        # output = solve([eq1,eq2],dict=True)
        # a = output[0][x]
        # b = output[0][y]
        # if a % 1 == 0 and b % 1 == 0:
        #     count_ += 3*a + b

        info = []
    else:
        info.append(line)

print("Fewest tokens to win all prizes:", count)
print("More fewest tokens to win all prizes:", count_)

f.close()
