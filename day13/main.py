
from functools import reduce

test_input = """939
7,13,x,x,59,x,31,19"""

with open('input.txt') as f:
    input = f.read().splitlines()


def part_1(input):
    start_time = int(input[0])
    schedule = [int(schedule_time)
                for schedule_time in input[1].split(',') if schedule_time != 'x']

    # print(start_time)
    # print(schedule)

    wait_time = []
    for s in schedule:
        wait_time.append(s - (start_time % s))

    bus_wait_time = min(wait_time)
    bus = schedule[wait_time.index(bus_wait_time)]

    return (bus, bus_wait_time)


# Part 1
bus, wait_time = part_1(input)
print("Part 1 = ", bus * wait_time)

def chinese_remainder(n, a):
    sum = 0
    
    # Find the "max" number based on multiplying all of the n's together:
    product = 1
    for num in n:
        product *= num
    
    for n_i, a_i in zip(n, a):
        p = product // n_i

        r, s, t = euclidean_gcd(p, n_i)
        sum += a_i * s * p
        
    return sum % product

def euclidean_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient, remainder = divmod(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    
    return old_r, old_s, old_t

# timestamp = part_2(test_input.split('\n')[1])
# print("Part 2 = ", timestamp)
# print(lcm(17, 13))


def part_2(input):

    # Build up chinese remainder theorem input: 
    numbers = []
    remainder = []

    for i, num in list(enumerate(input.split(','))):
        if num == 'x':
            continue
        
        num = int(num)
        numbers.append(num)
        remainder.append((-1 * i) % num)

    # print(numbers, remainder)
    return chinese_remainder(numbers, remainder)

print("")
# print("Part 2 = %d" % part_2(test_input.split('\n')[1]))
# print("Part 2 = %d" % part_2("67,7,59,61"))
# print("Part 2 = %d" % part_2("67,7,x,59,61"))
# print("Part 2 = %d" % part_2("1789,37,47,1889"))
print("Part 2 = %s" % part_2(input[1]))
