"""This module includes a series of checks you can run to validate data. All of them should be run in a try-except block as they will throw exceptions if any of them fail."""

def check_data_type(data_to_check, input_type, type_name: str=None):
    """
    Checks if the input is of the specified type. Will return an exception if it isn't.
    
    Input 1: The data to run a check on.
    Input 2: The data type to check input 1 against.
    Input 3 (optional): A short description of input 2, such as "a string" or "an int", to be included in the error message if the check fails.
    """
    if type(data_to_check) != input_type:
        if type_name == None:
            raise TypeError("is of the incorrect type")
        else: 
            raise TypeError(f"must be {type_name}")

def check_field_size(input_str: str, max_size: int, min_size: int):
    """
    Checks if the input string is within the specified size limits. Will return an exception if it isn't.
    
    Input 1: The string to be checked.
    Input 2: The upper size limit.
    Input 3: The lower size limit.
    """
    if len(input_str) > max_size:
        raise ValueError(f"must be at most {max_size} characters long")
    if len(input_str) < min_size:
        raise ValueError(f"must be at least {min_size} characters long")

def is_alpha_or_hyphen(input_str: str):
    """
    Checks if the input consists of only letters and up to one hyphen. Will return an exception otherwise. Used to validate the name of a person.
    
    Input: The string to be checked.
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

def list_check(input_str, input_list: list):
    """
    Checks if the input object is in the input list. Will raise an exception if it isn't.
    
    Input 1: The data to be checked.
    Input 2: The list that input 1 is checked against.
    """
    if input_str not in input_list:
        raise ValueError("not found")
    
def is_positive(input_num: int):
    """
    Checks if the input number is positive. Will raise an exception if it isn't. Intended for ID numbers and other ints, but should be usable with floats as well.
    
    Input: The number to be checked.
    """
    if input_num <= 0:
        raise ValueError("cannot be zero or negative")