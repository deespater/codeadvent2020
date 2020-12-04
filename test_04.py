import re
from functools import reduce

from utils import (
    read_file_into_list,
    validate_result,
)

class TestDay04:
    @classmethod
    def setup_class(cls):
        input_data = read_file_into_list('./inputs/04.txt')

        passports = []
        current_passport = {}
        for line in input_data:
            if line == '':
                passports.append(current_passport)
                current_passport = {}
            else:
                passport_data = cls.parse_passport_data(line)
                current_passport.update(**passport_data)

        passports.append(current_passport)
        cls.passports = passports

    @classmethod
    def parse_passport_data(cls, line):
        passport_data = {}
        for entry in line.split(' '):
            key, value = entry.split(':')
            passport_data[key] = value

        return passport_data

    def validate_passport_fields_set(self, passport_data):
        required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        passport_fields = passport_data.keys()

        return set(passport_fields) & set(required_fields) == set(required_fields)

    def validate_range(self, value, min_value, max_value):
        value = int(value)
        if not(min_value <= value and max_value >= value):
            raise Exception('Invalid')

    def validate_regexp(self, value, regexp):
        if not re.match(regexp, value):
            raise Exception('Invalid')

    def validate_list(self, value, values_list):
        if not value in values_list:
            raise Exception('Invalid')


    # @TODO: Probably JSON schema validation would be more elegant
    def validate_passport_data(self, passport_data):
        try:
            self.validate_range(passport_data['byr'], 1920, 2002)
            self.validate_range(passport_data['iyr'], 2010, 2020)
            self.validate_range(passport_data['eyr'], 2020, 2030)

            # hgt
            hgt = passport_data['hgt'][0:-2]
            hgt_measurment = passport_data['hgt'][-2:]
            if hgt_measurment == 'in':
                self.validate_range(hgt, 59, 76)
            elif hgt_measurment == 'cm':
                self.validate_range(hgt, 150, 193)
            else:
                raise Exception('Invalid')

            # hcl
            hcl = passport_data['hcl']
            self.validate_regexp(hcl, r'#([a-f]|[0-9]){6}')
            # ecl
            ecl = passport_data['ecl']
            self.validate_list(ecl, ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
            # pid
            pid = passport_data['pid']
            self.validate_regexp(pid, r'^[0-9]{9}$')

            return True

        except:
            return False


    @validate_result(242)
    def test_challenge_01(self):
        passports_status = [self.validate_passport_fields_set(passport) for passport in self.passports]
        return sum(passports_status)

    @validate_result(186)
    def test_challenge_02(self):
        validation_procedure = lambda passport: self.validate_passport_fields_set(passport) and self.validate_passport_data(passport)

        passports_status = [validation_procedure(passport) for passport in self.passports]
        return sum(passports_status)
