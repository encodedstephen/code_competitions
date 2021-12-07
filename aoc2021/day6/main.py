#!/usr/bin/env python3

fish_age = [0] * 9

with open("input.txt", "r") as f:

    for age in f.readline().split(','):
        fish_age[int(age)] += 1

def next_day(fish_age):
    next_age = [0] * 9
    for i in range(1,9):
        next_age[i - 1] = fish_age[i]
    next_age[8] = fish_age[0]
    next_age[6] += fish_age[0]

    return next_age

# pt 1
for day in range(80):
    fish_age = next_day(fish_age)
print(sum(fish_age))

# pt 2
for day in range(80, 256):
    fish_age = next_day(fish_age)
print(sum(fish_age))
