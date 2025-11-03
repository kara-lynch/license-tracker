from abc import ABC
from abc import abstractmethod
import json
from src.validation import validation_checks
from src.validation import validate_field
from src.logger import log

class Request(ABC):
    """
    This class manages the sanitization and storage of user defined request data.
    An abstract class is used for validation, which is implemented in request-type specific subclasses.
    Methods:
    __init__(json): calls the subclass specific validate_data function to automatically validate on instantiation.
    set_...(new_field): group of functions that call field specific validation and then set the class's internal variable for that field if valid.
    add_clean_data_field(new_key, new_field): takes in a value and key and maps them to the class's dictionary of clean data.
    get_clean_data_dict(): returns the object's clean data dictionary generated in validation; this is the proper way of externally accessing object data
    """
    lic_data:dict
    clean_data:dict = {}

    lic_name_key = "name"
    lic_version_key = "ver"
    lic_type_key = "type"
    lic_cost_key = "cost"
    lic_curr_key = "curr"
    lic_pay_period_key = "period"
    lic_date_of_renewal_key = "date_of_renewal"
    lic_date_of_expiration_key = "expiration_date"
    lic_restrictions_key = "restrictions"
    lic_id_key = "licenseID"
    lic_employee_id_key = "employeeID"
    lic_computer_id_key = "computerID"


    def __init__(self, user_req_json):
        log.log("INFO", "starting request data validation")
        self.lic_data = json.loads(user_req_json)
        self.validate_data()
    
    def field_exists(self, field_name):
        if self.lic_data.get(field_name) == None:
            return False
        else:
            return True
        
    def has_cost(self):
        if self.clean_data.get(self.lic_cost_key) == None:
            return False
        else:
            return True
    
    def has_expiration(self):
        if self.clean_data.get(self.lic_date_of_expiration_key) == None:
            return False
        else:
            return True
    
    def has_restrictions(self):
        if self.clean_data.get(self.lic_restrictions_key) == None:
            return False
        else:
            return True
    

    def set_lic_name(self, new_field):
        validate_field.validate_lic_name(str(new_field))
        self.clean_data[self.lic_name_key] = new_field
    
    def set_lic_version(self, new_field):
        validate_field.validate_lic_version(str(new_field)) 
        self.clean_data[self.lic_version_key] = new_field

    def set_lic_type(self, new_field):
        validate_field.validate_lic_type(str(new_field))
        self.clean_data[self.lic_type_key] = new_field
    
    def set_lic_cost(self, new_field):
        validate_field.validate_lic_cost(float(new_field))
        self.clean_data[self.lic_cost_key] = new_field
    
    def set_lic_curr(self, new_field):
        validate_field.validate_lic_curr(str(new_field))
        self.clean_data[self.lic_curr_key] = new_field
    
    def set_lic_pay_period(self, new_field):
        validate_field.validate_lic_pay_period(str(new_field))
        self.clean_data[self.lic_pay_period_key] = new_field
    
    def set_lic_date_of_renewal(self, new_field):
        validate_field.validate_lic_date_of_renewal(str(new_field))
        self.clean_data[self.lic_date_of_renewal_key] = new_field
    
    def set_lic_date_of_expiration(self, new_field):
        validate_field.validate_lic_date_of_expiration(str(new_field))
        self.clean_data[self.lic_date_of_expiration_key] = new_field
    
    def set_lic_restrictions(self, new_field):
        validate_field.validate_lic_restrictions(str(new_field))
        self.clean_data[self.lic_restrictions_key] = new_field
    
    def set_lic_id(self, new_field):
        validate_field.validate_lic_id(int(new_field))
        self.clean_data[self.lic_id_key] = new_field
    
    def set_lic_employee_id(self, new_field):
        validate_field.validate_lic_employee_id(int(new_field))
        self.clean_data[self.lic_employee_id_key] = new_field
    
    def set_lic_computer_id(self, new_field):
        validate_field.validate_lic_computer_id(int(new_field))
        self.clean_data[self.lic_computer_id_key] = new_field


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
        if not self.field_exists(self.lic_name_key) or not self.field_exists(self.lic_version_key) or not self.field_exists(self.lic_type_key):
            log.log("ERROR", "one or more components required for adding are missing; terminating program")
            raise ValueError("Missing one or more required field")
        else:
            self.set_lic_name(self.lic_data[self.lic_name_key])
            self.set_lic_version(self.lic_data[self.lic_version_key])
            self.set_lic_type(self.lic_data[self.lic_type_key])
            if self.field_exists(self.lic_cost_key):
                if self.field_exists(self.lic_curr_key):
                    self.set_lic_curr(self.lic_data[self.lic_curr_key])
                    self.set_lic_cost(self.lic_data[self.lic_cost_key])
                    if self.field_exists(self.lic_pay_period_key):
                        self.set_lic_pay_period(self.lic_data[self.lic_pay_period_key])
                    if self.field_exists(self.lic_date_of_renewal_key):
                        self.set_lic_date_of_renewal(self.lic_data[self.lic_date_of_renewal_key])
                else:
                    raise ValueError("cost must have currency")
            elif self.field_exists(self.lic_curr_key) or self.field_exists(self.lic_date_of_renewal_key) or self.field_exists(self.lic_pay_period_key):
                raise ValueError("cost based field entered but not cost")
            if self.field_exists(self.lic_date_of_expiration_key):
                self.set_lic_date_of_expiration(self.lic_data[self.lic_date_of_expiration_key])
            if self.field_exists(self.lic_restrictions_key):
                self.set_lic_restrictions(self.lic_data[self.lic_restrictions_key])


class DelLicReq(Request):
    def validate_data(self):
        log.log("INFO", "delete license request begin validation")
        if not self.field_exists(self.lic_id_key):
            log.log("ERROR", "license ID missing, required for delete; terminating program")
            raise ValueError("Missing license ID")
        else:
            self.set_lic_id(self.lic_data[self.lic_id_key])


class AssignLicense(Request):
    def validate_data(self):
        log.log("INFO", "assign license request begin validation")
        if not self.field_exists(self.lic_id_key) or (not self.field_exists(self.lic_employee_id_key) and not self.field_exists(self.lic_computer_id_key)):
            log.log("ERROR", "one or more fields required for assigning are missing; terminating program")
            raise ValueError("Missing one or more required field")
        elif self.field_exists(self.lic_employee_id_key) and self.field_exists(self.lic_computer_id_key): 
            log.log("ERROR", "attempting to assign both computer and employee simultaneously; not supported; terminating program")
            raise ValueError("Can't assign employee and computer at same time")
        else:
            self.set_lic_id(self.lic_data[self.lic_id_key])
            if self.field_exists(self.lic_data[self.lic_employee_id_key]):
                self.set_lic_employee_id(self.lic_data[self.lic_employee_id_key])
            else:
                self.set_lic_computer_id(self.lic_data[self.lic_computer_id_key])


class UpdateLicReq(Request):
    def validate_data(self):
        log.log("INFO", "update license request begin validation")
        if not self.field_exists(self.lic_id_key):
            log.log("ERROR", "license ID missing, required for updating; terminating program")
            raise ValueError("Missing license ID")
        else:
            if self.field_exists(self.lic_name_key):
                self.set_lic_name(self.lic_data[self.lic_name_key])
            if self.field_exists(self.lic_version_key):
                self.set_lic_version(self.lic_data[self.lic_version_key])
            if self.field_exists(self.lic_type_key):
                self.set_lic_type(self.lic_data[self.lic_type_key])
            if self.field_exists(self.lic_cost_key):
                self.set_lic_cost(self.lic_data[self.lic_cost_key])
            if self.field_exists(self.lic_curr_key):
                self.set_lic_curr(self.lic_data[self.lic_curr_key])
            if self.field_exists(self.lic_pay_period_key):
                self.set_lic_pay_period(self.lic_data[self.lic_pay_period_key])
            if self.field_exists(self.lic_date_of_renewal_key):
                self.set_lic_date_of_renewal(self.lic_data[self.lic_date_of_renewal_key])
            if self.field_exists(self.lic_date_of_expiration_key):
                self.set_lic_date_of_expiration(self.lic_data[self.lic_date_of_expiration_key])
            if self.field_exists(self.lic_restrictions_key):
                self.set_lic_restrictions(self.lic_data[self.lic_restrictions_key])


class QueryLicReq(Request):
    def validate_data(self):
        log.log("INFO", "query license request begin validation")
        if (len(self.lic_data.keys()) > 1):
             log.log("ERROR", "multiple fields given in query request, not supported; program terminated")
             raise ValueError("Query by multiple fields not currently supported")
        else:
            if self.field_exists(self.lic_name_key):
                self.set_lic_name(self.lic_data[self.lic_name_key])
            if self.field_exists(self.lic_type_key):
                self.set_lic_type(self.lic_data[self.lic_type_key])
            if self.field_exists(self.lic_id_key):
                self.set_lic_type(self.lic_data[self.lic_id_key])        

#here for testing purposes
class QueryReturn(Request):
    def validate_data(self):
        log.log("INFO", "returned table  begin validation")
        if not self.field_exists(self.lic_name_key) or not self.field_exists(self.lic_version_key) or not self.field_exists(self.lic_type_key):
            log.log("ERROR", "one or more components required for licenses are missing; terminating program")
            raise ValueError("Missing one or more required field")
        else:
            self.set_lic_id(self.lic_data[self.lic_id_key])
            self.set_lic_name(self.lic_data[self.lic_name_key])
            self.set_lic_version(self.lic_data[self.lic_version_key])
            self.set_lic_type(self.lic_data[self.lic_type_key])
            if self.field_exists(self.lic_cost_key):
                self.set_lic_cost(self.lic_data[self.lic_cost_key])
            if self.field_exists(self.lic_curr_key):
                self.set_lic_curr(self.lic_data[self.lic_curr_key])
            if self.field_exists(self.lic_pay_period_key):
                self.set_lic_pay_period(self.lic_data[self.lic_pay_period_key])
            if self.field_exists(self.lic_date_of_renewal_key):
                self.set_lic_date_of_renewal(self.lic_data[self.lic_date_of_renewal_key])
            if self.field_exists(self.lic_date_of_expiration_key):
                self.set_lic_date_of_expiration(self.lic_data[self.lic_date_of_expiration_key])
            if self.field_exists(self.lic_restrictions_key):
                self.set_lic_restrictions(self.lic_data[self.lic_restrictions_key])