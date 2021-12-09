#!/usr/bin/env python3

lines = []
with open("input.txt", "r") as f:
# with open("sample.txt", "r") as f:
    lines = [list(map(int,list(line.strip()))) for line in f.readlines()]

# for l in lines:
#     print(l)

# pt 1
max_row = len(lines)
max_col = len(lines[0])
idxs = []

pt2 = []
for r, row in enumerate(lines):
    p2 = []
    for c,col in enumerate(row): 
        check = [col]
        if r > 0: 
            check.append(lines[r-1][c])
        if c > 0:
            check.append(lines[r][c-1])
        if c < max_col - 1:
            check.append(lines[r][c+1])
        if r < max_row - 1:
            check.append(lines[r+1][c])
        
        if min(check) == col and check.count(col) == 1:
            idxs.append((r,c))
        
        p2.append(int(col != 9))
    pt2.append(p2)

sum = 0
for i in idxs: 
    r,c = i
    sum += (lines[r][c] + 1)
print(sum)

# pt 2
visited = set()
def dfs(visited, graph, node):
    if node not in visited: 
        r,c = node
        visited.add(node)
        # print(node)

        if graph[r][c] == 0:
            # We encountered a 9, we don't do any dfs
            return 0

        neighbors = []
        if r > 0: 
            neighbors.append((r-1,c))
        if c > 0:
            neighbors.append((r,c-1))
        if c < max_col - 1:
            neighbors.append((r, c+1))
        if r < max_row - 1:
            neighbors.append((r+1, c))
        
        total = 1
        for n in neighbors: 
            total += dfs(visited, graph, n)

        return total
    return 0

totals = []
for pt in idxs: 
    total = dfs(visited, pt2, pt)
    totals.append(total)

totals.sort(reverse=True)
print(totals[0]*totals[1]*totals[2])
