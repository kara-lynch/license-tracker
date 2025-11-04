

from abc import ABC
from abc import abstractmethod
import json
from src.validation import validation_checks
from src.logger import log
from pydoc import locate

class Request(ABC):
    """This class manages the sanitization and storage of user defined request data.
    An abstract class is used for validation, which is implemented in request-type specific subclasses.

    :peram user_req_json: json string object from user, to be validated and turned into a dictionary
    :type user_req_json: str
    """

    lic_data:dict
    clean_data:dict = {}
    config_dict = {}

    def __init__(self, user_req_json):
        """constructor"""
        log.log("INFO", "starting request data validation")
        self.lic_data = json.loads(user_req_json)
        self.config_dict = self.get_configs()
        self.validate_data()

    def validate_field(self, field_key):
        """validates request fields based on config file values
        :param field_key: key to use for accessing and submitting data to dictionaries
        :type field_key: str
        :raises valueError: raises value error if field is found to be invalid
        """
        if self.field_exists(field_key):
            validation_checks.check_data_type(self.lic_data[field_key], locate(self.config_dict[field_key]["type"]))
            validation_checks.check_field_size(str(self.lic_data[field_key]), self.config_dict[field_key]["max_size"], self.config_dict[field_key]["min_size"])
            self.clean_data[field_key] = self.lic_data[field_key]
            log.log("INFO", "license {field_key} validated")

    def get_configs(self):
        """gets business rules for each field from config and returns them as a dictionary
        :return: dictionary form of request_fields.json config file
        :rtype: dictionary
        """
    
        config_path = "./src/config/request_fields.json"

        with open(config_path, "r") as file:
            config_json = json.load(file)

        log.log("INFO", "User request manager configs loaded successfully")
    
        return config_json
    
    def field_exists(self, field_name):
        """checks to confirm if a field exists in the initial user request
        :param field_name: the key used to access the field being verified in the request data dictionary
        :type field_name: str
        :rtype: boolean
        """
        if self.lic_data.get(field_name) == None:
            return False
        else:
            return True
        
    def has_cost(self):
        """checks to confirm if the cost field exists in clean data; used as a flag in the database api layer
        :rtype: boolean
        """
        if self.clean_data.get(self.config_dict["cost"]["key"]) == None:
            return False
        else:
            return True
    
    def has_expiration(self):
        """checks to confirm if the date of expiration field exists in clean data; used as a flag in the database api layer
        :rtype: boolean
        """
        if self.clean_data.get(self.config_dict["date_of_expiration"]["key"]) == None:
            return False
        else:
            return True
    
    def has_restrictions(self):
        """checks to confirm if the restrictions field exists in clean data; used as a flag in the database api layer
        :rtype: boolean
        """
        if self.clean_data.get(self.config_dict["restrictions"]["key"]) == None:
            return False
        else:
            return True

    def get_clean_data_dict(self):
        """getter for clean data dictionary, for external use
        :return: dictionary of validated data
        :rtype: dictionary
        """
        if self.clean_data == None:
            self.clean_data = {}
        return self.clean_data
    
    def get_clean_data_json(self):
        """getter for clean data, converted to json formatted string, for external use
        :return: str of json formatted validated data
        :rtype: str
        """
        return json.dumps(self.get_clean_data_dict())


    @abstractmethod 
    def validate_data(self):
        """abstract method to force emplementation of data validation by request specific subclasses"""
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
                    self.validate_field(self.lic_data[self.config_dict["curr"]["key"]])
                    self.validate_field(self.lic_data[self.config_dict["cost"]["key"]])
                    if self.field_exists(self.config_dict["period"]["key"]):
                        self.validate_field(self.lic_data[self.config_dict["period"]["key"]])
                    if self.field_exists(self.config_dict["date_of_renewal"]["key"]):
                        self.validate_field(self.lic_data[self.config_dict["date_of_renewal"]["key"]])
                else:
                    raise ValueError("cost must have currency")
            elif self.field_exists(self.config_dict["curr"]["key"]) or self.field_exists(self.config_dict["date_of_renewal"]["key"]) or self.field_exists(self.config_dict["period"]["key"]):
                raise ValueError("cost based field entered but not cost")
            if self.field_exists(self.config_dict["date_of_expiration"]["key"]):
                self.validate_field(self.lic_data[self.config_dict["date_of_expiration"]["key"]])
            if self.field_exists(self.config_dict["restrictions"]["key"]):
                self.validate_field(self.lic_data[self.config_dict["restrictions"]["key"]])


class DelLicReq(Request):
    def validate_data(self):
        log.log("INFO", "delete license request begin validation")
        if not self.field_exists(self.config_dict["licenseID"]["key"]):
            log.log("ERROR", "license ID missing, required for delete; terminating program")
            raise ValueError("Missing license ID")
        else:
            self.validate_field(self.lic_data[self.config_dict["licenseID"]["key"]])

class QueryLicReq(Request):
    def validate_data(self):
        log.log("INFO", "query license request begin validation")
        if (len(self.lic_data.keys()) > 1):
             log.log("ERROR", "multiple fields given in query request, not supported; program terminated")
             raise ValueError("Query by multiple fields not currently supported")
        else:
            if self.field_exists(self.config_dict["name"]["key"]):
                self.validate_field(self.lic_data[self.config_dict["name"]["key"]])
            if self.field_exists(self.config_dict["type"]["key"]):
                self.validate_field(self.lic_data[self.config_dict["type"]["key"]])
            if self.field_exists(self.config_dict["licenseID"]["key"]):
                self.validate_field(self.lic_data[self.config_dict["licenseID"]["key"]])        


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