import logging

from Consts import ROOT_DIR
from Live import load_game, welcome

PATH_TO_LOG_FILE = f'{ROOT_DIR}//Logs/wog.log'
LOGGER_FORMAT = '[%(levelno)s %(levelname)s][%(asctime)s][%(process)d %(processName)s %(thread)d %(threadName)s][%(filename)s %(lineno)d]%(message)s'

logging.basicConfig(filename=PATH_TO_LOG_FILE, level=logging.DEBUG,
                    format=LOGGER_FORMAT)

if __name__ == '__main__':
    PLAYER_NAME = "Ilya"
    logging.debug(f"Player name {PLAYER_NAME}")

    WELCOME_MESSAGE = welcome(PLAYER_NAME)
    logging.info(WELCOME_MESSAGE)
    print(WELCOME_MESSAGE)

    logging.info("Game to be loaded")
    load_game()

    logging.info("WoG Finished")
