#!/usr/bin/env python3        
import numpy as np

grid = np.zeros((10, 10))
with open("input.txt", "r") as f:
# with open("sample2.txt", "r") as f:
    for x, line in enumerate(f.readlines()):
        for y, octopus in enumerate(line.strip()):
            grid[x][y] = int(octopus)

flashes = []
flash_step = []
def flash(grid, x, y):
    if grid[x][y] >= 10 and (x,y) not in flash_step:
        # flash
        flash_step.append((x,y))

        minx = max(0, x-1)
        miny = max(0, y-1)
        maxx = min(x+1, len(grid) - 1)
        maxy = min(y+1, len(grid[x]) - 1)

        # print(f"checking ({x},{y}): [{minx}:{maxx}][{miny}:{maxy}]")
        for x_i in range(minx, maxx+1):
            for y_i in range(miny, maxy+1): 
                if x != x_i or y != y_i:
                    grid[x_i][y_i] += 1
                    # print(f"({x_i},{y_i}) => {grid[x_i][y_i]}")
                    flash(grid, x_i, y_i)

for i in range(1,500):

    flash_step = []

    grid += 1

    adds = np.zeros(grid.shape)
    for x, row in enumerate(grid):
        for y, octopus in enumerate(row):
            # check to see how many 10s we have for this octopus
            flash(grid, x, y)

    num_flashes = np.sum(grid > 9)
    flashes.append(num_flashes)

    grid[grid > 9] = 0  

    # if i % 10 == 0: 
        # print("After step %d:" % i)
        # print(grid)
        # print(sum(flashes), flashes[-1])
# pt 1
print(sum(flashes[0:100]))

# pt 2
print(flashes.index(100) + 1)
