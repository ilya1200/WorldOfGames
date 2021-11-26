import logging
import random
import time
from typing import List

from Consts import LOGGING_FORMAT, PATH_TO_LOG_FILE

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter(LOGGING_FORMAT)
file_handler = logging.FileHandler(PATH_TO_LOG_FILE)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class MemoryGame:
    """
    The purpose of memory game is to display an amount of random numbers to the users for 0.7
    seconds and then prompt them from the user for the numbers that he remember. If he was right
    with all the numbers the user will win otherwise he will lose.
    """
    TIME_TO_MEMORIZE: float = 0.7

    def __init__(self, difficulty: int):
        self.difficulty: int = difficulty

    def generate_sequence(self) -> List[int]:
        """
        Generates and stores a list size equals difficulty of random values between 1 and 101.
        """
        sequence: List[int] = random.choices(range(1, 102), k=self.difficulty)
        logger.debug(f"Sequence generated: {sequence}")

        return sequence

    def get_list_from_user(self) -> List[int]:
        """
        Get list of values represent the numbers the user remember

        :return: list of the values user remembered
        """
        while True:
            player_input: str = None
            try:
                player_input = input(f"Enter the numbers you remember separated with space:")
                logger.debug(f"Player entered: {player_input}")

                list_from_player: List[int] = list(map(lambda str_value: int(str_value), player_input.split()))
            except ValueError:
                ERR_MSG: str = f"Bad input: expected a list of ints separated by spaces, but got: {player_input}"
                logger.error(ERR_MSG)
                print(ERR_MSG)
                continue
            else:
                logger.debug(f"list_from_player: {list_from_player}")
                return list_from_player

    def is_list_equal(self, first_list: List[int], second_list: List[int]) -> bool:
        """
        Compares to two lists if they are equal.

        :param first_list: First list to compare
        :param second_list: Second list to compare with
        :return: Compare the two lists. Will return True if equal, and False otherwise.
        :rtype: bool
        """
        logger.debug(f"first_list={first_list}")
        logger.debug(f"second_list={second_list}")
        logger.debug(f"Is first_list == second_list : {first_list == second_list}")

        return first_list == second_list

    def play(self) -> bool:
        """
        Run the game

        :return: The result of the game: True- Win, False-Lose
        """
        logger.info("Player is playing MemoryGame")

        sequence_to_memorize: List[int] = self.generate_sequence()
        logger.info(f"A sequence to memorize generated: {sequence_to_memorize}")

        print("Remember the sequence:" + str(sequence_to_memorize))
        time.sleep(MemoryGame.TIME_TO_MEMORIZE)

        list_from_user: List[int] = self.get_list_from_user()
        logger.info(f"Player remembered: {list_from_user}")

        is_win: bool = self.is_list_equal(sequence_to_memorize, list_from_user)

        if is_win:
            logger.info(f"Players sequence is correct {list_from_user}. The sequence was: {sequence_to_memorize}.")
            print(f"Correct! The sequence was: {sequence_to_memorize}")
        else:
            logger.info(f"Players sequence is wrong {list_from_user}. The sequence was: {sequence_to_memorize}.")
            print(f"Wrong! The sequence was: {sequence_to_memorize}, you entered: {list_from_user}")

        logger.info(f"Did player win the game: {is_win}")
        return is_win
