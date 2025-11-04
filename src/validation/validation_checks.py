"""This module includes a series of checks you can run to validate data. All of them should be run in a try-except block as they will throw exceptions if any of them fail."""

def check_data_type(data_to_check, input_type, type_name: str=None):
    """
    Checks if the input is of the specified type. Will raise an exception if it isn't.
    
    :param data_to_check: The data to run a check on.
    :param input_type: The data type to be checked against.
    :param type_name: Deprecated. Does nothing.
    :raise TypeError: If the input is not of the specified type.
    :return: None
    """
    if type(data_to_check) != input_type:
        raise TypeError(f"must be {str(input_type)}")

def check_field_size(input_str: str, max_size: int, min_size: int):
    """
    Checks if the input string is within the specified size limits. Will raise an exception if it isn't.
    
    :param input_str: The string to be checked.
    :type input_str: str
    :param max_size: The upper size limit.
    :type max_size: int
    :param min_size: The lower size limit.
    :type min_size: int
    :raise ValueError: If the input is outside the specified range.
    :return: None
    """
    if len(input_str) > max_size:
        raise ValueError(f"must be at most {max_size} characters long")
    if len(input_str) < min_size:
        raise ValueError(f"must be at least {min_size} characters long")

def is_alpha_or_hyphen(input_str: str):
    """
    :deprecated:

    Checks if the input consists of only letters and up to one hyphen. Will return an exception otherwise. Used to validate the name of a person.
    
    :param input_str: The string to be checked.
    :type input_str: str
    :raise ValueError: If invalid characters are found in the input string.
    :return: None
    """
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

def list_check(input_obj, input_list: list):
    """
    Checks if the input object is in the input list. Will raise an exception if it isn't.

    :param input_obj: The data to be checked.
    :param input_list: The list to be checked against.
    :type input_list: list or tuple
    :raise ValueError: If the input object isn't in the input list.
    :return: None
    """
    if input_obj not in input_list:
        raise ValueError("not found")
    
def is_positive(input_num: int):
    """
    Checks if the input number is positive. Will raise an exception if it isn't. Intended for ID numbers and other ints, but should be usable with floats as well.
    
    :param input_num: The number to be checked.
    :type input_num: int or float
    """
    if input_num <= 0:
        raise ValueError("cannot be zero or negative")
    
