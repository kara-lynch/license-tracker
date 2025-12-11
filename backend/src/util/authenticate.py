import requests
import json

from src.logger import log
from src.config.settings import Settings

class _Authenticate(object):
    """
    Class that encapsulates security token authentication actions.

    The class is responsible for stripping the security token, validating it, and sending it to the authorization server.
    """
    def __init__(self) -> None:
        """
        Constructor for Authenticate object. Pings the authorization to make sure it is responsive.
        """

        log.log("DEBUG", "Loading API config.")
        config_path = Settings.api_config_file()
        with open(config_path, "r") as file:
            config_json = json.load(file)
        _ping_url = config_json["PING_URL"]
        self._auth_url = config_json["AUTH_URL"]

        # Ping Authorization Server to make sure it is up
        log.log("INFO", "Pinging authorization server.")
        ping_response = requests.get(_ping_url)
        if ping_response.status_code == 200:
            log.log("INFO", "Ping successful; authorization server is up.")
        else:
            log.log("ERROR", "Ping failed; server is down.")
            raise RuntimeError("Authentication server is unavailable at this time.")
        
    
    def _validate_token(self, headers) -> tuple[bool, str]:
        """
        Internal method for sanity checking a provided token.

        Tests:
            1. Is token present (not NULL)?
            2. Is token too large?
            3. Is token too small?

        :param headers: Headers stripped from HTTP request

        :return: If true, token was validated
        :rtype: boolean

        :return: Contains the stripped authorization token
        :rtype: str
        """
        # Extract token
        token = headers.get("Bearer")
        if token is None:
            log.log("WARNING", "Request has no authorization token attached.")
            return False, None

        # TODO: ADD LENGTH CHECKING
        if len(token) < 250:
            log.log("WARNING", "Provided security token was too short.")
            return False, None
        elif len(token) > 400:
            log.log("WARNING", "Provided security token was too long.")
            return False, None
        
        return True, token
    
    
    def authorize(self, headers) -> tuple[bool, str]:
        """
        Public method for calling authorization server.

        :param headers: Headers from incoming HTTP request, should contain authorization token

        :return: True if successfully authenticated, False otherwise
        :rtype: bool 

    
        :return: The credentials associated with the token
        :rtype: str 
        """
        log.log("INFO", "Beginning authorization process.")
        valid_token, token = self._validate_token(headers)
        if not valid_token:
            log.log("ERROR", "Invalid authorization token provided.")
            return False, None
        
        body = {"token": token}
        log.log("INFO", "Calling authentication server.")
        print(body)
        auth_response = requests.post(self._auth_url, json=body)
        if auth_response.status_code == 201:
            log.log("INFO", "Token authenticatd successfully.")
            return True, auth_response.text
        else:
            log.log("ERROR", "Token failed authorization.")
            return False, None

        