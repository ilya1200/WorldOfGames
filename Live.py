from typing import List, Dict

from Games.CurrencyRouletteGame import CurrencyRouletteGame
from Games.GuessGame import GuessGame
from Games.MemoryGame import MemoryGame


def welcome(name: str) -> str:
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."


def load_game():
    def get_games() -> List[Dict]:
        """
        :return: List of details about all games
        """
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
        if game_number not in range(1, len(games) + 1):
            raise ValueError(f"Expect the chosen game number between 1 and {len(games)}, but got {game_number}")

        game_index = game_number - 1
        return games[game_index]

    def choose_difficulty_level(easiest: int, hardest: int) -> int:
        """
        Prompts the player to choose difficulty level from levels list

        :param easiest: The easiest level of the game
        :param hardest: The hardest level of the game
        :return: The chosen level
        :raise ValueError: If player doesnt provide a number that represent a level between the easiest(include) and hardest(include) level
        """

        difficulty_level = int(input(f"Please choose game difficulty from {easiest} to {hardest}:"))
        if not (easiest <= difficulty_level <= hardest):
            raise ValueError(f"Expected game difficulty from {easiest} to {hardest} but got {difficulty_level}")

        return difficulty_level

    game_over_messages = {
        "win": "Congrats! You win!",
        "lose": "Game lost"
    }

    all_games = get_games()
    chosen_game = None
    chosen_difficulty_level = None
    while True:
        try:
            chosen_game = choose_game(all_games)
        except ValueError as e:
            print(e)
            continue
        else:
            break

    while True:
        try:
            chosen_difficulty_level = choose_difficulty_level(chosen_game["easiest_level"],
                                                              chosen_game["hardest_level"])
        except ValueError as e:
            print(e)
            continue
        else:
            break

    print(f"You chose to play {chosen_game['name']} at level {chosen_difficulty_level}")
    game = None
    if chosen_game['name'] == "Memory Game":
        game = MemoryGame(chosen_difficulty_level)
    elif chosen_game['name'] == "Guess Game":
        game = GuessGame(chosen_difficulty_level)
    elif chosen_game['name'] == "Currency Roulette":
        game = CurrencyRouletteGame(chosen_difficulty_level)
    else:
        raise ValueError(f"The game:{chosen_game['name']} is undefined")

    is_win = game.play()
    game_status = "win" if is_win else "lose"
    print(game_over_messages[game_status])

