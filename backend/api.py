from flask import Flask, request, abort
from src.logger import log
from src.database import db
from src.util import authentication 
from src.request.user_request import *
from src.validation import *
# from src.database.record_entities_licenseID import *
from src.credentials.credentials_manager import *
from flask_cors import CORS

import json

log.log("INFO", "REST API started.")
# db = LicenseDAO()

app = Flask(__name__)

CORS(
    app,
    resources={r"/*": {"origins": "http://localhost:5173"}},
    allow_headers=["Content-Type", "Bearer", "Authorization"],
    supports_credentials=True,
) 

@app.get("/hello_world/")
def hello():
    return f'<p>Hello!</p>'

"""
When sending get request to this URI, API will respond with instructions for how to use API.
"""
# @app.get("/")
# def help():
#     return "<p>HELP SCREEN TBA<p>"

"""
Returns a JSON object displaying information about the developers of this project.
The data is pulled from config/about_us.json
"""
@app.get("/aboutUs/")
def about_us():
    try:
        log.log("INFO", "Request to view the about us page received.")
        about_path = "./src/config/about_us.json"

        log.log("DEBUG", "Loading about_us.json...")
        with open(about_path, "r") as file:
            about_json = json.load(file)
        
        log.log("DEBUG", "about_us.json loaded successfully")        
        return json.loads(about_json)
    
    except OSError:
        log.log("WARNING", f"Error loading about_us.json")
        abort(500)
        
    except Exception as e:
        log.log("WARNING", f"Error occurred while handling about us request: {e.args[0]}")
        abort(500)

"""
User expected to provide a JSON object in the body includin the fields of the license being added.

If user fails to include the JSON object in the request body, a 415 error is returned.

Required: 
    - "name": str
    - "ver": str
    - "type": str

Optional fields:
    - "cost": float and "curr": str with 3 chars (if one is present, the other must be as well)
    - "period": str (cost and curr required)
    - "renewal_date": str, format "yyyy-mm-dd
    - "expiration_date": str, format "yyyy-mm-dd
    - "restrictions": str
"""
@app.post("/addLicense/")
def addLicense():
    # Extract info from request, create request object 
    try:
        log.log("INFO", "Request to add license received.")
        log.log("DEBUG", "Getting user request...")
        license_request = request.json
        log.log("DEBUG", "Loading and validating user request...")
        user_req = AddLicReq(json.dumps(license_request))
        log.log("DEBUG", "Add license request validated successfully")
    except Exception as e:
        # If the code ends up here, it was probably the user's fault
        log.log("WARNING", f"Error occurred while processing add license request: {e.args[0]}")
        abort(400)

    # Verify credentials received from authentication server.
    try:
        log.log("DEBUG", "Sending user authentication token to auth server...")
        success, auth_response = authentication.authorize(request.headers)
        if not success:
            raise Exception("User authentication token invalid.")
        log.log("DEBUG", "User credentials received successfully. Validating...")
        credentials = UserCredentials(json.loads(auth_response))
        credentials.validate()
        log.log("DEBUG", "User credentials validated successfully.")

        # check user is a manager and IT/Legal
        if not credentials.has_license_auth():
            raise Exception("User not authorized to make this request.")
        log.log("DEBUG", "User authorization confirmed.")
    except Exception as e:
        log.log("WARNING", f"Error occurred while processing user credentials for add license request: {e.args[0]}")
        abort(401)

    # DB Call. If method returns false, user couldn't be authorizaed.
    try:
        log.log("DEBUG", "Initiating DB call for add license request.")
        added_record = db.AddLicense(user_req, credentials)
        log.log("DEBUG", "License add request succeeded.")
    except Exception as e:
        log.log("WARNING", f"Error occurred with database during add license request: {e.args[0]}")
        abort(400)
    if not added_record:
        #This has no logging because the DAO already logs any problem that would cause it to return false.
        abort(401)
    log.log("DEBUG", "Add license request processed successfully. Terminating process.")
    return f'<p>License added<p>'

"""
User expected to provide a JSON object in the body includin the fields of the license being added.

Required: 
    - "licenseID": int
"""
@app.delete("/deleteLicense/")
def deleteLicense():
    # Extract info from request, create request object 
    try:
        log.log("INFO", "Request to delete license received.")
        log.log("DEBUG", "Getting user request...")
        license_request = request.json
        log.log("DEBUG", "Loading and validating user request...")
        user_req = DelLicReq(json.dumps(license_request))
        log.log("DEBUG", "Delete license request validated successfully")
    except Exception as e:
        # If the code ends up here, it was probably the user's fault
        log.log("WARNING", f"Error occurred while processing delete license request: {e.args[0]}")
        abort(400)

    # Verify credentials received from authentication server.
    try:
        log.log("DEBUG", "Sending user authentication token to auth server...")
        success, auth_response = authentication.authorize(request.headers)
        log.log("DEBUG", "Authentication token received successfully.")
        if not success:
            raise Exception("User authentication token invalid.")
        log.log("DEBUG", "Authentication token received successfully. Validating...")
        credentials = UserCredentials(json.loads(auth_response))
        credentials.validate()
        log.log("DEBUG", "User credentials validated successfully.")

        # check user is a manager and IT/Legal
        if not credentials.has_license_auth():
            raise Exception("User not authorized to make this request")
        log.log("DEBUG", "User authorization confirmed.")
    except Exception as e:
        log.log("WARNING", f"Error occurred while processing user credentials for add license request: {e.args[0]}")
        abort(401)

    # DB Call. If method returns false, user couldn't be authorizaed.
    try:
        log.log("DEBUG", "Initiating DB call for add license request.")
        deleted_record = db.DeleteLicense(user_req, credentials)
        log.log("DEBUG", "License add request succeeded.")
    except:
        log.log("WARNING", f"Error occurred with database during add license request: {e.args[0]}")
        abort(400)
    if not deleted_record:
        #This has no logging because the DAO already logs any problem that would cause it to return false.
        abort(401)
    
    log.log("DEBUG", "Add license request processed successfully. Terminating process.")
    return f'<p>License L{license_request["licenseID"]} removed.<p>'

"""
For updating a license, the user is expected to provide a license ID, 
along with the fields they want to update. 

Any fields not provided will not be updated.
"""
@app.post("/editLicense/")
def editLicense():
    # Extract info from request, create request object 
    try:
        log.log("INFO", "Request to edit license received.")
        license_request = request.json
        user_req = EditLicReq(json.dumps(license_request))
    except:
        # If the code ends up here, it was probably the user's fault
        abort(400)

    # Verify credentials received from authentication server.
    try:
        success, auth_response = authentication.authorize(request.headers)
        if not success:
            raise Exception("User authentication token invalid.")
        credentials = UserCredentials(json.loads(auth_response))
        credentials.validate()

        # check user is a manager and IT/Legal
        if not credentials.has_license_auth():
            raise Exception
    except:
        abort(401)

    # DB Call. If method returns false, user couldn't be authorizaed.
    try:
        updated_record = db.EditLicense(user_req, credentials)
    except:
        abort(400)
    if not updated_record:
        abort(401)
    
    return f'<p>License updated<p>'

# Query methods

@app.get("/seeLicenses/")
def seeLicenses():
    # Extract token from request.
    # This method has no logging because the authenticate module already logs everything.
    try:
        log.log("INFO", "Request to see all licenses received.")
        log.log("DEBUG", "Sending user authentication token to auth server...")
        success, auth_response = authentication.authorize(request.headers)
        if success:
            log.log("DEBUG", "Authentication token received successfully. Validating...")
            credentials = UserCredentials(json.loads(auth_response))
            credentials.validate()
            log.log("DEBUG", "User credentials validated successfully")
            log.log("DEBUG", "Initiating DB call for see licenses request.")
            records = db.seeLicenses()
            log.log("DEBUG", "See licenses request processed successfully. Terminating process.")
            return records
        else:
            raise Exception
    except:
        # If the code ends up here, it was probably the user's fault
        abort(401)

"""
To see a specific range of licenses, the following fields can be provided by the frontend:

range: int
offset: int (optional)
sort_field: str (optional)
ascending: bool (optional)

If provided, sort_field is case sensitive and must match one of the following: [licenseName, licenseType, price,
period, renewalDate, endDate, restriction]
"""
@app.post("/seeLicenseRange/")
def seeLicenseRange():
    # Extract token from request.
    try:
        log.log("INFO", "Request to see a range of licenses received.")
        log.log("DEBUG", "Getting user request...")
        license_request = request.json
        log.log("DEBUG", "Loading and validating user request...")
        user_req = QueryRangeLicReq(json.dumps(license_request))
        log.log("DEBUG", "Add license request validated successfully")
    except Exception as e:
        # If the code ends up here, it was probably the user's fault
        log.log("WARNING", f"Error occurred while processing see license range request: {e.args[0]}")
        abort(400)

    # Verify credentials received from auth server
    try:
        log.log("DEBUG", "Sending user authentication token to auth server...")
        success, auth_response = authentication.authorize(request.headers)
        if not success:
            raise Exception("User authentication token invalid.")
        log.log("DEBUG", "User credentials received successfully. Validating...")
        credentials = UserCredentials(json.loads(auth_response))
        credentials.validate()
        log.log("DEBUG", "User credentials validated successfully.")
    except Exception as e:
        log.log("WARNING", f"Error occurred while processing user credentials for see license range request: {e.args[0]}")
        abort(401)

    # DB Call
    try:
        log.log("DEBUG", "Initiating DB call for see license range request.")
        records = db.seeLicenseRange(user_req)
        log.log("DEBUG", "See license range request processed successfully. Terminating process.")
        return records
    
    except Exception as e:
        # If the code ends up here, it was probably the user's fault
        log.log("WARNING", f"Error occurred with database during see license range request: {e.args[0]}")
        abort(401)

"""
User expected to provide a JSON object in the body including the fields of the assignment being added.

If user fails to include the JSON object in the request body, a 415 error is returned.

Required: 
    - "licenseId": int
    - "employeeId": int
"""
@app.post("/employeeAssign/")
def employeeAssign():
    # Extract info from request, create request object 
    try:
        log.log("INFO", "Request to assign license to employee received.")
        log.log("DEBUG", "Getting user request...")
        license_request = request.json
        log.log("DEBUG", "Loading and validating user request...")
        user_req = EmpAssignLicReq(json.dumps(license_request))
        log.log("DEBUG", "Employee assign request validated successfully")
    except Exception as e:
        # If the code ends up here, it was probably the user's fault
        log.log("WARNING", f"Error occurred while processing employee assign request: {e.args[0]}")
        abort(400)

    # Verify credentials received from authentication server.
    try:
        log.log("DEBUG", "Sending user authentication token to auth server...")
        success, auth_response = authentication.authorize(request.headers)
        if not success:
            raise Exception("User authentication token invalid.")
        log.log("DEBUG", "User credentials received successfully. Validating...")
        credentials = UserCredentials(json.loads(auth_response))
        credentials.validate()
        log.log("DEBUG", "User credentials validated successfully.")

        # check user is a manager and IT/Legal
        if not credentials.has_license_auth():
            raise Exception("User not authorized to make this request.")
        log.log("DEBUG", "User authorization confirmed.")
    except Exception as e:
        log.log("WARNING", f"Error occurred while processing user credentials for employee assign request: {e.args[0]}")
        abort(401)

    # DB Call. If method returns false, user couldn't be authorizaed.
    try:
        log.log("DEBUG", "Initiating DB call for employee assign request.")
        added_record = db.employeeAssign(user_req, credentials)
        log.log("DEBUG", "Employee assign request succeeded.")
    except Exception as e:
        log.log("WARNING", f"Error occurred with database during employee assign request: {e.args[0]}")
        abort(400)
    if not added_record:
        #This has no logging because the DAO already logs any problem that would cause it to return false.
        abort(401)
    log.log("DEBUG", "Add license request processed successfully. Terminating process.")
    return f'<p>License assigned<p>'

"""
User expected to provide a JSON object in the body including the fields of the assignment being removed.

If user fails to include the JSON object in the request body, a 415 error is returned.

Required: 
    - "licenseId": int
    - "employeeId": int
"""
@app.delete("/employeeUnassign/")
def employeeUnassign():
    # Extract info from request, create request object 
    try:
        log.log("INFO", "Request to unassign license from employee received.")
        log.log("DEBUG", "Getting user request...")
        license_request = request.json
        log.log("DEBUG", "Loading and validating user request...")
        user_req = EmpAssignLicReq(json.dumps(license_request))
        log.log("DEBUG", "Employee unassign request validated successfully")
    except Exception as e:
        # If the code ends up here, it was probably the user's fault
        log.log("WARNING", f"Error occurred while processing employee unassign request: {e.args[0]}")
        abort(400)

    # Verify credentials received from authentication server.
    try:
        log.log("DEBUG", "Sending user authentication token to auth server...")
        success, auth_response = authentication.authorize(request.headers)
        log.log("DEBUG", "Authentication token received successfully.")
        if not success:
            raise Exception("User authentication token invalid.")
        log.log("DEBUG", "Authentication token received successfully. Validating...")
        credentials = UserCredentials(json.loads(auth_response))
        credentials.validate()
        log.log("DEBUG", "User credentials validated successfully.")

        # check user is a manager and IT/Legal
        if not credentials.has_license_auth():
            raise Exception("User not authorized to make this request.")
        log.log("DEBUG", "User authorization confirmed.")
    except:
        log.log("WARNING", f"Error occurred while processing user credentials for employee unassign request: {e.args[0]}")
        abort(401)

    # DB Call. If method returns false, user couldn't be authorizaed.
    try:
        log.log("DEBUG", "Initiating DB call for employee unassign request.")
        added_record = db.employeeUnassign(user_req, credentials)
        log.log("DEBUG", "Employee unassign request succeeded.")
    except:
        log.log("WARNING", f"Error occurred with database during employee unassign request: {e.args[0]}")
        abort(400)
    if not added_record:
        #no logging here, the DAO already logs anything that would cause it to return false
        abort(401)
    
    log.log("DEBUG", "Employee unassign request processed successfully. Terminating process.")
    return f'<p>License assignment removed<p>'

"""
To see licenses assigned to a user, the following fields can be provided by the frontend:

range: int
offset: int (optional)
sort_field: str (optional)
ascending: bool (optional)
employeeId: int (optional)

If provided, sort_field is case sensitive and must match one of the following: [licenseName, licenseType, price,
period, renewalDate, endDate, restriction]

employeeId is only checked if the user is a manager. A non-manager user can only see licenses assigned to that user.
"""
@app.post("/seeAssignment/")
def seeAssignment():
    # Extract token from request.
    try:
        log.log("INFO", "Request to see a range of license assignments received.")
        log.log("DEBUG", "Getting user request...")
        license_request = request.json
        log.log("DEBUG", "Loading and validating user request...")
        user_req = AssignQueryLicReq(json.dumps(license_request))
        log.log("DEBUG", "See user assignment request validated successfully")
    except Exception as e:
        # If the code ends up here, it was probably the user's fault
        log.log("WARNING", f"Error occurred while processing see user assignment request: {e.args[0]}")
        abort(400)

    # Verify credentials received from auth server
    try:
        log.log("DEBUG", "Sending user authentication token to auth server...")
        success, auth_response = authentication.authorize(request.headers)
        if not success:
            raise Exception("User authentication token invalid.")
        log.log("DEBUG", "User credentials received successfully. Validating...")
        credentials = UserCredentials(json.loads(auth_response))
        credentials.validate()
        log.log("DEBUG", "User credentials validated successfully.")
    except Exception as e:
        log.log("WARNING", f"Error occurred while processing user credentials for see license range request: {e.args[0]}")
        abort(401)

    # DB Call
    try:
        log.log("DEBUG", "Initiating DB call for see user assignment request.")
        records = db.SeeAssignment(user_req, credentials)
        log.log("DEBUG", "See user assignment request processed successfully. Terminating process.")
        return records
    except:
        # If the code ends up here, it was probably the user's fault
        log.log("WARNING", f"Error occurred with database during see license range request: {e.args[0]}")
        abort(401)

# @app.get("/filteredView/")
# def filteredView():
#     return f'NOT YET IMPLEMENTED'


# Error handlers

# @app.errorhandler(401)
# def handle_401():
#     return f'ERROR: Unable to authenticate user.', 401
