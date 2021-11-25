import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_TO_LOG_FILE = f'{ROOT_DIR}//Logs/wog.log'
LOGGING_FORMAT = '[%(levelno)s %(levelname)s][%(name)s][%(asctime)s][%(process)d %(processName)s %(thread)d %(threadName)s][%(filename)s %(funcName)s %(lineno)d]%(message)s'