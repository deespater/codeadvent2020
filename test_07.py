import re

from utils import (
    read_file_into_list,
    validate_result,
)


# BAG_REGEXP = r'\w+ \w+ bags contain'
# INNER_BAG_REGEXP = r'\s\d\s\w+\s\w+\sbag(s?)(,|\.)'
# NO_INNER_BAG_REGEXP = r'\sno other bags\.'
# REGEXP = f'^{BAG_REGEXP}((({INNER_BAG_REGEXP})+)|({NO_INNER_BAG_REGEXP}))$'

BAG_REGEXP = r'(?P<bag_color>\w+\s\w+) bags contain'
INNER_BAG_REGEXP = r'\s(?P<inner_bag_count>\d)\s(?P<inner_bag_color>\w+\s\w+)\sbag(s?)(,|\.)'
NO_INNER_BAG_REGEXP = r'\sno other bags\.'
REGEXP = f'^{BAG_REGEXP}(?P<inner_bags>(({INNER_BAG_REGEXP})+)|({NO_INNER_BAG_REGEXP}))$'


class TestDay06:
    @classmethod
    def setup_class(cls):
        input_data = read_file_into_list('./inputs/07.txt')
        cls.rule_regexp = re.compile(REGEXP)

        rules = {}
        for rule_line in input_data:
            rules.update(cls.parse_rule_line(rule_line))

        cls.rules = rules
        # print(cls.rules)

    @classmethod
    def parse_rule_line(cls, rule_line):
        matches = cls.rule_regexp.match(rule_line)
        match_groups = matches.groupdict()

        inner_rules = {}

        inner_bag_matches = re.findall(INNER_BAG_REGEXP, match_groups['inner_bags'])
        for inner_bag_match in inner_bag_matches:
            inner_rules.update({
                inner_bag_match[1]: inner_bag_match[0]
            })

        return {
            match_groups['bag_color']: inner_rules
        }


    def find_bag(self, color_to_find, color_list = None, root_color = None):
        found_colors = []

        color_list = list(color_list or self.rules.keys())
        for color in color_list:
            nested_colors_list = list(self.rules[color].keys())

            if not nested_colors_list:
                continue

            for nested_color in nested_colors_list:
                if color_to_find == nested_color:
                    found_colors.append(root_color or color)
                else:
                    inner_colors = self.find_bag(color_to_find, [nested_color], root_color or color)
                    found_colors += inner_colors

        return list(set(found_colors))

    @validate_result(164)
    def test_challenge_01(self):
        bag_to_carry = 'shiny gold'

        needed_bags = self.find_bag(bag_to_carry)
        return len(needed_bags)
