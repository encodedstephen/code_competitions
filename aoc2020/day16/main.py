import re

with open('input.txt') as f:
    input = f.read()

def parse_input(input:str):
    
    rules = {}
    tickets = []
    for line in input.splitlines():
        if '-' in line: 
            # Process as rule: 
            name, valid = re.match('(.*): (.*)', line).groups()
            rules[name] = []
            for v in re.findall('(\d+)-(\d+)', valid): 
                rules[name] += list(range(int(v[0]), int(v[1]) + 1))
        elif ',' in line: 
            tickets.append([int(i) for i in line.split(',')])
    
    return (rules, tickets)

def part_1(input:str): 
    rules, tickets = parse_input(input)
    
    valid_nums = []
    for k,v in rules.items():
        valid_nums += v

    invalids = 0
    for ticket in tickets[1:]: 
        for num in ticket: 
            if num not in valid_nums: 
                invalids += num
    
    return invalids

# Part 1
test_input = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

print("Part 1 (test) = %d" % part_1(test_input))
print("Part 1 (act)  = %d" % part_1(input))

def part_2(input:str): 
    rules, tickets = parse_input(input)
    rule_list = rules.keys()

    # Get a list of all valid numbers
    valid_nums = []
    for k,v in rules.items():
        valid_nums += v

    ticket_length = len(tickets[0])
    section = [set(rule_list) for i in range(0, ticket_length)]

    for ticket in tickets: 
        # Ensure we have a valid ticket
        if sum([num in valid_nums for num in ticket]) < ticket_length:
            continue

        # We have a valid ticket, now let's try and narrow down the field
        for i, num in enumerate(ticket): 
            updated = set()
            for rule_key in section[i]:
                vn = rules[rule_key]
                if num in vn:
                    updated.add(rule_key)
            section[i] = updated
    
    # We have our sections, but they have repeated fields. 
    chosen = set()
    lengths = [len(sec) for sec in section]
    for i in sorted(lengths):
        idx = lengths.index(i)
        
        # Subtract the items that we have already used: 
        remaining = set(section[idx]) - chosen
        if len(remaining) == 1: 
            val = remaining.pop()

            section[idx] = val
            chosen.add(val)
    
    total = 1
    my_ticket = tickets[0]
    for i, sec in enumerate(section): 
        if 'departure' in sec: 
            total *= my_ticket[i]
    
    return total

# Part 2 
test_input = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""
print("Part 2 (test) = %d" % part_2(test_input))
print("Part 2 (act)  = %d" % part_2(input))
