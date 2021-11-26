import logging
import random
import threading
from queue import Queue
from threading import Thread
from typing import List

from Consts import LOGGING_FORMAT, PATH_TO_LOG_FILE
from Interfaces.Game import Game

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter(LOGGING_FORMAT)
file_handler = logging.FileHandler(PATH_TO_LOG_FILE)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class GuessGame(Game):
    """
    The purpose of guess game is to start a new game, cast a random number between 1 to a
    variable called difficulty. The game will get a number input from the
    """

    def __init__(self, difficulty: int):
        self.difficulty = difficulty

    def generate_number(self):
        """
        Set a random value between 1 to difficulty to secret_number
        """
        self.secret_number = random.randint(1, self.difficulty)
        logger.debug(f"Generated secret number: {self.secret_number}")

    def get_guess_from_user(self) -> int:
        """
        Prompts the player for guess

        :return: an int in between 1 to difficulty, which represents the user guess
        """
        while True:
            player_input: str = None
            try:
                player_input = input(f"Guess a number between 1 to {self.difficulty}:")
                logger.debug(f'Player input: {player_input}')
                player_guess: int = int(player_input)
                if not 1 <= player_guess <= self.difficulty:
                    raise ValueError(f'Players guess is outside the range from 1 to {self.difficulty}')

            except ValueError:
                ERR_MSG: str = f"Bad input expected a number between 1 to {self.difficulty}, but got {player_input}"
                logger.error(ERR_MSG)
                print(ERR_MSG)
                continue
            else:
                logger.debug(f'Player guess: {player_guess}')
                return player_guess

    def play(self) -> bool:
        """
        Run the game

        :return: The result of the game: True- Win, False-Lose
        """

        logger.info("Player playing GuessGame")
        player_guess: int = None
        que: Queue[int] = Queue()
        threads: List[Thread] = [
            Thread(name="ApplyGuessThread", target=lambda q: q.put(self.get_guess_from_user()), args=(que,)),
            Thread(name="GenerateNumberThread", target=self.generate_number),
        ]

        for thread in threads:
            logger.debug(f"Thread {thread.name} is about to start")
            thread.start()
            logger.debug(f"Thread {thread.ident}-{thread.name} started to run")

        while True:
            alive_threads: List[Thread] = list(filter(lambda thread: thread.is_alive(), threads))
            is_any_thread_alive = any(alive_threads)
            if is_any_thread_alive:
                logger.debug(f"Waiting for these Threads to finish: {list(map(lambda alive_thread: f'{alive_thread.ident}-{alive_thread.name}', alive_threads))}")
                threading.Event().wait(0.5)
            else:
                logger.debug("Done waiting for threads")
                break

        logger.info(f"A secret number generated: {self.secret_number}")
        logger.info(f"Player apply guess: {player_guess}")

        is_win = self.secret_number == player_guess
        if is_win:
            logger.info(f"Players guess {player_guess} is correct.")
        else:
            logger.info(f"Players guess {player_guess} is wrong. The number was: {self.secret_number}.")
            print(f"Wrong guess! The number was: {self.secret_number}")

        logger.info(f"Did player win the game: {is_win}")
        return is_win
