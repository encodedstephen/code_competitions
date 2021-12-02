import re

def first_star ():
    with open('./input.txt') as f:
        
        num_valid = 0

        for line in f: 
            lower, upper, char, passwd = re.match('(\d+)-(\d+) (.): (.*)', line).groups()

            cnt = passwd.count(char)
            if cnt >= int(lower) and cnt <= int(upper):
                num_valid += 1
        
        print(num_valid)

def second_start(): 

    with open('./input.txt') as f:
        
        num_valid = 0

        for line in f: 
            lower, upper, char, passwd = re.match('(\d+)-(\d+) (.): (.*)', line).groups()

            lower_match = passwd[int(lower) - 1] == char
            upper_match = passwd[int(upper) - 1] == char

            if lower_match + upper_match == 1:
                num_valid += 1
        
        print(num_valid)
    

second_start()
