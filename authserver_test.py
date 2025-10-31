import requests

from src.logger import log

if __name__ == "__main__":
    print("Beginning authorization test.")
    log.log("INFO", "Begin authorization test.")

    PING_URL = "http://172.16.0.51:8080/auth_service/api/auth/ping"

    # Ping server to make sure it is up
    log.log("INFO", "Pinging authorization server...")
    ping_response = requests.get(PING_URL)
    if ping_response.status_code == 200:
        log.log("INFO", "Ping successful; server is up.")
    else:
        log.log("ERROR", "Ping failed, server is down.")
        exit(1)    
    
    print("Ping successful, continuing test.")
    test_user = {
    "first_Name": "Joleen",
    "location": "Japan",
    "id": 658,
    "last_Name": "Fishbie",
    "department": "Legal",
    "title": "Manager",
    "token": "eyJhbGciOiJIUzI1NiJ9.eyJsYXN0X25hbWUiOiJGaWxpcGN6eW5za2kiLCJsb2NhdGlvbiI6Ikdlcm1hbnkiLCJpZCI6MTksImRlcGFydG1lbnQiOiJJbmZvcm1hdGlvbiBUZWNobm9sb2d5IiwidGl0bGUiOiJEZXZlbG9wZXIiLCJmaXJzdF9uYW1lIjoiTWFyZ2l0Iiwic3ViIjoiTWFyZ2l0IEZpbGlwY3p5bnNraSIsImlhdCI6MTc2MTg1OTEyMywiZXhwIjoxNzYxODYyNzIzfQ._tdhgRBwgO5qJs2Ipb1TDxNVvorUQUlMaNG361Q8p7I"
    }
    token = test_user["token"]

    POST_URL = "http://172.16.0.51:8080/auth_service/api/auth/verify"
    BODY = {"token": token}
    log.log("INFO", "Begin testing token authentication.")
    post_response = requests.post(POST_URL, json=BODY)
    if post_response.status_code == 201:
        log.log("INFO", "Token authenticated successfully.")
        print(post_response.text)
    else:
        log.log("ERROR", "Token failed authentication!")
        print(post_response)
        exit(1)

    log.log("INFO", "Ending test.")
