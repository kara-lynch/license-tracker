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


@dataclass(frozen=True)
class UserCredentials:
    """
    Stores information about the current user.
    
    :param _user_dict: The dict that the object will pull its information from. It must have the following keys: ``id``, ``fName``, ``lName``, ``loc``, ``dept``, and ``title``.
    :type user_dict: dict
    """
    _user_dict: dict        

    def validate(self):
        """
        Checks all of the information entered for a user for validity.

        More information on the checks can be found on the :doc:`validation` page.
        
        :raise Exception: If one of the fields is invalid or missing, or if there are too many fields provided. 
        
        """
        global config_dict
        if len(config_dict.keys()) == 0:
            config_dict = get_configs()
            
        _field_name = ""
        for field in ["fName", "lName", "id", "loc", "dept", "title"]:
            if not field in self._user_dict:
                
                log.log("WARNING", f"Credentials validation failed")
                raise KeyError(f"Key '{field}' not found in input")
            
        if len(self._user_dict) > 6:
            log.log("WARNING", "Credentials validation failed")
            raise KeyError("Too many fields provided")
        
        try:
            _field_name = "fName"
            check_data_type(self._user_dict[_field_name], str)
            check_field_size(self._user_dict[_field_name], config_dict["FIRST_NAME_MAX_SIZE"], config_dict["FIRST_NAME_MIN_SIZE"])

            _field_name = "lName"
            check_data_type(self._user_dict[_field_name], str)
            check_field_size(self._user_dict[_field_name], config_dict["LAST_NAME_MAX_SIZE"], config_dict["LAST_NAME_MIN_SIZE"])

            _field_name = "id"
            check_data_type(self._user_dict[_field_name], int)
            is_positive(self._user_dict[_field_name])

            _field_name = "loc"
            check_data_type(self._user_dict[_field_name], str)
            list_check(self._user_dict[_field_name], config_dict["LOCATIONS_LIST"])

            _field_name = "dept"
            check_data_type(self._user_dict[_field_name], str)
            list_check(self._user_dict[_field_name], config_dict["DEPARTMENTS_LIST"])

            _field_name = "title"
            check_data_type(self._user_dict[_field_name], str)
            list_check(self._user_dict[_field_name], config_dict["TITLES_LIST"])

            log.log("INFO", f"Credentials validation succeeded for {self.name()}")


        except Exception as e:
            error_msg = _field_name + " " + e.args[0]
            #print(f"Credentials validation failed for {self.name()}: {error_msg}")
            log.log("WARNING", f"Credentials validation failed")
            raise Exception(error_msg)
    
    def name(self):
        """
        :return: The user's first and last name, e.g. "Kara Lynch".
        :rtype: str
        """
        return f"{self._user_dict['fName']} {self._user_dict['lName']}"
    
    def first_name(self):
        """
        :return: The user's first name, e.g. "Kara".
        :rtype: str
        """
        return self._user_dict["fName"]
    
    def last_name(self):
        """
        :return: The user's last name, e.g. "Lynch".
        :rtype: str
        """
        return self._user_dict["lName"]
    
    def employee_id(self):
        """
        :return: The user's employee ID number, e.g. 263.
        :rtype: int
        """
        return self._user_dict["id"]
    
    def location(self):
        """
        :return: The user's country of residence, e.g. "United States".
        :rtype: str
        """
        return self._user_dict["loc"]
    
    def department(self):
        """
        :return: The department the user works in, e.g. "Legal".
        :rtype: str
        """
        return self._user_dict["dept"]
    
    def title(self):
        """
        :return: The user's job title, e.g. "Aide".
        :rtype: str
        """
        return self._user_dict["title"]
    
    def is_manager(self):
        """
        :return: True if the user is a manager, False otherwise.
        :rtype: bool
        """
        return self._user_dict["title"] == "Manager"
    
    def has_license_auth(self):
        """
        :return: True if the user is a manager of IT or Legal (i.e. the user has the authority to edit license records), False otherwise.
        :rtype: bool
        """
        return (self._user_dict["title"] == "Manager" and self._user_dict["dept"] in ["Legal", "Information Technology"])
    
