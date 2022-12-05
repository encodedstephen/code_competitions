#!/usr/bin/env python3

val = {
    # Rock, Paper, Scissors
    'A': 1, 'B': 2, 'C': 3,
    'X': 1, 'Y': 2, 'Z': 3
}

outcomes = {
    #   LOSE, TIE, WIN
    'A': ['Z', 'X', 'Y'],
    'B': ['X', 'Y', 'Z'],
    'C': ['Y', 'Z', 'X']    
}

def score(opp:chr, you:chr) -> int:
    score = val.get(you, 0)
    score += 3 * outcomes.get(opp, []).index(you)
    return score

lines = []
with open("input.txt", "r") as f:
# with open("sample.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

# pt 1
total_score = 0
for line in lines:
    total_score += score( *line.split(' '))
print(total_score)

# pt 2
total_score = 0
"""
X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!
"""
mapping = {
    'X': 0, 
    'Y': 1, 
    'Z': 2
}
for line in lines:

    opp, you = line.split(' ')
    outcome = outcomes[opp][mapping[you]]
    total_score += score(opp, outcome)
print(total_score)
