from flask import Flask, request, abort
from src.logger import log
from src.util import authentication 
from src.request.user_request import *
from src.validation import *

import json

log.log("INFO", "REST API started.")

app = Flask(__name__)

@app.get("/hello_world/")
def hello():
    return f'<p>Hello!</p>'

"""
When sending get request to this URI, API will respond with instructions for how to use API.
"""
@app.get("/")
def help():
    return "<p>HELP SCREEN TBA<p>"

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
    try:
        log.log("INFO", "Request to add license received.")
        license_request = request.json
        user_req = AddLicReq(json.dumps(license_request))
        success, auth_response = authentication.authorize(request.headers)
        if success:
            # INTEGRATION:
            # credentials = Credentials(auth_response)
            # check user is a manager and IT/Legal
            # request_info = AddLicReq(auth_response)
            # LicenseDatabase.addLicense(request_info, credentials)
            return f'<p>License added<p>'
        else:
            abort(401)
    # CHECK FOR THE EXCEPT FROM USER CRED CLASS
    except:
        # If the code ends up here, it was probably the user's fault
        abort(400)

"""
User expected to provide a JSON object in the body includin the fields of the license being added.

Required: 
    - "id": int
"""
@app.post("/deleteLicense/")
def deleteLicense():
    return f'<p>NOT YET IMPLEMENTED</p>'

"""
For updating a license, the user is expected to provide a license ID, 
along with the fields they want to update. 

Any fields not provided will not be updated.
"""
@app.post("/updateLicense/")
def updateLicense():
    return f'<p>NOT YET IMPLEMENTED</p>'


# Query methods

"""
Alternative URI for getting the API documentation.
"""
@app.get("/")
def help_screen():
    return f'NOT YET IMPLEMENTED'

@app.get("/seeLicenses/")
def seeLicenses():
    try:
        log.log("INFO", "Request to see all licenses received.")
        license_request = request.json
        # CREATE REQUEST OBJECT
        success, auth_response = authentication.authorize(request.headers)
        if success:
            # INTEGRATION:
            # credentials = Credentials(auth_response)
            # request_info = AddLicReq(auth_response)
            # LicenseDatabase.addLicense(request_info, credentials)
            return f'<p>License added<p>'
        else:
            abort(401)
    # CHECK FOR THE EXCEPT FROM USER CRED CLASS
    except:
        # If the code ends up here, it was probably the user's fault
        abort(400)

@app.get("/filteredView/")
def filteredView():
    return f'NOT YET IMPLEMENTED'


# Error handlers

# @app.errorhandler(401)
# def handle_401():
#     return f'ERROR: Unable to authenticate user.', 401
