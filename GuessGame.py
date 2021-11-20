import random


class GuessGame:
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

    def get_guess_from_user(self) -> int:
        """
        Prompts the player for guess

        :return: an int in between 1 to difficulty, which represents the user guess
        """
        while True:
            try:
                player_guess = int(input(f"Guess a number between 1 to {self.difficulty}:"))
            except ValueError as e:
                print(f"Bad input expected a number between 1 to {self.difficulty}")
                continue
            else:
                return player_guess

    def play(self) -> bool:
        """
        Run the game

        :return: The result of the game: True- Win, False-Lose
        """
        self.generate_number()
        player_guess = self.get_guess_from_user()
        game_result = self.secret_number == player_guess
        if not game_result:
            print(f"Wrong guess! The number was: {self.secret_number}")
        return game_result
