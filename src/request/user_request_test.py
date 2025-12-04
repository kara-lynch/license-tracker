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

def test_del_valid():
    request_obj = user_request.DelLicReq('{"licenseID":12}')
    assert request_obj.get_clean_data_dict() == {"licenseID":12}

def test_del_empty():
    with pytest.raises(ValueError):
        request_obj = user_request.DelLicReq('{}')

def test_query_valid_empty():
    request_obj = user_request.QueryLicReq('{}')
    assert request_obj.get_clean_data_dict() == {}

#add license, type name too long, should throw value error
def test_lic_name_too_long():
    with pytest.raises(ValueError):
        request_obj = user_request.AddLicReq('{"name":"AddedLic666666666666666666666666666666666","ver":"3.0","type":"enterprise"}')

def test_lic_name_too_short():
    with pytest.raises(ValueError):
        request_obj = user_request.AddLicReq('{"name":"","ver":"v0.8","type":"Enterprise","cost":1200.99,"curr":"USD","period":"annual","date_of_renewal":"2026-03-24","expiration_date":"2045-10-24","restrictions":"Asia-Pacific Region"}')

def test_cost_negative():
    with pytest.raises(ValueError):
        request_obj = user_request.AddLicReq('{"name":"Windows 11","ver":"v0.8","type":"Enterprise","cost":-1200.99,"curr":"USD","period":"annual","date_of_renewal":"2026-03-24","expiration_date":"2045-10-24","restrictions":"Asia-Pacific Region"}')

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
    request_obj = user_request.AddLicReq('{"name":"Windows 11","ver":"v0.8","type":"Enterprise","cost":1200.99,"curr":"USD","period":"annual","date_of_renewal":"2026-03-24","expiration_date":"2045-10-24","restrictions":"Asia-Pacific Region"}')   
    assert request_obj.has_restrictions() == True

def test_has_restrictions_false():
    request_obj = user_request.AddLicReq('{"name":"Windows 11","ver":"v0.8","type":"Enterprise","expiration_date":"2045-10-24"}')
    assert request_obj.has_restrictions() == False

def test_lic_id_negative():
    with pytest.raises(ValueError):
        request_obj = user_request.DelLicReq('{"licenseID":-12}')

def test_lic_id_wrong_type():
    with pytest.raises(TypeError):
        request_obj = user_request.DelLicReq('{"licenseID":12.5}')

#query range, valid data, min fields
def test_query_range_min_request():
    request_obj = user_request.QueryRangeLicReq('{"range":5}')
    print(request_obj.lic_data)
    print(request_obj.get_clean_data_json())
    print("all good")
    assert request_obj.get_clean_data_dict() == {"range":5}

#query range, valid data, all fields
def test_query_range_all_request():
    request_obj = user_request.QueryRangeLicReq('{"range":5,"offset":1,"sort_field":"NAME"}')
    print(request_obj.lic_data)
    print(request_obj.get_clean_data_json())
    print("all good")
    assert request_obj.get_clean_data_dict() == {"range":5,"offset":1,"sort_field":"NAME"}

#query range, valid data, two fields
def test_query_range_sort_no_offset_request():
    request_obj = user_request.QueryRangeLicReq('{"range":5,"sort_field":"date_added"}')
    print(request_obj.lic_data)
    print(request_obj.get_clean_data_json())
    print("all good")
    assert request_obj.get_clean_data_dict() == {"range":5,"sort_field":"DATE_ADDED"}

#query range, invalid sort field
def test_query_range_request_enum_negative():
    with pytest.raises(ValueError):
        request_obj = user_request.QueryRangeLicReq('{"range":5,"sort_field":"hello"}')






    
