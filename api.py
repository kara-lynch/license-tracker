from flask import Flask, request, abort
from src.logger import log
from src.util import authentication 

log.log("INFO", "REST API started.")

app = Flask(__name__)

@app.get("/hello_world/")
def hello():
    return f'<p>Hello!</p>'

@app.post("/addLicense/")
def addLicense():
    log.log("INFO", "Request to add license received.")
    license_request = request.json
    success, auth_response = authentication.authorize(request.headers)
    if success:
        # INTEGRATION: Call backend function
        # credentials = Credentials(auth_response)
        # request_info = AddLicReq(auth_response)
        # LicenseDatabase.addLicense(request_info, credentials)
        return f'<p>License added'
    else:
        abort(401)

@app.post("/deleteLicense/")
def deleteLicense():
    return f'<p>Hello! {request.view_args}</p>'

@app.post("/updateLicense/")
def updateLicense():
    return f'<p>Hello! {request.view_args}</p>'


# Query methods

@app.get("/")
def help_screen():
    return f'NOT YET IMPLEMENTED'

@app.get("/seeAllLicenses/")
def seeAllLicenses():
    return f'NOT YET IMPLEMENTED'

@app.get("/filteredView/")
def filteredView():
    return f'NOT YET IMPLEMENTED'


# Error handlers

@app.errorhandler(401)
def handle_401():
    return f'ERROR: Unable to authenticate user.', 401