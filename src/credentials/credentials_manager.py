from dataclasses import dataclass
from src.validation.validation_checks import *
from src.logger import log

import json

config_dict = {}

def get_configs():
    
    config_path = "./src/config/credentials.json"

    with open(config_path, "r") as file:
        config_json = json.load(file)

    log.log("INFO", "Credentials manager configs loaded successfully")
    
    return config_json

@dataclass
class UserCredentials:
    """
    This class handles the credentials for a user, including their department and title.
    
    Methods:

    id(), first_name(), last_name(), location(), department(), title(): Will return the respective info field.

    name(): Will return the user's first and last name.

    is_manager(): Will return True if the user's title is "Manager", False otherwise.

    validate(): Checks each of the user info fields to ensure its validity. Will throw an exception if any are invalid.
    """

    _id: int
    _first_name: str
    _last_name: str
    _location: str
    _department: str
    _title: str

    def validate(self):
        """Checks all of the information entered for a user for validity. Will return an error if any of the fields are too long, too short, or have invalid characters."""
        global config_dict
        if len(config_dict.keys()) == 0:
            config_dict = get_configs()
            
        _field_name = ""
        try:
            _field_name = "First name"
            check_data_type(self._first_name, str, "a string")
            self._first_name = self._first_name.strip()
            check_field_size(self._first_name, config_dict["FIRST_NAME_MAX_SIZE"], config_dict["FIRST_NAME_MIN_SIZE"])
            is_alpha_or_hyphen(self._first_name)

            _field_name = "Last name"
            check_data_type(self._last_name, str, "a string")
            self._last_name = self._last_name.strip()
            check_field_size(self._last_name, config_dict["LAST_NAME_MAX_SIZE"], config_dict["LAST_NAME_MIN_SIZE"])
            is_alpha_or_hyphen(self._last_name)

            _field_name = "Employee ID number"
            check_data_type(self._id, int, "an int")
            is_positive(self._id)

            _field_name = "Location"
            check_data_type(self._location, str, "a string")
            self._location = self._location.strip()
            list_check(self._location, config_dict["LOCATIONS_LIST"])

            _field_name = "Department"
            check_data_type(self._department, str, "a string")
            self._department = self._department.strip()
            list_check(self._department, config_dict["DEPARTMENTS_LIST"])

            _field_name = "Job title"
            check_data_type(self._title, str, "a string")
            self._title = self._title.strip()
            list_check(self._title, config_dict["TITLES_LIST"])


        except Exception as e:
            error_msg = _field_name + " " + e.args[0]
            log.log("WARNING", f"Credentials validation failed for {self.name()}: {error_msg}")
            raise Exception(error_msg)
    
    def name(self):
        return f"{self._first_name} {self._last_name}"
    
    def first_name(self):
        return self._first_name
    
    def last_name(self):
        return self._last_name
    
    def employee_id(self):
        return self._id
    
    def location(self):
        return self._location
    
    def department(self):
        return self._department
    
    def title(self):
        return self._title
    
    def is_manager(self):
        return self._title == "Manager"
    
