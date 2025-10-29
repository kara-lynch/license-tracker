from abc import ABC
from abc import abstractmethod
import json
from src.validation import validation_checks
from src.validation import validate_field

class Request(ABC):
    lic_data = None

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

    lic_name:str
    lic_version:str
    lic_type:str
    lic_cost:float
    lic_curr:str
    lic_pay_period:str
    lic_date_of_renewal:str
    lic_date_of_expiration:str
    lic_restrictions:str
    lic_id:int
    lic_employee_id:int
    lic_computer_id:int


    def __init__(self, user_req_json):
        self.lic_data = json.loads(user_req_json)
        self.validate_data()
    
    def field_exists(self, field_name):
        if self.lic_data.get(field_name) == None:
            return False
        else:
            return True
        
    def validate_str_field(self, field_name, char_min = 0, char_max = 100):
        if self.field_exists(field_name):
            if len(self.lic_data[field_name]) > char_max or len(self.lic_data[field_name]) < char_min:
                raise ValueError(field_name + " field invalid")
        return True
    

    def set_lic_name(self, new_field):
            validate_field.validate_lic_name((self.lic_data[self.lic_name_key]))
    
    def set_lic_version(self, new_field):
            validate_field.validate_lic_version(str(self.lic_data[self.lic_version_key])) 

    def set_lic_type(self, new_field):
            validate_field.validate_lic_type(str(self.lic_data[self.lic_type_key]))
    
    def set_lic_cost(self, new_field):
            validate_field.validate_lic_cost(str(self.lic_data[self.lic_cost_key]))
    
    def set_lic_curr(self, new_field):
            validate_field.validate_lic_curr(str(self.lic_data[self.lic_curr_key]))
    
    def set_lic_pay_period(self, new_field):
            validate_field.validate_lic_pay_period(str(self.lic_data[self.lic_pay_period_key]))
    
    def set_lic_date_of_renewal(self, new_field):
            validate_field.validate_lic_date_of_renewal(str(self.lic_data[self.lic_date_of_renewal_key]))
    
    def set_lic_date_of_expiration(self, new_field):
            validate_field.validate_lic_date_of_expiration(str(self.lic_data[self.lic_date_of_expiration_key]))
    
    def set_lic_restrictions(self, new_field):
            validate_field.validate_lic_restrictions(str(self.lic_data[self.lic_restrictions_key]))
    
    def set_lic_id(self, new_field):
            validate_field.validate_lic_id(str(self.lic_data[self.lic_id_key]))
    
    def set_lic_employee_id(self, new_field):
            validate_field.validate_lic_employee_id(str(self.lic_data[self.lic_employee_id_key]))
    
    def set_lic_computer_id(self, new_field):
            validate_field.validate_lic_computer_id(str(self.lic_data[self.lic_computer_id_key]))


    @abstractmethod
    def validate_data(self):
        pass


class AddLicReq(Request):
    def validate_data(self):
        if not self.field_exists(self.lic_name_key) or not self.field_exists(self.lic_version_key) or not self.field_exists(self.lic_type_key):
            raise ValueError("Missing one or more required field")
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

class AssignLicense(Request):
    def validate_data(self):
        if not self.field_exists(self.lic_id_key):
            pass


def testFunc():
    request_obj = AddLicReq('{"name":"softwareeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee","ver":"4.0","type":"enterprise"}')
    print("all good")
    validation_checks.is_positive(2)