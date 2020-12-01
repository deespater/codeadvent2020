def read_file_into_list(file_path):
    with open (file_path, 'r') as file_reader:
        file_lines = file_reader.readlines()
    file_lines = [line.strip() for line in file_lines]

    return file_lines

def cast_list_to_integer(input_list):
    return [int(line) for line in input_list]

def validate_result(expected_result):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            assert result == expected_result
        return wrapper
    return decorator
