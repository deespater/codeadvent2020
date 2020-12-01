from utils import (
    cast_list_to_integer,
    read_file_into_list,
    validate_result,
)

class TestDay01:
    @classmethod
    def setup_class(cls):
        cls.input_data = read_file_into_list('./inputs/01.txt')
        cls.input_data = cast_list_to_integer(cls.input_data)

    @validate_result(918339)
    def test_challenge_01(self):
        for i, first_number in enumerate(self.input_data):
            for j, second_number in enumerate(self.input_data):
                if i == j:
                    continue

                if first_number + second_number == 2020:
                    return first_number * second_number



    @validate_result(23869440)
    def test_challenge_02(self):
        for i, first_number in enumerate(self.input_data):
            for j, second_number in enumerate(self.input_data):
                for k, third_number in enumerate(self.input_data):
                    if i == j == k:
                        continue

                    if first_number + second_number + third_number == 2020:
                        return first_number * second_number * third_number
