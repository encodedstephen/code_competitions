#!/usr/bin/env python3
import statistics 
import math 

positions = []
with open("input.txt", "r") as f:
# with open("sample.txt", "r") as f:
    positions = list(map(int, f.readline().split(',')))

# pt 1
mean = round(statistics.mean(positions))
min_moves = math.inf
min_idx = 0
for idx in range(max(positions)):
    moves = sum([abs(pos - idx) for pos in positions])
    if moves < min_moves:
        print("Position %d = %d moves" % (idx, moves))
        min_moves = moves
        min_idx = idx
print(min_idx)
print(min_moves)

# pt 2
mean = round(statistics.mean(positions))
min_moves = math.inf
min_idx = 0
for idx in range(max(positions)):
    moves = [abs(pos - idx) for pos in positions]
    moves = sum([ int((n * (n + 1)) / 2) for n in moves])
    if moves < min_moves:
        print("Position %d = %d moves" % (idx, moves))
        min_moves = moves
        min_idx = idx
print(min_idx)
print(min_moves)
