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

    def parse_input_line(self, input_line):
        parsed_data = self.regexpr.match(input_line)
        rule, letter, password = parsed_data.groups()
        rule = rule.split('-')
        return (rule, letter, password)

    def is_line_valid_v1(self, input_line):
        rule, rule_letter, password = self.parse_input_line(input_line)

        letters_count = len([letter for letter in password if letter == rule_letter])
        return letters_count >= int(rule[0]) and letters_count <= int(rule[1])

    @validate_result(546)
    def test_challenge_01(self):
        valid_lines = [line for line in self.input_data if self.is_line_valid_v1(line)]

        return len(valid_lines)
