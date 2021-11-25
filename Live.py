import logging
from typing import List, Dict

from Consts import LOGGING_FORMAT, PATH_TO_LOG_FILE
from Games.CurrencyRouletteGame import CurrencyRouletteGame
from Games.GuessGame import GuessGame
from Games.MemoryGame import MemoryGame

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter(LOGGING_FORMAT)
file_handler = logging.FileHandler(PATH_TO_LOG_FILE)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def welcome(name: str) -> str:
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."


def load_game():
    def get_games() -> List[Dict]:
        """
        :return: List of details about all games
        """
        logger.debug("Trying to get games")
        games = [
            {
                "name": "Memory Game",
                "description": "a sequence of numbers will appear for 1 second and you have to\nguess it back",
                "easiest_level": 1,
                "hardest_level": 5
            },
            {
                "name": "Guess Game",
                "description": "guess a number and see if you chose like the computer",
                "easiest_level": 1,
                "hardest_level": 5
            },
            {
                "name": "Currency Roulette",
                "description": "Currency Roulette - try\nand guess the value of a random amount of USD in ILS",
                "easiest_level": 1,
                "hardest_level": 5
            }
        ]
        logger.debug(str(games))
        return games

    def choose_game(games: List[Dict]) -> dict:
        """
        Prompts the player to choose a game by number: 1,2,3,etc...

        :param games: The details for the games
        :return: The chosen game data
        :raise ValueError: If invalid or not existing game number provided by player
        """
        player_prompt = "Please choose a game to play:\n"
        for index, game in enumerate(games):
            game_number = index + 1
            player_prompt += f"\t{game_number}.{game['name']} - {game['description']}\n"

        game_number = int(input(player_prompt))
        logger.debug(f'Player ask for game number: {game_number}')

        if game_number not in range(1, len(games) + 1):
            ERR_MSG = f"Expect the chosen game number between 1 and {len(games)}, but got {game_number}"
            logger.error(ERR_MSG)
            raise ValueError(ERR_MSG)

        game_index = game_number - 1
        CHOSEN_GAME = games[game_index]
        logger.debug(f'A game with the requested number: {game_number} is found {CHOSEN_GAME}')

        return CHOSEN_GAME

    def choose_difficulty_level(easiest: int, hardest: int) -> int:
        """
        Prompts the player to choose difficulty level from levels list

        :param easiest: The easiest level of the game
        :param hardest: The hardest level of the game
        :return: The chosen level
        :raise ValueError: If player doesnt provide a number that represent a level between the easiest(include) and hardest(include) level
        """

        difficulty_level = int(input(f"Please choose game difficulty from {easiest} to {hardest}:"))
        logger.debug(f'Player request for difficulty level: {difficulty_level}')

        if not (easiest <= difficulty_level <= hardest):
            ERR_MSG = f"Expected game difficulty from {easiest} to {hardest} but got {difficulty_level}"
            logger.error(ERR_MSG)
            raise ValueError(ERR_MSG)

        logger.debug(f'Player chose difficulty level: {difficulty_level}')
        return difficulty_level

    chosen_game = None
    chosen_difficulty_level = None
    game_menu = {
        "Currency Roulette": CurrencyRouletteGame,
        "Guess Game": GuessGame,
        "Memory Game": MemoryGame
    }
    game_over_messages = {
        "win": "Congrats! You win!",
        "lose": "Game lost"
    }

    all_games = get_games()
    logger.debug(f'Games data: {all_games}')

    logger.info(f"Prompt player to choose game from {list(map(lambda game: game['name'], all_games))}")
    while True:
        try:
            chosen_game = choose_game(all_games)
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
            chosen_difficulty_level = choose_difficulty_level(chosen_game["easiest_level"],
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
        game = game_menu[chosen_game['name']](chosen_difficulty_level)
    except KeyError:
        logger.error(f"The game:{chosen_game['name']} is not mapped to a game object in the dict games_menu")
        raise KeyError(f"The game:{chosen_game['name']} is undefined")
    else:
        logger.info(f"Player is about to play:{chosen_game['name']}")

    is_win = game.play()
    game_status = "win" if is_win else "lose"

    logger.info(f"Player finished and {game_status} the game {chosen_game['name']}")
    logger.debug(f"Player should see the message: {game_over_messages[game_status]}")
    print(game_over_messages[game_status])
