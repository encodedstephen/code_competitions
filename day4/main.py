import re


class Passport():

    def __init__(self):
        self.field_list = ['byr', 'iyr', 'eyr',
                           'hgt', 'hcl', 'ecl', 'pid', 'cid']

    def exists(self, fields: list) -> bool:
        for field in fields:
            if not hasattr(self, field):
                return False
        return True
    
    def valid(self, fields: list) -> bool:
        for field in fields:
            if not hasattr(self, field):
                return False
            
            fx_name = 'valid_'+field
            if not getattr(self, fx_name, lambda x: False)():
                return False

        return True

    def valid_byr(self): 
        val = getattr(self, 'byr', 0)
        return re.fullmatch(r'\d{4}', val) != None and int(val) >= 1920 and int(val) <= 2002

    def valid_iyr(self):
        val = getattr(self, 'iyr', 0)
        return re.fullmatch(r'\d{4}', val) != None and int(val) >= 2010 and int(val) <= 2020
    
    def valid_eyr(self):
        val = getattr(self, 'eyr', 0)
        return re.fullmatch(r'\d{4}', val) != None and int(val) >= 2020 and int(val) <= 2030

    def valid_hgt(self): 
        if not hasattr(self, 'hgt'):
            return False

        matches = re.fullmatch(r'(\d+)(cm|in)', self.hgt)
        if matches == None:
            return False

        v,t = matches.groups()
        if t == 'cm':
            return int(v) >= 150 and int(v) <= 193
        if t == 'in':
            return int(v) >= 59 and int(v) <= 76

    def valid_hcl(self):
        val = getattr(self, 'hcl', '')
        return re.fullmatch(r'#[0-9a-f]{6}', val) != None

    def valid_ecl(self):
        val = getattr(self, 'ecl', '')
        return re.fullmatch(r'(amb|blu|brn|gry|grn|hzl|oth)', val) != None

    def valid_pid(self):
        val = getattr(self, 'pid', '')
        return re.fullmatch(r'\d{9}', val) != None


    @classmethod
    def parse(cls, fields: list):
        p = cls()

        for field in fields:
            f, v = field.split(':')
            setattr(p, f, v.strip('\n'))

        return p


def first_star():

    passport_text = []
    num_valid = 0

    def parse_and_check(passport_text):
        passport = Passport.parse(passport_text)
        if passport.exists(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
            return True
        return False
            
    with open('./input.txt') as input:

        for line in input:
            if line.find(':') < 0:
                # we have finished processing a passport
                num_valid += parse_and_check(passport_text)
                passport_text = []
            else:
                for field in line.split(' '):
                    passport_text.append(field)

        if len(passport_text) != 0:
            num_valid += parse_and_check(passport_text)

        print(num_valid)

first_star()

def second_star():

    passport_text = []
    num_valid = 0

    def parse_and_check(passport_text):
        passport = Passport.parse(passport_text)
        if passport.valid(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
            return True
        return False

    with open('./input.txt') as input:

        passport_text= []
        num_valid= 0

        for line in input:
            if line.find(':') < 0:
                # we have finished processing a passport
                num_valid += parse_and_check(passport_text)
                passport_text = []
            else:
                for field in line.split(' '):
                    passport_text.append(field)

        if len(passport_text) != 0:
            num_valid += parse_and_check(passport_text)

        print(num_valid)

second_star()
