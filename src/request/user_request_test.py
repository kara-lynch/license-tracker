from src.request import user_request
from src.validation import validation_checks
import pytest

#add license, valid data, minimum fields
def test_add_min_valid():
    request_obj = user_request.AddLicReq('{"name":"AddedLic","ver":"3.0","type":"enterprise"}')
    print(request_obj.lic_data)
    print(request_obj.get_clean_data_json())
    print("all good")

    assert request_obj.get_clean_data_dict() == {"name":"AddedLic","ver":"3.0","type":"enterprise"}

#add license, valid data, maximum fields
def test_add_max_valid():
    request_obj = user_request.AddLicReq('{"name":"AddedLic2","ver":"3.0","type":"enterprise","cost":2000.50,"curr":"USD","period":"Annual","date_of_renewal":"12-17-2025","expiration_date":"12-20-2025","restrictions":"Australia"}')
    print(request_obj.lic_data)
    print(request_obj.get_clean_data_json())
    print("all good")

    assert request_obj.get_clean_data_dict() == {"name":"AddedLic2","ver":"3.0","type":"enterprise","cost":2000.50,"curr":"USD","period":"Annual","date_of_renewal":"12-17-2025","expiration_date":"12-20-2025","restrictions":"Australia"}

#add license, extra data field not expected, should be ignored and not returned in cleaned data
def test_add_extra_field():
    request_obj = user_request.AddLicReq('{"name":"AddedLic3","ver":"3.0","type":"enterprise", "badReq":"DROP LICENSE"}')
    print(request_obj.lic_data)
    print(request_obj.get_clean_data_json())
    print(request_obj.get_clean_data_dict().get("storage"))
    print("all good")

    assert request_obj.get_clean_data_dict() == {"name":"AddedLic3","ver":"3.0","type":"enterprise"}

#add license, name missing, should throw value error
def test_add_name_missing():
    with pytest.raises(ValueError):
        request_obj = user_request.AddLicReq('{"ver":"3.0","type":"enterprise"}')

#add license, version missing, should throw value error
def test_add_version_missing():
    with pytest.raises(ValueError):
        request_obj = user_request.AddLicReq('{name:"AddedLic5","type":"enterprise"}')

#add license, type missing, should throw value error
def test_add_type_missing():
    with pytest.raises(ValueError):
        request_obj = user_request.AddLicReq('{name:"AddedLic6","ver":"3.0"}')

#add license, type name too long, should throw value error
def test_lic_name_too_long():
    with pytest.raises(ValueError):
        request_obj = user_request.AddLicReq('{name:"AddedLic666666666666666666666666666666666","ver":"3.0","type":"enterprise"}')

def test_lic_name_too_short():
    with pytest.raises(ValueError):
        request_obj = user_request.AddLicReq('{"name":"","ver":"v0.8","type":"Enterprise","cost":1200.99,"curr":"USD","period":"annual","date_of_renewal":"2026-03-24","expiration_date":"2045-10-24","restrictions":"Asia-Pacific Region"}')

#add license, testing has expiration function valid data
def test_has_expiration_true():
    request_obj = user_request.AddLicReq('{"name":"Windows 11","ver":"v0.8","type":"Enterprise","cost":1200.99,"curr":"USD","period":"annual","date_of_renewal":"2026-03-24","expiration_date":"2045-10-24","restrictions":"Asia-Pacific Region"}')
    
    assert request_obj.has_expiration() == True

def test_has_expiration_False():
    request_obj = user_request.AddLicReq('{"name":"Windows 11","ver":"v0.8","type":"Enterprise","cost":1200.99,"curr":"USD","period":"annual","date_of_renewal":"2026-03-24","restrictions":"Asia-Pacific Region"}')
    
    assert request_obj.has_expiration() == False

def test_has_cost_true():
    request_obj = user_request.AddLicReq('{"name":"Windows 11","ver":"v0.8","type":"Enterprise","cost":1200.99,"curr":"USD","period":"annual","date_of_renewal":"2026-03-24","expiration_date":"2045-10-24","restrictions":"Asia-Pacific Region"}')
    
    assert request_obj.has_cost() == True

def test_has_cost_false():
    request_obj = user_request.AddLicReq('{"name":"Windows 11","ver":"v0.8","type":"Enterprise","expiration_date":"2045-10-24","restrictions":"Asia-Pacific Region"}')
    
    assert request_obj.has_cost() == False

def test_has_restrictions_true():
    request_obj = user_request.AddLicReq('{"name":"Windows 11","ver":"v0.8","type":"Enterprise","cost":1200.99,"curr":"USD","period":"annual","date_of_renewal":"2026-03-24","expiration_date":"2045-10-24"}')
    
    assert request_obj.has_cost() == True

def test_has_restrictions_false():
    request_obj = user_request.AddLicReq('{"name":"Windows 11","ver":"v0.8","type":"Enterprise","expiration_date":"2045-10-24"}')
    
    assert request_obj.has_restrictions() == False
