from flask import Flask, request, abort
from src.logger import log
from src.util import authentication 

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
    log.log("INFO", "Request to add license received.")
    success, auth_response = authentication.authorize(request.headers)
    if success:
        license_request = request.json
        # INTEGRATION: Call backend function
        # credentials = Credentials(auth_response)
        # check user is a manager and IT/Legal
        # request_info = AddLicReq(auth_response)
        # LicenseDatabase.addLicense(request_info, credentials)
        return f'<p>License added<p>'
    else:
        abort(401)

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

@app.get("/seeAllLicenses/")
def seeAllLicenses():
    log.log("INFO", "Request to see all licenses received..")
    success, auth_response = authentication.authorize(request.headers)
    if success:
        # license_request = request.json
        # INTEGRATION: Call backend function
        # credentials = Credentials(auth_response)
        # LicenseDatabase.viewLicenses(request_info, credentials)
        return f'<p>License added<p>'
    else:
        abort(401)

@app.get("/filteredView/")
def filteredView():
    return f'NOT YET IMPLEMENTED'


# Error handlers

# @app.errorhandler(401)
# def handle_401():
#     return f'ERROR: Unable to authenticate user.', 401
