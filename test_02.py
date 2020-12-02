import re

from utils import (
    read_file_into_list,
    validate_result,
)

class TestDay02:
    @classmethod
    def setup_class(cls):
        cls.input_data = read_file_into_list('./inputs/02.txt')
        cls.regexpr = re.compile(r'^(\d+-\d+)\s([a-z]):\s(\w+$)')

    def is_line_valid(self, input):
        parsed_data = self.regexpr.match(input)
        rule_range, rule_letter, password = parsed_data.groups()
        rule_range = rule_range.split('-')

        return self.is_password_valid(rule_range, rule_letter, password)

    def is_password_valid(self, rule_range, rule_letter, password):
        letters_count = len([letter for letter in password if letter == rule_letter])
        return letters_count >= int(rule_range[0]) and letters_count <= int(rule_range[1])

    @validate_result(546)
    def test_challenge_01(self):
        valid_lines = [line for line in self.input_data if self.is_line_valid(line)]

        return len(valid_lines)
