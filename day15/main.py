with open('input.txt') as f:
    input = f.readline().split(",")

def part_1(input, iter_len:int = 10): 

    previously_seen = set()
    for i in range(len(input), iter_len):
        last_num = input[-1]
        reversed = input[::-1]

        try:
            print("Attempting to find %d" % last_num)
            last_index = reversed[1:].index(last_num) + 1
            print("Had to look back %d (len = %d)" % (last_index, len(input)))
            
            input.append(last_index)
        except ValueError as e: 
            print(e)
            input.append(0)
        
        print(input)

    return input

# Part 1
print("Part 1 = %d" % part_1([0,3,6])[-1])
# print("Part 1 = %d" % part_1([1,3,2])[-1])
# print("Part 1 = %d" % part_1([2,1,3])[-1])
# print("Part 1 = %d" % part_1([1,2,3])[-1])
# print("Part 1 = %d" % part_1([2,3,1])[-1])
# print("Part 1 = %d" % part_1([3,2,1])[-1])
# print("Part 1 = %d" % part_1([3,1,2])[-1])
# print("Part 1 = %d" % part_1([14,8,16,0,1,17])[-1])

# Part 2
# print("Part 2 = %d" % part_1([2,1,3], 30000000)[-1])
# print("Part 2 = %d" % part_1([1,2,3], 30000000)[-1])
# print("Part 2 = %d" % part_1([2,3,1], 30000000)[-1])
# print("Part 2 = %d" % part_1([3,2,1], 30000000)[-1])
# print("Part 2 = %d" % part_1([3,1,2], 30000000)[-1])
# print("Part 2 = %d" % part_1([14,8,16,0,1,17], 30000000)[-1])
