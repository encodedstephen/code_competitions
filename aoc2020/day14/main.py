import re 

def part_1 (input_str) -> dict:

    mask = None
    mem = {}

    for line in input_str.split('\n'): 
        if 'mask' in line: 
            # We have a new grouping
            mask = re.match('mask = ([01X]+)', line).group(1)
        elif 'mem[' in line: 
            addr, dec_val = re.match('mem\[(\d+)\] = (\d+)', line).groups()
            dec_bin = bin(int(dec_val)).lstrip('0b').zfill(len(mask))
            mem[addr] = (dec_bin[::-1], mask[::-1])

    calc = {}
    for mem, info in mem.items():

        val, mask = info
        result = ""
        for i in range(0, len(mask)):
            x = val[i]
            m = mask[i]

            if m == 'X': 
                result += x
            else:
                result += m
            
        calc[mem] = int(result[::-1],2)

    return calc

        
def part_2(input_str) -> dict:

    mask = None
    mem = {}

    for line in input_str.split('\n'): 
        if 'mask' in line: 
            # We have a new grouping
            mask = re.match('mask = ([01X]+)', line).group(1)
        elif 'mem[' in line: 
            addr, dec_val = re.match('mem\[(\d+)\] = (\d+)', line).groups()
            mask_len = len(mask)
            addr_bin = bin(int(addr)).lstrip('0b').zfill(mask_len)
            
            result = ''
            for i in range(0, mask_len):
                x = addr_bin[i]
                m = mask[i]

                if m == '0': 
                    result += x
                else:
                    result += m

            num_xs = result.count('X')
            for i in range(0, 2 ** num_xs):
                mem_computed = result
                replacements = bin(i).lstrip('0b').zfill(num_xs)
                for char in replacements: 
                    mem_computed = mem_computed.replace('X', char, 1)
            
                mem[int(mem_computed,2)] = int(dec_val)

    return mem

with open('input.txt') as f:
    input = f.read().rstrip("\n")

# Part 1
test_input = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
vals = part_1(test_input)
print("Part 1 = ", sum(vals.values()))
vals = part_1(input)
print("Part 1 = ", sum(vals.values()))

# Part 2
test_input = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""
vals = part_2(test_input)
print("Part 2 = ", sum(vals.values()))
vals = part_2(input)
print("Part 2 = ", sum(vals.values()))
