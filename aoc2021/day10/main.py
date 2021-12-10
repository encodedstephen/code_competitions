#!/usr/bin/env python3

lines = []
with open("input.txt", "r") as f:
# with open("sample.txt", "r") as f:
    lines = f.readlines()

pairs = {
    '(':')',
    '[':']',
    '{':'}',
    '<':'>'
}
opens = pairs.keys()

scores = {
    'syntax': {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    },
    'autocomplete': {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
}

def score_stack(remaining_chars):
    # print(remaining_chars)
    total = 0
    for i in range(len(remaining_chars)):
        c = remaining_chars.pop()
        total = total * 5 + scores['autocomplete'][c]
    return total

illegal_chars = {}
auto_complete_score = []
for line in lines:
    line = line.strip()

    stack = []

    skip = False    
    for c in line: 
        if c in opens:
            stack.append(pairs[c])
        elif stack[-1] == c: 
            stack.pop()
        else:
            if c not in illegal_chars:
                illegal_chars[c] = 0
            illegal_chars[c] += 1
            # print("Expected %s, but found %s instead." % (stack[-1], c))
            skip = True
            break
    
    if not skip: 
        # Figure out the score for autocomplete for this line
        auto_complete_score.append(score_stack(stack))

# pt 1
sums = 0      
for char, cnt in illegal_chars.items(): 
    sums += scores['syntax'][char] * cnt
print(sums)

# pt 2
acs_len = len(auto_complete_score)
auto_complete_score.sort()
print(auto_complete_score[int(acs_len/2)])
