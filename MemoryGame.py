import random
from typing import List


class MemoryGame:
    """
    The purpose of memory game is to display an amount of random numbers to the users for 0.7
    seconds and then prompt them from the user for the numbers that he remember. If he was right
    with all the numbers the user will win otherwise he will lose.
    """

    def __init__(self, difficulty: int):
        self.difficulty = difficulty

    def generate_sequence(self):
        """
        Generates and stores a list size equals difficulty of random values between 1 and 101.
        """
        self.sequence = random.choices(range(1, 102), k=self.difficulty)

    def get_list_from_user(self) -> List[int]:
        pass

    def is_list_equal(self, first_list: List[int], second_list: List[int]) -> bool:
        """

        :return: Compare the two lists. Will return True if equal, and False otherwise.
        :rtype: bool
        """
        return first_list == second_list

    def play(self):
        """
        Run the game

        :return: The result of the game: True- Win, False-Lose
        """
        self.generate_sequence()
        list_from_user = self.get_list_from_user()
        return self.is_list_equal(self.sequence, list_from_user)
