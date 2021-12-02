import tqdm

with open('input.txt') as f:
    input = f.readline().split(",")

def game(input, iter_len:int = 2020): 

    last_seen = dict()
    last_num = input[0]

    for i in range(1, len(input)):
        last_seen[last_num] = i - 1
        last_num = input[i]

    for i in tqdm.tqdm(range(len(input), iter_len)):
        # Find the last_number in the list. 
        # print("Attempting to find the last index for %d." % last_num)
        if last_num not in last_seen: 
            # We haven't had this number prior: 
            next_num = 0
        else: 
            next_num = i - last_seen[last_num] - 1
        
        last_seen[last_num] = i - 1
        last_num = next_num

    return last_num

# Part 1
# print("Part 1 = %d" % game([0,3,6]))
# print("Part 1 = %d" % game([1,3,2]))
# print("Part 1 = %d" % game([2,1,3]))
# print("Part 1 = %d" % game([1,2,3]))
# print("Part 1 = %d" % game([2,3,1]))
# print("Part 1 = %d" % game([3,2,1]))
# print("Part 1 = %d" % game([3,1,2]))
print("Part 1 = %d" % game([14,8,16,0,1,17], 2020))

# Part 2
# print("Part 2 = %d" % game([2,1,3], 30000000))
# print("Part 2 = %d" % game([1,2,3], 30000000))
# print("Part 2 = %d" % game([2,3,1], 30000000))
# print("Part 2 = %d" % game([3,2,1], 30000000))
# print("Part 2 = %d" % game([3,1,2], 30000000))
print("Part 2 = %d" % game([14,8,16,0,1,17], 30000000))
