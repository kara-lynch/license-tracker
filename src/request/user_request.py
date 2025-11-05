

from abc import ABC
from abc import abstractmethod
import json
from src.validation import validation_checks
from src.logger import log
from pydoc import locate

class Request(ABC):
    """
    This class manages the sanitization and storage of user defined request data.
    An abstract class is used for validation, which is implemented in request type-specific subclasses.

    :param user_req_json: JSON string object from user, to be validated and turned into a dictionary.
    :type user_req_json: str
    """

    def __init__(self, user_req_json):
        """constructor"""
        log.log("INFO", "starting request data validation")
        self.lic_data:dict = {}
        self.clean_data:dict = {}
        self.config_dict = {}
        self.lic_data = json.loads(user_req_json)
        self.config_dict = self.get_configs()
        self.validate_data()

    def validate_field(self, field_key):
        """
        Validates request fields based on config file values.

        :param field_key: The name of the field to validate.
        :type field_key: str
        :raises ValueError: If the field is found to be invalid.
        """
        if self.field_exists(field_key):
            validation_checks.check_data_type(self.lic_data[field_key], locate(self.config_dict[field_key]["type"]))
            validation_checks.check_field_size(str(self.lic_data[field_key]), self.config_dict[field_key]["max_size"], self.config_dict[field_key]["min_size"])
            if locate(self.config_dict[field_key]["type"]) == int or locate(self.config_dict[field_key]["type"]) == float:
                validation_checks.is_positive(self.lic_data[field_key])
            self.clean_data[field_key] = self.lic_data[field_key]
            log.log("INFO", f"license {field_key} validated")

    def get_configs(self):
        """
        Gets business rules for each field from config and returns them as a dictionary.

        :return: Contents of the request_fields.json config file formatted as a dictionary.
        :rtype: dict
        """
    
        config_path = "./src/config/request_fields.json"

        with open(config_path, "r") as file:
            config_json = json.load(file)

        log.log("INFO", "User request manager configs loaded successfully")
    
        return config_json
    
    def field_exists(self, field_name):
        """
        Checks to confirm if a field exists in the initial user request.

        :param field_name: The name of the field being checked.
        :type field_name: str
        :rtype: boolean
        """
        if self.lic_data.get(field_name) == None:
            return False
        else:
            return True
        
    def has_cost(self):
        """
        Checks to confirm if the cost field exists in clean data. Used as a flag in the database API layer.

        :rtype: boolean
        """
        if self.clean_data.get(self.config_dict["cost"]["key"]) == None:
            return False
        else:
            return True
    
    def has_expiration(self):
        """
        Checks to confirm if the date of expiration field exists in clean data. Used as a flag in the database API layer.

        :rtype: boolean
        """
        if self.clean_data.get(self.config_dict["expiration_date"]["key"]) == None:
            return False
        else:
            return True
    
    def has_restrictions(self):
        """
        Checks to confirm if the restrictions field exists in clean data. Used as a flag in the database API layer.

        :rtype: boolean
        """
        if self.clean_data.get(self.config_dict["restrictions"]["key"]) == None:
            return False
        else:
            return True

    def get_clean_data_dict(self):
        """
        Getter for clean data formatted as a dict.

        :return: Dictionary of validated data.
        :rtype: dict
        """
        if self.clean_data == None:
            self.clean_data = {}
        return self.clean_data
    
    def get_clean_data_json(self):
        """
        Getter method for clean data converted to a JSON-formatted string.

        :return: Validated data as a JSON string object.
        :rtype: str
        """
        return json.dumps(self.get_clean_data_dict())


    @abstractmethod 
    def validate_data(self):
        """Abstract method to force implementation of data validation by request specific subclasses."""
        pass


class AddLicReq(Request):
    def validate_data(self):
        log.log("INFO", "add license request begin validation")
        if not self.field_exists(self.config_dict["name"]["key"]) or not self.field_exists(self.config_dict["ver"]["key"]) or not self.field_exists(self.config_dict["type"]["key"]):
            log.log("ERROR", "one or more components required for adding are missing; terminating program")
            raise ValueError("Missing one or more required field")
        else:
            self.validate_field(self.config_dict["name"]["key"])
            self.validate_field(self.config_dict["ver"]["key"])
            self.validate_field(self.config_dict["type"]["key"])
            if self.field_exists(self.config_dict["cost"]["key"]):
                if self.field_exists(self.config_dict["curr"]["key"]):
                    self.validate_field(self.config_dict["curr"]["key"])
                    self.validate_field(self.config_dict["cost"]["key"])
                    if self.field_exists(self.config_dict["period"]["key"]):
                        self.validate_field(self.config_dict["period"]["key"])
                    if self.field_exists(self.config_dict["date_of_renewal"]["key"]):
                        self.validate_field(self.config_dict["date_of_renewal"]["key"])
                else:
                    raise ValueError("cost must have currency")
            elif self.field_exists(self.config_dict["curr"]["key"]) or self.field_exists(self.config_dict["date_of_renewal"]["key"]) or self.field_exists(self.config_dict["period"]["key"]):
                raise ValueError("cost based field entered but not cost")
            if self.field_exists(self.config_dict["expiration_date"]["key"]):
                self.validate_field(self.config_dict["expiration_date"]["key"])
            if self.field_exists(self.config_dict["restrictions"]["key"]):
                self.validate_field(self.config_dict["restrictions"]["key"])


class DelLicReq(Request):
    def validate_data(self):
        log.log("INFO", "delete license request begin validation")
        if not self.field_exists(self.config_dict["licenseID"]["key"]):
            log.log("ERROR", "license ID missing, required for delete; terminating program")
            raise ValueError("Missing license ID")
        else:
            self.validate_field(self.config_dict["licenseID"]["key"])

class QueryLicReq(Request):
    def validate_data(self):
        log.log("INFO", "query license request begin validation")
        if (len(self.lic_data.keys()) > 1):
             log.log("ERROR", "multiple fields given in query request, not supported; program terminated")
             raise ValueError("Query by multiple fields not currently supported")
        else:
            if self.field_exists(self.config_dict["name"]["key"]):
                self.validate_field(self.config_dict["name"]["key"])
            if self.field_exists(self.config_dict["type"]["key"]):
                self.validate_field(self.config_dict["type"]["key"])
            if self.field_exists(self.config_dict["licenseID"]["key"]):
                self.validate_field(self.config_dict["licenseID"]["key"])        


"""
#here for testing purposes
class QueryReturn(Request):
    def validate_data(self):
        log.log("INFO", "returned table  begin validation")
        if not self.field_exists(self.config_dict["name"]["key"]) or not self.field_exists(self.config_dict["ver"]["key"]) or not self.field_exists(self.config_dict["type"]["key"]):
            log.log("ERROR", "one or more components required for licenses are missing; terminating program")
            raise ValueError("Missing one or more required field")
        else:
            self.validate_field(self.lic_data[self.config_dict["licenseID"]["key"]])
            self.validate_field(self.lic_data[self.config_dict["name"]["key"]])
            self.validate_field(self.lic_data[self.config_dict["ver"]["key"]])
            self.validate_field(self.lic_data[self.config_dict["type"]["key"]])
            if self.field_exists(self.config_dict["cost"]["key"]):
                self.validate_field(self.lic_data[self.config_dict["cost"]["key"]])
            if self.field_exists(self.config_dict["curr"]["key"]):
                self.validate_field(self.lic_data[self.config_dict["curr"]["key"]])
            if self.field_exists(self.config_dict["period"]["key"]):
                self.validate_field(self.lic_data[self.config_dict["period"]["key"]])
            if self.field_exists(self.config_dict["date_of_renewal"]["key"]):
                self.validate_field(self.lic_data[self.config_dict["date_of_renewal"]["key"]])
            if self.field_exists(self.config_dict["date_of_expiration"]["key"]):
                self.validate_field(self.lic_data[self.config_dict["date_of_expiration"]["key"]])
            if self.field_exists(self.config_dict["restrictions"]["key"]):
                self.validate_field(self.lic_data[self.config_dict["restrictions"]["key"]])
*/
"""