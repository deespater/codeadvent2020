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


    def execute_instructions(self, instructions):
        accumulator = 0
        instruction_index = 0
        executed_instructions_indexes = []
        recursion_detected = False

        while instruction_index not in executed_instructions_indexes:
            try:
                operator, argument = instructions[instruction_index]
            except IndexError:
                return accumulator, False

            executed_instructions_indexes.append(instruction_index)

            if operator == 'acc':
                accumulator += argument
            elif operator == 'jmp':
                instruction_index += (argument - 1)

            instruction_index += 1
        else:
            recursion_detected = True

        return accumulator, recursion_detected


    @validate_result(1262)
    def test_challenge_01(self):
        result, loop_was_detected = self.execute_instructions(self.instructions)
        assert loop_was_detected
        return result


    def swap_instruction(self, start_index = 0):
        instructions = self.instructions.copy()
        for index in range(start_index, len(instructions)):
            operation, argument = instructions[index]
            if operation == 'jmp' or operation == 'nop':
                swapped_operation = 'jmp' if operation == 'nop' else 'nop'
                instructions[index] = (swapped_operation, argument)
                return instructions, index + 1

        raise Exception('No more swaps available')


    @validate_result(1643)
    def test_challenge_02(self):
        # First run
        result, loop_was_detected = self.execute_instructions(self.instructions)
        swapped_index = 0

        while loop_was_detected:
            modified_instructions, swapped_index = self.swap_instruction(swapped_index)
            result, loop_was_detected = self.execute_instructions(modified_instructions)
        else:
            return result
