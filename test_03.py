from functools import reduce

from utils import (
    read_file_into_list,
    validate_result,
)

class TestDay03:
    @classmethod
    def setup_class(cls):
        input_data = read_file_into_list('./inputs/03.txt')
        cls.map_pattern = [
            list(line) for line in input_data
        ]

    def calculate_hit_trees(self, steps_right, steps_down):
        x_current, y_current = 0, 0
        x_max = len(self.map_pattern[0])
        y_max = len(self.map_pattern) - 1

        trees = 0

        while y_current < y_max:
            # Calculating new coordinates
            x_current += steps_right
            y_current += steps_down

            # If we're out of the map pattern
            if x_current >= x_max:
                x_current -= x_max

            if self.map_pattern[y_current][x_current] == '#':
                trees += 1

        return trees


    @validate_result(151)
    def test_challenge_01(self):
        return self.calculate_hit_trees(3, 1)

    @validate_result(7540141059)
    def test_challenge_02(self):
        plans = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        trees_hit = [self.calculate_hit_trees(*plan) for plan in plans]
        return reduce(lambda x, y: x * y, trees_hit)
