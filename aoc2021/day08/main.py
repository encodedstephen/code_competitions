#!/usr/bin/env python3
from itertools import permutations

# Make sure lights is in alphabetical order. We will use this property when guessing
lights = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf','abdfg', 'abdefg','acf','abcdefg', 'abcdfg']

def guess_perm(input_list): 
    
    # Generate all of the permutations for this list of characters
    for p in permutations('abcdefg'):
        found = True
        keymap = dict(zip(p, 'abcdefg'))
        new_list = []
        for word in input_list:
            # Make sure your converted value is sorted in abc order for lookup later
            converted = ''.join(sorted([keymap[c] for c in word ]))

            if converted not in lights:
                # this is not the permutation
                found = False
                break

            new_list.append(converted)

        if found:
            return [str(lights.index(item)) for item in new_list]      

    return False

lines = []
with open("input.txt", "r") as f:
# with open("sample2.txt", "r") as f:
# with open("sample.txt", "r") as f:
    for line in f.readlines():
        test, output = line.split('|')
        tests = (test.strip().split(' '))
        outputs = output.strip().split(' ')
        lines.append((tests, outputs))

# pt 1
valid = 0
for line in lines:
    tests, outputs = line
    lengths = {}
    for txt in outputs:
        l = len(txt)
        if l not in lengths:
            lengths[l] = 0
        lengths[l] += 1
    
    valid += lengths.get(2, 0)
    valid += lengths.get(4, 0)
    valid += lengths.get(3, 0)
    valid += lengths.get(7, 0)   
print(valid)

# pt 2
valid = 0
for line in lines: 
    tests, outputs = line
    guess = guess_perm(tests+outputs)

    # Only grab the output area and convert into a number
    num = int(''.join(guess[-1 * len(outputs):]))
    valid += num
print(valid)

