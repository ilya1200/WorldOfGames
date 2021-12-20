import logging
from Consts import LOGGING_FORMAT, PATH_TO_LOG_FILE

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter(LOGGING_FORMAT)
file_handler = logging.FileHandler(PATH_TO_LOG_FILE)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


SCORES_FILE_NAME: str = "Scores.txt"
BAD_RETURN_CODE: int = -1


def screen_cleaner() -> None:
    """

    A function to clear the screen
    """
    print('\r', '', end='')
    logger.debug("Screen cleared")
