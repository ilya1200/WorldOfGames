import logging

from Consts import LOGGING_FORMAT, PATH_TO_LOG_FILE
from Live import load_game, welcome

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

    WELCOME_MESSAGE = welcome(PLAYER_NAME)
    logger.debug(WELCOME_MESSAGE)
    print(WELCOME_MESSAGE)

    logger.debug("Game to be loaded")
    load_game()

    logger.info("WoG Finished")
