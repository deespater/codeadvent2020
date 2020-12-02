def read_file_into_list(file_path, cast_to_number=False):
    with open (file_path, 'r') as file_reader:
        file_lines = file_reader.readlines()
    file_lines = [line.strip() for line in file_lines]

    if cast_to_number:
        file_lines = [int(line) for line in file_lines]

    return file_lines

def validate_result(expected_result):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            assert result == expected_result
        return wrapper
    return decorator
