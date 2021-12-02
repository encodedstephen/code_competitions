from typing import List

with open('input.txt') as f:
    instructions = f.read().splitlines()

def run_instructions(instructions: List[str], visited: List[int], accumulator: int = 0, curr_index: int = 0): 

    while True:

        # Check to see if we have visited this instruction before: 
        if curr_index in visited: 
            raise Exception("Infinite loop detected. Accumulator = %d" % accumulator)

        # Set the visited index
        visited.append(curr_index)
        
        # Decode the instruction
        instr = instructions[curr_index]
        if 'nop' == instr[0:3]:
            curr_index += 1
        elif 'acc' == instr[0:3]:
            accumulator += int(instr[4:])
            curr_index += 1
        elif 'jmp' == instr[0:3]:
            curr_index += int(instr[4:])

        # Check to see if we reached the end of the program
        if curr_index == len(instructions):
            return accumulator

try:
    visited = []
    run_instructions(instructions, visited,  accumulator = 0, curr_index = 0)
except Exception as e:
    print(e)

# Attempt to correct the infinite loop by modifying on the instruction path: 
for i in visited:

    instr = instructions[i][0:3]
    if instr == 'acc':
        continue
    
    if instr == 'nop':
        # switch to jmp and check 
        previous = instructions[i]
        instructions[i] = instructions[i].replace('nop', 'jmp')
        try:
            acc = run_instructions(instructions, [],  accumulator = 0, curr_index = 0)
            print("Accumulator = ", acc)
            break
        except:
            instructions[i] = previous
    else:
        previous = instructions[i]
        instructions[i] = instructions[i].replace('jmp', 'nop')
        try:
            acc = run_instructions(instructions, [],  accumulator = 0, curr_index = 0)
            print("Accumulator = ", acc)
            break
        except:
            instructions[i] = previous
    
