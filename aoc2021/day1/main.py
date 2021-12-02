#!/usr/bin/env python3
import numpy as np 

lines = []
with open("input.txt", "r") as f:
    lines = [int(l) for l in f.readlines()]

# pt 1
valid = 0
prev = lines[0]
for curr in lines[1:]:
    if curr > prev:
        valid += 1
    prev = curr
print(valid)

# pt 2
valid = 0
results = np.convolve(lines, np.ones(3,dtype=int), 'valid')
prev = results[0]
for curr in results:
    if curr > prev:
        valid += 1
    prev = curr
print(valid)
