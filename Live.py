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

    def choose_difficulty_level(difficulty_levels: List[int]) -> int:
        """
        Prompts the player to choose difficulty level from levels list

        :param difficulty_levels: a list of the levels for a particular game to choose from
        :return: The chosen level
        :raise ValueError: If player doesnt provide a an existing level number between the easiest and hardest level
        """
        easiest = difficulty_levels[0]
        hardest = difficulty_levels[-1]

        difficulty_level = int(input(f"Please choose game difficulty from {easiest} to {hardest}:"))
        if not (easiest <= difficulty_level <= hardest):
            raise ValueError(f"Expected game difficulty from {easiest} to {hardest} but got {difficulty_level}")
        if difficulty_level not in difficulty_levels:
            raise ValueError(f"Level {difficulty_level} doesn't exist. Available levels:"+str(difficulty_levels))

        return difficulty_level

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
            chosen_difficulty_level = choose_difficulty_level(chosen_game["difficulty_levels"])
        except ValueError as e:
            print(e)
            continue
        else:
            break

    print(f"You chose to play {chosen_game['name']} at level {chosen_difficulty_level}")
