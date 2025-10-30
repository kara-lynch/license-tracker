from abc import ABC
from abc import abstractmethod
import json
from src.validation import validation_checks
from src.validation import validate_field

class Request(ABC):
    lic_data:dict
    clean_data:dict

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
    

    def set_lic_name(self, new_field):
        validate_field.validate_lic_name(str(new_field))
        self.lic_name = new_field
    
    def set_lic_version(self, new_field):
        validate_field.validate_lic_version(str(new_field)) 
        self.lic_name = new_field

    def set_lic_type(self, new_field):
        validate_field.validate_lic_type(str(new_field))
        self.lic_name = new_field
    
    def set_lic_cost(self, new_field):
        validate_field.validate_lic_cost(str(new_field))
        self.lic_name = new_field
    
    def set_lic_curr(self, new_field):
        validate_field.validate_lic_curr(str(new_field))
        self.lic_name = new_field
    
    def set_lic_pay_period(self, new_field):
        validate_field.validate_lic_pay_period(str(new_field))
        self.lic_name = new_field
    
    def set_lic_date_of_renewal(self, new_field):
        validate_field.validate_lic_date_of_renewal(str(new_field))
        self.lic_name = new_field
    
    def set_lic_date_of_expiration(self, new_field):
        validate_field.validate_lic_date_of_expiration(str(new_field))
        self.lic_name = new_field
    
    def set_lic_restrictions(self, new_field):
        validate_field.validate_lic_restrictions(str(new_field))
        self.lic_name = new_field
    
    def set_lic_id(self, new_field):
        validate_field.validate_lic_id(str(new_field))
        self.lic_name = new_field
    
    def set_lic_employee_id(self, new_field):
        validate_field.validate_lic_employee_id(str(new_field))
        self.lic_name = new_field
    
    def set_lic_computer_id(self, new_field):
        validate_field.validate_lic_computer_id(str(new_field))
        self.lic_name = new_field

    def add_clean_data_field(self, new_key, new_field):
        self.clean_data[new_key, new_field]

    def get_clean_data_dict(self):
        if self.clean_data == None:
            self.clean_data = {}
        return self.clean_data


    @abstractmethod
    def validate_data(self):
        pass


class AddLicReq(Request):
    def validate_data(self):
        if not self.field_exists(self.lic_name_key) or not self.field_exists(self.lic_version_key) or not self.field_exists(self.lic_type_key):
            raise ValueError("Missing one or more required field")
        else:
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
        if not self.field_exists(self.lic_id_key) or (not self.field_exists(self.lic_employee_id_key) and not self.field_exists(self.lic_computer_id_key)):
            raise ValueError("Missing one or more required field")
        elif self.field_exists(self.lic_employee_id_key) and self.field_exists(self.lic_computer_id_key): 
            raise ValueError("Can't assign employee and computer at same time")
        else:
            self.set_lic_id(self.lic_data[self.lic_id_key])
            if self.field_exists(self.lic_data[self.lic_employee_id_key]):
                self.set_lic_employee_id(self.lic_data[self.lic_employee_id_key])
            else:
                self.set_lic_computer_id(self.lic_data[self.lic_computer_id_key])


class UpdateLicReq(Request):
    def validate_data(self):
        if not self.field_exists(self.lic_id_key):
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
        if (len(self.lic_data.keys()) > 1):
             raise ValueError("Query by multiple fields not currently supported")
        else:
            if self.field_exists(self.lic_name_key):
                self.set_lic_name(self.lic_data[self.lic_name_key])
            if self.field_exists(self.lic_type_key):
                self.set_lic_type(self.lic_data[self.lic_type_key])
            if self.field_exists(self.lic_id_key):
                self.set_lic_type(self.lic_data[self.lic_id_key])               

def testFunc():
    request_obj = AddLicReq('{"name":"softwareeeeeeeeeee","ver":"4.0","type":"enterprise"}')
    print("all good")