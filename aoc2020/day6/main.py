import re

union = set()
intersect = set()

total_union = 0
total_intersect = 0
first = True
with open('./input.txt') as input:
    for line in input: 
        if line == '\n':
            total_union += len(union)
            total_intersect += len(intersect)
            union = set()
            intersect = set()
            first = True
            continue 

        current_user = set(a for a in line.rstrip())

        union = union | current_user
        
        if (first): 
            intersect = current_user
            first = False
        else:
            intersect = intersect.intersection(current_user)

total_union += len(union)
total_intersect += len(intersect)

print("Total Union (first_star): ", total_union)
print("Total Intersect (second star): ", total_intersect)
