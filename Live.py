from typing import List, Dict


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
                "description": "a sequence of numbers will appear for 1 second and you have to guess it back",
                "difficulty_levels": [1, 2, 3, 4, 5]
            },
            {
                "name": "Guess Game",
                "description": "guess a number and see if you chose like the computer",
                "difficulty_levels": [1, 2, 3, 4, 5]
            },
            {
                "name": "Currency Roulette",
                "description": "try and guess the value of a random amount of USD in ILS",
                "difficulty_levels": [1, 2, 3, 4, 5]
            }
        ]
        return games

    def choose_game(games: List[Dict]) -> dict:
        player_prompt = "Please choose a game to play:\n"
        for index, game in enumerate(games):
            game_number = index + 1
            player_prompt += f"\t{game_number}.{game['name']} - {game['description']}\n"

        game_number = int(input(player_prompt))

        game_index = game_number - 1
        return games[game_index]

    def choose_difficulty_level(difficulty_levels: List[int]) -> int:
        easiest = difficulty_levels[0]
        hardest = difficulty_levels[-1]
        difficulty_level = int(input(f"Please choose game difficulty from {easiest} to {hardest}:"))
        return difficulty_level

    games = get_games()
    chosen_game = choose_game(games)
    chosen_difficulty_level = choose_difficulty_level(chosen_game["difficulty_levels"])
    print(f"You chose to play:{chosen_game['name']} at level:{chosen_difficulty_level}")


