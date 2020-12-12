from functools import reduce

from utils import (
    read_file_into_list,
    validate_result,
)

class TestDay06:
    @classmethod
    def setup_class(cls):
        input_data = read_file_into_list('./inputs/06.txt')

        groups = []
        current_group = []

        for line in input_data:
            if line == '':
                groups.append(current_group)
                current_group = []
            else:
                current_group.append(list(line))

        groups.append(current_group)
        cls.groups = groups

    @validate_result(6249)
    def test_challenge_01(self):
        group_summ = 0
        for group in self.groups:
            answers = [item for sublist in group for item in sublist]
            group_summ += len(set(answers))
        return group_summ

    @validate_result(3103)
    def test_challenge_02(self):
        group_summ = 0
        for group in self.groups:
            answers = reduce(lambda a, all: set(a) & set(all), group)
            group_summ += len(answers)
        return group_summ
