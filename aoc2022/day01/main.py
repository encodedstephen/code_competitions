#!/usr/bin/env python3
import numpy as np 

lines = []
with open("input.txt", "r") as f:
# with open("sample.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

# pt 1
elves = []
curr = []
for line in lines:
    if line.isnumeric():
        curr.append(int(line))
    else:
        elves.append(sum(curr))
        curr = []

if len(curr) != 0:
    elves.append(sum(curr))

idx = np.argmax(elves)
print(elves[idx])

# pt 2
print(sum(sorted(elves, reverse=True)[0:3]))
