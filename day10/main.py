
test_input="""16
10
15
5
1
11
7
19
6
12
4"""

test_input2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

# 3 choose 1 = 3 
# 2 choose 1 = 2

with open('input.txt') as f:
    input = f.read()

def as_int_list(input:str):
    return [int(i) for i in input.splitlines()]

# Part 1 
def part_1(input:str): 
    joltage = sorted(as_int_list(input))

    differences = [0, 0, 0, 0]
    max_jolt = max(joltage) + 3

    joltage.append(0)
    joltage.append(max_jolt)
    joltage.sort()

    diffs = []
    for i in range(1, len(joltage)):
        diff = joltage[i] - joltage[i-1]
        diffs.append(diff)

        differences[diff] += 1

    print(differences[1] * differences[3])

    return diffs



def part_2(diffs):
    
    # TODO: Calculate instead of computing by hand
    combinations = [1, 1, 2, 4, 7]
    # Find number of contiguous 1's. Based on the number, multiple

    total = 1
    num_ones = 0
    for val in diffs: 
        if val == 1:
            num_ones += 1
        else: 
            total *= combinations[num_ones]
            num_ones = 0
        
    print(total)

part_1(test_input)
part_1(test_input2)
diffs = part_1(input)

part_2(diffs)

# 1:4 = 7
# 1:3 = 4
# 1:2 = 2

