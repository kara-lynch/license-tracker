from dataclasses import dataclass
from validation_checks import *

FIRST_NAME_MAX_SIZE = 32
FIRST_NAME_MIN_SIZE = 2
LAST_NAME_MAX_SIZE = 32
LAST_NAME_MIN_SIZE = 2
LOCATIONS_LIST = ["United States", "Japan", "Germany", "Brazil", "South Africa"]
DEPARTMENTS_LIST = ["Sales", "Information Technology", "Legal", "HR"]
TITLES_LIST = ["Manager", "Aide", "Developer", "Sales Agent"]

@dataclass
class UserCredentials:
    id: int
    first_name: str
    last_name: str
    location: str
    department: str
    title: str

    """This class handles the credentials for a user, including their department and title."""

    def validate(self):
        """Checks all of the information entered for a user for validity. Will return an error if any of the fields are too long, too short, or have invalid characters."""
        field_name = ""
        try:
            field_name = "First name"
            check_data_type(self.first_name, str, "a string")
            self.first_name = self.first_name.strip()
            check_field_size(self.first_name, FIRST_NAME_MAX_SIZE, FIRST_NAME_MIN_SIZE)
            is_alpha_or_hyphen(self.first_name)

            field_name = "Last name"
            check_data_type(self.last_name, str, "a string")
            self.last_name = self.last_name.strip()
            check_field_size(self.last_name, LAST_NAME_MAX_SIZE, LAST_NAME_MIN_SIZE)
            is_alpha_or_hyphen(self.last_name)

            field_name = "Employee ID number"
            check_data_type(self.id, int, "an int")
            check_id_number(self.id)

            field_name = "Location"
            check_data_type(self.location, str, "a string")
            self.location = self.location.strip()
            list_check(self.location, LOCATIONS_LIST)


        except Exception as e:
            raise Exception(field_name + " " + e.args[0])
    
    def name(self):
        return f"{self.first_name} {self.last_name}"
    
def main():
    test_data = [
        (
            263,
            "Ava'); DROP TABLE Employee; --",
            "Fishbie",
            "Japan",
            "Legal",
            "Manager"
        ),
        (
            264,
            "Amélie",
            "Garçon-Beaumont",
            "France",
            "Sales",
            "Sales Agent"
        ),
        (
            265,
            "Jens",
            "van der Meer",
            "Germany",
            "Information Technology",
            "Developer"
        )
    ]
    users = []
    for test in test_data:
        new_user = UserCredentials(test[0], test[1], test[2], test[3], test[4], test[5])
        try:
            new_user.validate()
            users.append(new_user)
            print(f"{new_user.name()} added successfully")
        except Exception as e:
            print(f"Cannot add {new_user.name()}: {e.args[0]}")
    print("List of users:")
    for user in users:
        print(user.name())

main()