import os
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_TO_LOG_FILE = f'{ROOT_DIR}//Logs/wog_{datetime.now().strftime("%a-%d-%m-%y_%H:%M:%S")}.log'
LOGGING_FORMAT = '[%(levelno)s %(levelname)s][%(name)s][%(asctime)s][%(process)d %(processName)s %(thread)d %(threadName)s][%(filename)s %(funcName)s %(lineno)d]::\t%(message)s'
PATH_TO_GAMES_JSON = f"{ROOT_DIR}//games.json"
