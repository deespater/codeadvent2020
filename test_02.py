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
        rule = [int(number) for number in rule.split('-')]
        return (rule, letter, password)

    def is_line_valid_v1(self, input_line):
        rule, rule_letter, password = self.parse_input_line(input_line)

        letters_count = len([letter for letter in password if letter == rule_letter])
        return letters_count >= rule[0] and letters_count <= rule[1]

    def is_line_valid_v2(self, input_line):
        rule, rule_letter, password = self.parse_input_line(input_line)

        first_position, second_position = rule

        first_position_correct = password[first_position - 1] == rule_letter and password[second_position - 1] != rule_letter
        second_position_correct = password[first_position - 1] != rule_letter and password[second_position - 1] == rule_letter

        return first_position_correct or second_position_correct

    @validate_result(546)
    def test_challenge_01(self):
        valid_lines = [line for line in self.input_data if self.is_line_valid_v1(line)]
        return len(valid_lines)

    @validate_result(275)
    def test_challenge_02(self):
        valid_lines = [line for line in self.input_data if self.is_line_valid_v2(line)]
        return len(valid_lines)
