#!/usr/bin/env python3

lines = []
with open("input.txt", "r") as f:
# with open("sample.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

def get_priority(c): 
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return 27 + ord(c) - ord('A')

# pt 1
total_score = 0
for line in lines:
    portion = len(line) // 2
    both = set(line[0:portion]) & set(line[portion:])
    for c in both:
        total_score += get_priority(c)

print(total_score)

# pt 2
if len(lines) % 3 != 0: 
    print('ERROR: Their aren\'t a valid number of rows for groupings of 3.')

total_score = 0
for lines in [lines[n:n+3] for n in range(0, len(lines), 3)]:
    common = set(lines[0]) & set(lines[1]) & set(lines[2])
    for c in common:
        total_score += get_priority(c)
    pass
print(total_score)
