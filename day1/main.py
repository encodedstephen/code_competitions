

def first_star ():
    with open('./input.txt') as f:
        data = [int(num) for num in f.read().split('\n') if num.isdigit()]

        for num in data: 
            opposite = 2020 - num
            if opposite in data:
                return ((num, opposite), opposite * num)

def second_start(): 
    with open('./input.txt') as f:
        data = [int(num) for num in f.read().split('\n') if num.isdigit()]


        remainder = [2020 - d for d in data]

        for idx1, remain in enumerate(remainder): 
            orig = data[idx1]

            for idx2, num in enumerate(data): 
                if idx1 == idx2:
                    continue

                opposite = remain - num
                if opposite in data:
                    return ((orig, num, opposite), orig * num * opposite)
