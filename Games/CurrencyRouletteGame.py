import logging
import random
import requests
from typing import Tuple, Dict

from requests import Response

from Consts import LOGGING_FORMAT, PATH_TO_LOG_FILE

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter(LOGGING_FORMAT)
file_handler = logging.FileHandler(PATH_TO_LOG_FILE)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class CurrencyRouletteGame:
    """
    This game will use t he free currency api to get the current exchange rate from USD to ILS, will
    generate a new random number between 1-100 a will ask the user what he thinks is the value of
    the generated number from USD to ILS, depending on the user’s difficulty his answer will be
    correct if the guessed value is between the interval surrounding the correct answer
    """

    def __init__(self, difficulty: int):
        self.difficulty: int = difficulty

    def _get_currency_rate(self, from_currency: str, to_currency: str) -> float:
        """
        Generates the conversion rate between the specified currencies

        :param from_currency: The currency to be converted
        :param to_currency: The currency to convert to
        :return: The currency rate between the specified currencies. Rounded to 2 digits after decimal point.
        """
        logger.debug(f"from_currency:{from_currency}")
        logger.debug(f"to_currency:{to_currency}")

        RATES_API_URL: str = f'https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}'

        logger.debug(f"Getting rates from RATES_API at URL: {RATES_API_URL}")
        response: Response = requests.get(RATES_API_URL)
        rates: Dict[str] = response.json()['rates']

        currency_rate: float = round(float(rates[to_currency.upper()]), 2)
        logger.debug(f"Form currency {from_currency} to currency {to_currency} the rate: {currency_rate}")

        return currency_rate

    def get_money_interval(self, amount: int, currency_rate: float) -> Tuple[float, float]:
        """
        Generates an interval represented by a tuple, the first value is the lowest value and the second is the highest value.

        :param amount: the amount of money to be converted to different currency
        :param currency_rate: the conversion rate
        :return: The tuple with the values
        """
        logger.debug(f'amount: {amount}')
        logger.debug(f'currency_rate: {currency_rate}')

        d: int = self.difficulty
        logger.debug(f'd: {d}')

        t: float = amount * currency_rate
        logger.debug(f't: {t}')

        interval: Tuple[float, float] = t - (5 - d), t + (5 - d)
        logger.debug(f'calculated interval: {interval}')

        return interval

    def get_guess_from_user(self, amount_to_be_converted: int) -> float:
        """
        Prompts the player for guess

        :param amount_to_be_converted: Represents the amount of money to be converted to a different currency the new amount of which the user will be prompted gess
        :return: a float which represents the user guess rounded to 2 numbers after the decimal point
        """

        while True:
            player_input: str = None
            try:
                player_input = input(f"If I to convert USD {amount_to_be_converted} to ILS, I will get :")
                logger.debug(f'Player input: {player_input}')
                player_guess: float = round(float(player_input), 2)
            except ValueError:
                ERR_MSG = f"Bad input expected a float with 2 digits, but got: {player_input}"
                logger.error(ERR_MSG)
                print(ERR_MSG)
                continue
            else:
                logger.debug(f'Player guess rounded: {player_guess}')
                return player_guess

    def play(self) -> bool:
        """
        Run the game

        :return: The result of the game: True- Win, False-Lose
        """

        logger.info("Player playing CurrencyRouletteGame")
        FROM_CURRENCY: str = "USD"
        TO_CURRENCY: str = "ILS"

        CURRENCY_RATE: float = self._get_currency_rate(FROM_CURRENCY, TO_CURRENCY)
        logger.info(f"Got the conversion rate from {FROM_CURRENCY} to {TO_CURRENCY} it is {CURRENCY_RATE}")

        AMOUNT: int = random.randint(1, 100)
        logger.debug(f"AMOUNT: {AMOUNT}")

        money_interval: tuple = self.get_money_interval(AMOUNT, CURRENCY_RATE)
        logger.info(f"A money interval generated: {money_interval}")

        player_guess: float = self.get_guess_from_user(AMOUNT)
        logger.info(f"Player apply guess: {player_guess}")

        is_win: bool = money_interval[0] <= player_guess <= money_interval[1]
        if is_win:
            logger.info(f"Players guess {player_guess} is correct. It is inside interval {money_interval}")
            print(f"Your guess {player_guess} is correct!")
        else:
            logger.info(f"Players guess {player_guess} is wrong. It is outside interval: {money_interval}.")
            print(f"Wrong guess! Your guess {player_guess} is not in the interval: {money_interval}.")

        logger.info(f"Did player win the game: {is_win}")
        return is_win
