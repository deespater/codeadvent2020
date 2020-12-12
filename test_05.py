from utils import (
    read_file_into_list,
    validate_result,
)

class TestDay05:
    ROWS_MAX = 127
    COLS_MAX = 7

    @classmethod
    def setup_class(cls):
        cls.input_data = read_file_into_list('./inputs/05.txt')

    def follow_sequence(self, code, max_number):
        full_range = [0, max_number]

        for step in code:
            half = (full_range[1] - full_range[0]) // 2
            if step == 'B' or step == 'R':
                full_range[0] = full_range[1] - half
            elif step == 'F' or step == 'L':
                full_range[1] = full_range[0] + half

        assert full_range[0] == full_range[1]
        return full_range[0]

    def parse_ticket_code(self, code):
        rows_code = code[0:7]
        cols_code = code[7:]

        row = self.follow_sequence(rows_code, self.ROWS_MAX)
        col = self.follow_sequence(cols_code, self.COLS_MAX)

        return row * (self.COLS_MAX + 1) + col

    def find_missed_spot(self, seats):
        seats_amount = len(seats)

        for index, seat in enumerate(seats):
            if index == 0 or index > seats_amount - 1:
                continue

            if (seats[index - 1] + 1) == seat and (seats[index + 1] - 1) == seat:
                continue
            else:
                return seat + 1

            raise Exception('Error')


    @validate_result(842)
    def test_challenge_01(self):
        highest_set_number = 0

        for seat_code in self.input_data:
            seat_number = self.parse_ticket_code(seat_code)
            if highest_set_number < seat_number:
                highest_set_number = seat_number

        return highest_set_number

    @validate_result(617)
    def test_challenge_02(self):
        sold_tickets_seats = [self.parse_ticket_code(code) for code in self.input_data]
        sold_tickets_seats.sort()

        return self.find_missed_spot(sold_tickets_seats)
