from abc import ABC
from abc import abstractmethod
import json

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
    

    def validate_lic_name(self):
        return self.validate_str_field(self.lic_name_key, 2, 40)
    
    def validate_lic_version(self):
        return self.validate_str_field(self.lic_version_key, 1, 8)
    
    def validate_lic_type(self):
        return self.validate_str_field(self.lic_type_key, 1, 20)
    
    def validate_lic_cost(self):
        return self.validate_str_field(self.lic_cost_key, 1, 20)
    
    def validate_lic_curr(self):
        return self.validate_str_field(self.lic_curr_key, 1, 20)
    
    def validate_lic_period(self):
        return self.validate_str_field(self.lic_pay_period_key, 1, 20)
    
    def validate_lic_date_of_renewal(self):
        return self.validate_str_field(self.lic_date_of_renewal_key, 1, 20)
    
    def validate_lic_date_of_expiration(self):
        return self.validate_str_field(self.lic_date_of_expiration_key, 1, 20)
    
    def validate_lic_restrictions(self):
        return self.validate_str_field(self.lic_restrictions_key, 1, 20)
    
    def validate_lic_id(self):
        return self.validate_str_field(self.lic_restrictions_key, 1, 20)
    
    def validate_lic_employee_id(self):
        return self.validate_str_(self.lic_restrictions_key, 1, 20)
    
    def validate_lic_computer_id(self):
        return self.validate_str_field(self.lic_restrictions_key, 1, 20)


    @abstractmethod
    def validate_data(self):
        pass


class AddLicReq(Request):
    def validate_data(self):
        if not self.field_exists(self.lic_name_key) or not self.field_exists(self.lic_version_key) or not self.field_exists(self.lic_type_key):
            raise ValueError("Missing one or more required field")
        self.validate_lic_name()
        self.validate_lic_version()
        self.validate_lic_type()
        self.validate_lic_cost()
        self.validate_lic_curr()
        self.validate_lic_period()
        self.validate_lic_date_of_renewal()
        self.validate_lic_date_of_expiration()
        self.validate_lic_restrictions()

class AssignLicense(Request):
    def validate_data(self):
        if not self.field_exists(self.lic_id_key):
            pass

    
if __name__ == "__main__":
    request_obj = AddLicReq('{"name":"thesoft","ver":"3.0","type":"Enterprise"}')
    print("all good")