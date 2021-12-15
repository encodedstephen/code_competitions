#!/usr/bin/env python3
from collections import Counter, defaultdict

lines = []
with open("input.txt", "r") as f:
# with open("sample.txt", "r") as f:
    chemical = f.readline().strip()

    subs = {}
    for l in f.readlines():
        if ' -> ' in l:
            pair, sub = l.strip().split(' -> ')
            subs[pair] = sub

def print_count(pairs):
    char_count = defaultdict(int)

    # Count each left character in the pairs
    for k,v in pairs.items(): 
        char_count[k[0]] += v

    # Add the last character from the list (since we add to the middle)
    char_count[chemical[-1]] += 1

    # Compute max - min based on the counts of the dict
    res = Counter(char_count)
    print(max(res.values()) - min(res.values()))


# Initialize the pairs based on the given input
pairs = defaultdict(int)
for i in range(len(chemical) - 1):
    sub = chemical[i:i+2]
    pairs[sub] += 1

for step in range(1,41):

    new_pair = defaultdict(int)
    for pair in pairs:
        ch = subs[pair]
        # AC -> B | AC => AB & AC
        new_pair[pair[0] + ch] += pairs[pair]
        new_pair[ch + pair[1]] += pairs[pair]
    
    pairs = new_pair

    # pt 1
    if step == 10:
        print_count(pairs)

# pt 2
print_count(pairs)
