import logging.config
import pathlib
import json

from enum import Enum
from inspect import getframeinfo, stack

"""
Enum for storing logger levels, in order of increasing severity.
"""
class Level(Enum):
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4

class _Logger(object):

    """
    Constructor. Loads logger settings JSON file from config folder to initialize logger.
    """
    def __init__(self) -> None:
        config_path = "./src/config/logger.json"

        with open(config_path, "r") as file:
            config_json = json.load(file)

        logging.config.dictConfig(config_json)

        self.logger = logging.getLogger()

    """
    Method for writing to logs. 

    Log levels are (in order of increasing severity):
        DEBUG
        INFO
        WARNING
        ERROR
        CRITICAL

    Levels stored in Level enum. Default level is INFO.

    :param level: Level of the input log
    :param msg: The message to display in the log
    :return: None
    """
    def log(self, level: Level, msg: str) -> None:
        # GET FRAME INFO? ASK LATER
        # FRAME INFO USED TO DISPLAY WHERE IN CODE LOG COMES FROM
        caller = getframeinfo(stack()[1][0]) # The path in the project where the call came from
        path = pathlib.PurePath(caller.filename)
        parts = path.parts # Split filepath into list of directories
        start = parts.index("license-tracker")
        packageName = "/".join(parts[start:-1])
        output = "{}/{}/{}:{} - {}".format(packageName, path.stem, caller.function, caller.lineno, msg)
        

        if level == Level.DEBUG.name:
            self.logger.debug(output)
        elif level == Level.INFO.name:
            self.logger.info(output)
        elif level == Level.WARNING.name:
            self.logger.warning(output)
        elif level == Level.ERROR.name:
            self.logger.error(output)
        elif level == Level.CRITICAL.name:
            self.logger.critical(output)
        else:
            self.logger.info(output)
