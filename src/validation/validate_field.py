from src.validation import validation_checks

def field_exists(field):
        if field == None:
            return False
        else:
            return True
        

def validate_lic_name(data):
    if field_exists(data):
        validation_checks.check_field_size(str(data), 40, 2)
    
def validate_lic_version(data):
    if field_exists(data):
        validation_checks.check_field_size(str(data), 40, 2) 

def validate_lic_type(data):
    if field_exists(data):
        validation_checks.check_field_size(str(data), 40, 2)
    
def validate_lic_cost(data):
    if field_exists(data):
        validation_checks.check_field_size(str(data), 40, 2)
    
def validate_lic_curr(data):
    if field_exists(data):
        validation_checks.check_field_size(str(data), 40, 2)
    
def validate_lic_pay_period(data):
    if field_exists(data):
        validation_checks.check_field_size(str(data), 40, 2)
    
def validate_lic_date_of_renewal(data):
    if field_exists(data):
        validation_checks.check_field_size(str(data), 40, 2)
    
def validate_lic_date_of_expiration(data):
    if field_exists(data):
        validation_checks.check_field_size(str(data), 40, 2)
    
def validate_lic_restrictions(data):
    if field_exists(data):
        validation_checks.check_field_size(str(data), 40, 2)
    
def validate_lic_id(data):
    if field_exists(data):
        validation_checks.check_field_size(str(data), 40, 2)
    
def validate_lic_employee_id(data):
    if field_exists(data):
        validation_checks.check_field_size(str(data), 40, 2)
    
def validate_lic_computer_id(data):
    if field_exists(data):
        validation_checks.check_field_size(str(data), 40, 2)