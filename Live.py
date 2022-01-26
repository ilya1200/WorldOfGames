import json
import logging
from typing import List, Dict, Any

from Consts import LOGGING_FORMAT, PATH_TO_LOG_FILE, PATH_TO_GAMES_JSON
from CurrencyRouletteGame import CurrencyRouletteGame
from GuessGame import GuessGame
from MemoryGame import MemoryGame
from Interfaces.Game import Game
from Score import Score

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter(LOGGING_FORMAT)
file_handler = logging.FileHandler(PATH_TO_LOG_FILE)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class Live:
    _game_menu: Dict[str, Game.__class__] = {
        "Currency Roulette": CurrencyRouletteGame,
        "Guess Game": GuessGame,
        "Memory Game": MemoryGame
    }
    _game_over_messages = {
        "win": "Congrats! You win!",
        "lose": "Game lost"
    }

    @staticmethod
    def welcome(name: str) -> str:
        return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."

    @staticmethod
    def _get_games() -> List[Dict[str, Any]]:
        """
        :return: List of details about all games
        """

        games: List[Dict[str, Any]] = list()
        logger.debug("Trying to get games")
        with open(PATH_TO_GAMES_JSON) as games_json:
            logger.debug(f"Opened file: {PATH_TO_GAMES_JSON}")
            games = json.loads(games_json.read())

            logger.debug(f"Retrieved games from file: {PATH_TO_GAMES_JSON}")
            logger.debug(f"Games Details:{games}")
        return games

    @staticmethod
    def _choose_game(games: List[Dict]) -> dict:
        """
        Prompts the player to choose a game by number: 1,2,3,etc...

        :param games: The details for the games
        :return: The chosen game data
        :raise ValueError: If invalid or not existing game number provided by player
        """
        player_prompt: str = "Please choose a game to play:\n"
        for index, game in enumerate(games):
            game_number = index + 1
            player_prompt += f"\t{game_number}.{game['name']} - {game['description']}\n"

        player_input: str = input(player_prompt)
        logger.debug(f'Player input: {player_input}')

        game_number: int = int(player_input)
        logger.debug(f'Player ask for game number: {game_number}')

        if game_number not in range(1, len(games) + 1):
            ERR_MSG = f"Expect the chosen game number between 1 and {len(games)}, but got {game_number}"
            logger.error(ERR_MSG)
            raise ValueError(ERR_MSG)

        game_index: int = game_number - 1
        CHOSEN_GAME: dict = games[game_index]
        logger.debug(f'A game with the requested number: {game_number} is found {CHOSEN_GAME}')

        return CHOSEN_GAME

    @staticmethod
    def _choose_difficulty_level(easiest: int, hardest: int) -> int:
        """
        Prompts the player to choose difficulty level from levels list

        :param easiest: The easiest level of the game
        :param hardest: The hardest level of the game
        :return: The chosen level
        :raise ValueError: If player doesnt provide a number that represent a level between the easiest(include) and hardest(include) level
        """
        difficulty_level_input: str = input(f"Please choose game difficulty from {easiest} to {hardest}:")
        logger.debug(f'Player input for difficulty level: {difficulty_level_input}')

        difficulty_level: int = int(difficulty_level_input)
        logger.debug(f'Player request for difficulty level: {difficulty_level}')

        if not (easiest <= difficulty_level <= hardest):
            ERR_MSG: str = f"Expected game difficulty from {easiest} to {hardest} but got {difficulty_level}"
            logger.error(ERR_MSG)
            raise ValueError(ERR_MSG)

        logger.debug(f'Player chose difficulty level: {difficulty_level}')
        return difficulty_level

    @staticmethod
    def load_game():
        logger.info(f'Games is loading...')

        chosen_game: dict = dict()
        chosen_difficulty_level: int = -1
        game: Game = None

        all_games: List[Dict[str, Any]] = Live._get_games()
        logger.debug(f'Games data: {all_games}')

        logger.info(f"Prompt player to choose game from {list(map(lambda game: game['name'], all_games))}")
        while True:
            try:
                chosen_game = Live._choose_game(all_games)
            except ValueError as e:
                logger.error(f'Player failed to choose a game, because of invalid input')
                print(e)
                continue
            else:
                logger.info(f"Player chose the game: {chosen_game['name']}")
                break

        logger.info(
            f"Prompt player to choose difficulty level from {chosen_game['easiest_level']} to {chosen_game['hardest_level']}")
        while True:
            try:
                chosen_difficulty_level = Live._choose_difficulty_level(chosen_game["easiest_level"],
                                                                  chosen_game["hardest_level"])
            except ValueError as e:
                logger.error(
                    f'Player failed to choose a difficulty level, because of invalid input')
                print(e)
                continue
            else:
                logger.info(f'Player chose difficulty level: {chosen_difficulty_level}')
                break

        try:
            game = Live._game_menu[chosen_game['name']](chosen_difficulty_level)
        except KeyError:
            logger.error(f"The game:{chosen_game['name']} is not mapped to a game object in the dict games_menu")
            raise KeyError(f"The game:{chosen_game['name']} is undefined")
        else:
            logger.info(f"Player is about to play:{chosen_game['name']}")

        is_win: bool = game.play()
        game_status: str = "win" if is_win else "lose"

        logger.info(f"Player finished and {game_status} the game {chosen_game['name']}")
        logger.debug(f"Player should see the message: {Live._game_over_messages[game_status]}")
        print(Live._game_over_messages[game_status])

        if is_win:
            Score.add_score(chosen_difficulty_level)
            logger.debug(f"Player won a game with difficulty: {chosen_difficulty_level}.Added score to player ")
