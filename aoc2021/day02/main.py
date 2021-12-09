#!/usr/bin/env python3

lines = []
with open("input.txt", "r") as f:
    lines = f.readlines()

# pt 1
x = 0
y = 0
for line in lines:
    instr, amt = line.split(' ')
    if instr == 'forward':
        x += int(amt)
    elif instr == 'down':
        y += int(amt)
    elif instr == 'up':
        y -= int(amt)
    else:
        print('Unknown instruction: ' + instr)
print(x * y)

# pt 2
horiz = 0
depth = 0
aim = 0
for line in lines:
    instr, amt = line.split(' ')
    if instr == 'forward':
        horiz += int(amt)
        depth += aim * int(amt)
    elif instr == 'down':
        aim += int(amt)
    elif instr == 'up':
        aim -= int(amt)
    else:
        print('Unknown instruction: ' + instr)
print(horiz * depth)
