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
        license_request = request.json
        user_req = AddLicReq(json.dumps(license_request))
    except:
        # If the code ends up here, it was probably the user's fault
        abort(400)

    # Verify credentials received from authentication server.
    try:
        success, auth_response = authentication.authorize(request.headers)
        if not success:
            raise Exception
        credentials = UserCredentials(json.loads(auth_response))
        credentials.validate()

        # check user is a manager and IT/Legal
        if not credentials.has_license_auth():
            raise Exception
    except:
        abort(401)

    # DB Call. If method returns false, user couldn't be authorizaed.
    try:
        added_record = db.AddLicense(user_req, credentials)
    except:
        abort(400)
    if not added_record:
        abort(401)
    
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
        license_request = request.json
        user_req = DelLicReq(json.dumps(license_request))
    except:
        # If the code ends up here, it was probably the user's fault
        abort(400)

    # Verify credentials received from authentication server.
    try:
        success, auth_response = authentication.authorize(request.headers)
        if not success:
            raise Exception
        credentials = UserCredentials(json.loads(auth_response))
        credentials.validate()

        # check user is a manager and IT/Legal
        if not credentials.has_license_auth():
            raise Exception
    except:
        abort(401)

    # DB Call. If method returns false, user couldn't be authorizaed.
    try:
        deleted_record = db.DeleteLicense(user_req, credentials)
    except:
        abort(400)
    if not deleted_record:
        abort(401)
    
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
            raise Exception
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
    try:
        log.log("INFO", "Request to see all licenses received.")
        success, auth_response = authentication.authorize(request.headers)
        if success:
            credentials = UserCredentials(json.loads(auth_response))
            credentials.validate()
            records = db.seeLicenses()
            return records
        else:
            raise Exception
    except:
        # If the code ends up here, it was probably the user's fault
        abort(401)

@app.post("/seeLicenseRange/")
def seeLicenseRange():
    # Extract token from request.
    try:
        log.log("INFO", "Request to see all licenses received.")
        success, auth_response = authentication.authorize(request.headers)
        license_request = request.json
        user_req = QueryRangeLicReq(json.dumps(license_request))
        if success:
            credentials = UserCredentials(json.loads(auth_response))
            credentials.validate()
            records = db.seeLicenseRange()
            return records
        else:
            raise Exception
    except:
        # If the code ends up here, it was probably the user's fault
        abort(401)

# @app.get("/filteredView/")
# def filteredView():
#     return f'NOT YET IMPLEMENTED'


# Error handlers

# @app.errorhandler(401)
# def handle_401():
#     return f'ERROR: Unable to authenticate user.', 401
