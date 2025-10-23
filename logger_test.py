from src.logger import log

config_path = "./src/config/logger.json"

# with open(config_path, "r") as file:
#     config_json = json.load(file)

# logging.config.dictConfig(config_json)

"""
Test function. Will take in a string and check that there are no colons (:) within. 
If a colon is found, log an error.
Returns true if no colons found.
"""
def validate_input(inp: str) -> bool:
    log.log("INFO", "Inside function 2.")

    for char in inp:
        if char == ":":
            log.log("ERROR", "A semicolon got through!")
            return False

    return True

"""
Function has three hardcoded strings. It will validate that none have colons, then print the ones without."""
def print_strings():
    log.log("INFO", "Inside function 1.")

    numberWithColons = 0

    str1 = "This is a test string."
    str2 = "This is a ::test string::"
    str3 = "This is NOT a test string."
    str4 = "Is this a test string?"
    str5 = "::yes::"

    strings = [str1, str2, str3, str4, str5]

    for i in range(len(strings)):
        colonFound = validate_input(strings[i])
        if not colonFound:
            log.log("WARNING", f'A colon was found in str{i+1}!')

if __name__ == "__main__":
    log.log("INFO", "Beginning test of logger module.")

    log.log("INFO", "Testing function call.")
    print_strings()

    log.log("INFO", "Ending test program.")