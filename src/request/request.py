"""
    This class manages the sanitization and storage of user defined request data.
    An abstract class is used for validation, which is implemented in request-type specific subclasses.
    Methods:
    __init__(json): calls the subclass specific validate_data function to automatically validate on instantiation.
    set_...(new_field): group of functions that call field specific validation and then set the class's internal variable for that field if valid.
    add_clean_data_field(new_key, new_field): takes in a value and key and maps them to the class's dictionary of clean data.
    get_clean_data_dict(): returns the object's clean data dictionary generated in validation; this is the proper way of externally accessing object data

    Request class is implemented by classes AddLicReq, DelLicReq, and QueryLicReq
"""

from abc import ABC
from abc import abstractmethod
import json
from src.validation import validation_checks
from src.logger import log
from pydoc import locate

class Request(ABC):
    
    lic_data:dict
    clean_data:dict = {}
    config_dict = {}

    def __init__(self, user_req_json):
        log.log("INFO", "starting request data validation")
        self.lic_data = json.loads(user_req_json)
        self.config_dict = self.get_configs()
        self.validate_data()

    def validate_field(self, field_key):
        if self.field_exists(field_key):
            validation_checks.check_data_type(self.lic_data[field_key], locate(self.config_dict[field_key]["type"]))
            validation_checks.check_field_size(str(self.lic_data[field_key]), self.config_dict[field_key]["max_size"], self.config_dict[field_key]["min_size"])
            self.clean_data[field_key] = self.lic_data[field_key]
            log.log("INFO", "license {field_key} validated")
        else:
            log.log("DEBUG", "license {field_key} empty")

    def get_configs(self):
    
        config_path = "./src/config/request_fields.json"

        with open(config_path, "r") as file:
            config_json = json.load(file)

        log.log("INFO", "User request manager configs loaded successfully")
    
        return config_json
    
    def field_exists(self, field_name):
        if self.lic_data.get(field_name) == None:
            return False
        else:
            return True
        
    def has_cost(self):
        if self.clean_data.get(self.config_dict["cost"]["key"]) == None:
            return False
        else:
            return True
    
    def has_expiration(self):
        if self.clean_data.get(self.config_dict["date_of_expiration"]["key"]) == None:
            return False
        else:
            return True
    
    def has_restrictions(self):
        if self.clean_data.get(self.config_dict["restrictions"]["key"]) == None:
            return False
        else:
            return True

    def get_clean_data_dict(self):
        if self.clean_data == None:
            self.clean_data = {}
        return self.clean_data
    
    def get_clean_data_json(self):
        return json.dumps(self.get_clean_data_dict())


    @abstractmethod
    def validate_data(self):
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
class AssignLicense(Request):
    def validate_data(self):
        log.log("INFO", "assign license request begin validation")
        if not self.field_exists(self.config_dict["licenseID"]["key"]) or (not self.field_exists(self.lic_employee_id_key) and not self.field_exists(self.lic_computer_id_key)):
            log.log("ERROR", "one or more fields required for assigning are missing; terminating program")
            raise ValueError("Missing one or more required field")
        elif self.field_exists(self.lic_employee_id_key) and self.field_exists(self.lic_computer_id_key): 
            log.log("ERROR", "attempting to assign both computer and employee simultaneously; not supported; terminating program")
            raise ValueError("Can't assign employee and computer at same time")
        else:
            self.validate_field(self.lic_data[self.config_dict["licenseID"]["key"]])
            if self.field_exists(self.lic_data[self.lic_employee_id_key]):
                self.set_lic_employee_id(self.lic_data[self.lic_employee_id_key])
            else:
                self.set_lic_computer_id(self.lic_data[self.lic_computer_id_key])
"""
"""
class UpdateLicReq(Request):
    def validate_data(self):
        log.log("INFO", "update license request begin validation")
        if not self.field_exists(self.config_dict["licenseID"]["key"]):
            log.log("ERROR", "license ID missing, required for updating; terminating program")
            raise ValueError("Missing license ID")
        else:
            if self.field_exists(self.config_dict["name"]["key"]):
                self.validate_field(self.lic_data[self.config_dict["name"]["key"]])
            if self.field_exists(self.config_dict["ver"]["key"]):
                self.validate_field(self.lic_data[self.config_dict["ver"]["key"]])
            if self.field_exists(self.config_dict["type"]["key"]):
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
"""


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