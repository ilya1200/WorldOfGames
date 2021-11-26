import logging
from Live import Live

from Consts import LOGGING_FORMAT, PATH_TO_LOG_FILE

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter(LOGGING_FORMAT)
file_handler = logging.FileHandler(PATH_TO_LOG_FILE)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

if __name__ == '__main__':
    logger.info("WoG Run")

    PLAYER_NAME = "Ilya"
    logger.debug(f"Player name {PLAYER_NAME}")

    WELCOME_MESSAGE = Live.welcome(PLAYER_NAME)
    logger.debug(WELCOME_MESSAGE)
    print(WELCOME_MESSAGE)

    logger.debug("Game to be loaded")
    Live.load_game()

    logger.info("WoG Finished")
