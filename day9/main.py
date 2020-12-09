PREAMBLE = 25

with open('input.txt') as f:
    numbers = [int(num) for num in f.read().splitlines()]


# Part 1
def two_numbers(stack, summation):
    for num in stack:
        if (summation - num) in stack:
            return (num, num - summation)
    return False

xmas_missing = None
for i in range(PREAMBLE, len(numbers)):

    stack = numbers[i-PREAMBLE:i]
    num = numbers[i]

    if not two_numbers(stack, num):
        xmas_missing = num
        print(num)
        break

# Part 2
def continuous_numbers(stack, summation):
    
    remainder = summation
    stack_len = len(stack)

    for i in range(0, stack_len):
        for j in range(i+1, stack_len):
            if sum(stack[i:j]) == summation:
                return stack[i:j]
    
    return []

combo = continuous_numbers(numbers, xmas_missing)
if len(combo) > 0:
    print(min(combo) + max(combo))
