import re

from utils import (
    read_file_into_list,
    validate_result,
)


class TestDay08:
    @classmethod
    def setup_class(cls):
        input_data = read_file_into_list('./inputs/08.txt')

        instructions = []

        for instruction in input_data:
            operator, argument = (instruction.split(' '))
            instructions.append((operator, int(argument)))

        cls.instructions = instructions

    @validate_result(1262)
    def test_challenge_01(self):
        accumulator = 0
        instruction_index = 0
        executed_instructions = set()

        while instruction_index not in executed_instructions:
            operator, argument = self.instructions[instruction_index]
            executed_instructions.add(instruction_index)

            if operator == 'acc':
                accumulator += argument
            elif operator == 'jmp':
                instruction_index += (argument - 1)

            instruction_index += 1

        return accumulator
