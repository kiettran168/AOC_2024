import math
f = open("data/day22.txt", "r")

count = 0
seq = {}
for line in f:
    number = int(line.strip())
    window = [number%10]
    visited = set()
    for i in range(2000):
        number = ((number * 64) ^ number) % 16777216
        number = (math.floor(number / 32) ^ number) % 16777216
        number = ((number * 2048) ^ number) % 16777216
        
        # Second puzzle
        window.append(number % 10)

        if len(window) == 5:
            d = tuple([window[i]-window[i-1] for i in range(1,5)])
            # print(d)
            if d not in visited:
                visited.add(d)
                if d in seq:
                    seq[d] += window[-1]
                else:
                    seq[d] = window[-1]
            window.pop(0)
        temp = number
    # First puzzle
    count += number    
print("Sum of secret numbers:", count)
print("Maximum bananas get:", max(seq.values()))
f.close()
