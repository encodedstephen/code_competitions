#!/usr/bin/env python3
import numpy as np 

lines = []
with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

num_instr = len(lines)
len_instr = len(lines[0])

sum = [0] * len_instr
for line in lines:
    for i, c in enumerate(line):
        sum[i] += int(c)

# pt 1
gamma = [0] * len_instr # most common 
epsilon = [0] * len_instr # least common

for i, s in enumerate(sum): 
    gamma[i] = int(s > num_instr / 2)
    epsilon[i] = str(1 - gamma[i])
    gamma[i] = str(gamma[i])

g = int(''.join(gamma),2)
e = int(''.join(epsilon),2)
print(g * e)


# pt 2
valid = 0

remaining = lines
for i in range(len_instr):
    left = []
    right = []
    for l in remaining: 
        if l[i] == '1':
            left.append(l)
        else:
            right.append(l)

    if len(left) >= len(right):
        remaining = left
    else:
        remaining = right
    
    if len(remaining) == 1:
        break

oxygen = int(remaining[0], 2)

remaining = lines
for i in range(len_instr):
    left = []
    right = []
    for l in remaining: 
        if l[i] == '0':
            left.append(l)
        else:
            right.append(l)

    if len(left) <= len(right):
        remaining = left
    else:
        remaining = right
    
    if len(remaining) == 1:
        break
    
co2 = int(remaining[0], 2)

print( oxygen * co2 )
