import random
from typing import Tuple


class CurrencyRouletteGame:
    """
    This game will use t he free currency api to get the current exchange rate from USD to ILS, will
    generate a new random number between 1-100 a will ask the user what he thinks is the value of
    the generated number from USD to ILS, depending on the user’s difficulty his answer will be
    correct if the guessed value is between the interval surrounding the correct answer
    """

    def __init__(self, difficulty: int):
        self.difficulty = difficulty

    def get_money_interval(self, currency_rate: float) -> Tuple[float, float]:
        d = self.difficulty
        t = self.usd_amount * currency_rate
        return t - (5 - d), t + (5 - d)

    def get_guess_from_user(self) -> float:
        while True:
            try:
                player_guess = round(float(input(f"If I to convert USD {self.usd_amount} to ILS, I will get :")), 2)
            except ValueError as e:
                print(f"Bad input expected a float with 2 digits")
                continue
            else:
                return player_guess

    def play(self):
        self.usd_amount = random.randint(1, 100)
        USD_TO_ILS_RATE = 3.5

        money_interval = self.get_money_interval(USD_TO_ILS_RATE)
        user_guess = self.get_guess_from_user()
        return user_guess in money_interval

