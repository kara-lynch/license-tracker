def check_data_type(data_to_check, input_type, type_name: str):
    """Checks if the input is of the specified type. Will return an exception if it isn't."""
    if type(data_to_check) != input_type:
        raise TypeError(f"must be {type_name}")

def check_field_size(input_str: str, max_size: int, min_size: int):
    """Checks if the input is within the specified size limits. Will return an exception if it isn't."""
    if len(input_str) > max_size:
        raise ValueError(f"must be at most {max_size} characters long")
    if len(input_str) < min_size:
        raise ValueError(f"must be at least {min_size} characters long")

def is_alpha_or_hyphen(input_str: str):
    """Checks if the input consists of only letters and up to one hyphen. Will return an exception otherwise."""
    if input_str.isalpha():
        return
    hyphen = False
    for char in input_str:
        if char == "-" and hyphen:
            raise ValueError("must contain only letters, spaces, and up to one hyphen")
        elif char == "-" and not hyphen:
            hyphen = True
            continue
        elif char == " ":
            continue
        elif not char.isalpha():
            raise ValueError("must contain only letters, spaces, and up to one hyphen")

def list_check(input_str: str, input_list: list):
    """Checks if the input object is in the input list. Will raise an exception if it isn't."""
    if input_str not in input_list:
        raise ValueError("not found")
    
def check_id_number(input_int: int):
    if input_int <= 0:
        raise ValueError("cannot be zero or negative")