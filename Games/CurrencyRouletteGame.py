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

    def _get_rate(self, from_currency: str, to_currency: str) -> float:
        logger.debug(f"from_currency:{from_currency}")
        logger.debug(f"to_currency:{to_currency}")

        RATES_API_URL: str = f'https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}'

        logger.debug(f"Getting rates from RATES_API at URL: {RATES_API_URL}")
        response: Response = requests.get(RATES_API_URL)
        rates: Dict[str] = response.json()['rates']

        rate: float = round(float(rates[to_currency.upper()]), 2)
        logger.debug(f"Form currency {from_currency} to currency {to_currency} the rate: {rate}")

        return rate

    def get_money_interval(self, amount: int, currency_rate: float) -> Tuple[float, float]:
        logger.debug(f'amount: {amount}')
        logger.debug(f'currency_rate: {currency_rate}')

        d: int = self.difficulty
        logger.debug(f'd: {d}')

        t: float = amount * currency_rate
        logger.debug(f't: {t}')

        interval: Tuple[float, float] = t - (5 - d), t + (5 - d)
        logger.debug(f'calculated interval: {interval}')

        return interval

    def get_guess_from_user(self, amount: int) -> float:
        while True:
            player_input: str = None
            try:
                player_input = input(f"If I to convert USD {amount} to ILS, I will get :")
                logger.debug(f'Player input: {player_input}')
                player_guess: float = round(float(player_input), 2)
            except ValueError:
                ERR_MSG = f"Bad input expected a float with 2 digits, but got: {player_input}"
                logger.error(ERR_MSG)
                print(ERR_MSG)
                continue
            else:
                logger.debug(f'Player guess: {player_guess}')
                return player_guess

    def play(self) -> bool:
        logger.info("Player playing CurrencyRouletteGame")

        CURRENCY_RATE: float = self._get_rate("USD", "ILS")
        logger.debug(f"Currency rate: {CURRENCY_RATE}")

        AMOUNT: int = random.randint(1, 100)
        logger.debug(f"AMOUNT: {AMOUNT}")

        money_interval: tuple = self.get_money_interval(AMOUNT, CURRENCY_RATE)
        logger.info(f"A money interval generated: {money_interval}")

        player_guess: float = self.get_guess_from_user(AMOUNT)
        logger.info(f"Player apply guess: {player_guess}")

        is_win: bool = money_interval[0] <= player_guess <= money_interval[1]
        if is_win:
            logger.info(f"Players guess {player_guess} is correct.")
            print(f"Your guess {player_guess} is correct!")
        else:
            logger.info(f"Players guess {player_guess} is wrong. The interval was: {money_interval}.")
            print(f"Wrong guess! Your guess {player_guess} is not in the interval: {money_interval}.")

        logger.info(f"Did player win the game: {is_win}")
        return is_win
