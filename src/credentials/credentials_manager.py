from dataclasses import dataclass
from src.validation.validation_checks import *

FIRST_NAME_MAX_SIZE = 32
FIRST_NAME_MIN_SIZE = 2
LAST_NAME_MAX_SIZE = 32
LAST_NAME_MIN_SIZE = 2
LOCATIONS_LIST = ["United States", "Japan", "Germany", "Brazil", "South Africa"]
DEPARTMENTS_LIST = ["Sales", "Information Technology", "Legal", "HR"]
TITLES_LIST = ["Manager", "Aide", "Developer", "Sales Agent"]

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
        _field_name = ""
        try:
            _field_name = "First name"
            check_data_type(self._first_name, str, "a string")
            self._first_name = self._first_name.strip()
            check_field_size(self._first_name, FIRST_NAME_MAX_SIZE, FIRST_NAME_MIN_SIZE)
            is_alpha_or_hyphen(self._first_name)

            _field_name = "Last name"
            check_data_type(self._last_name, str, "a string")
            self._last_name = self._last_name.strip()
            check_field_size(self._last_name, LAST_NAME_MAX_SIZE, LAST_NAME_MIN_SIZE)
            is_alpha_or_hyphen(self._last_name)

            _field_name = "Employee ID number"
            check_data_type(self._id, int, "an int")
            is_positive(self._id)

            _field_name = "Location"
            check_data_type(self._location, str, "a string")
            self._location = self._location.strip()
            list_check(self._location, LOCATIONS_LIST)

            _field_name = "Department"
            check_data_type(self._department, str, "a string")
            self._department = self._department.strip()
            list_check(self._department, DEPARTMENTS_LIST)

            _field_name = "Job title"
            check_data_type(self._title, str, "a string")
            self._title = self._title.strip()
            list_check(self._title, TITLES_LIST)


        except Exception as e:
            raise Exception(_field_name + " " + e.args[0])
    
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
    
