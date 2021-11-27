from typing import List, Dict, Any

import pytest

from Live import Live


@pytest.mark.parametrize(
    "name",
    [

        ("ilya",),
        ("Jack",),
        ("Gil",)
    ])
def test_welcome(name: str):
    expected_welcome_msg: str = f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."
    actual_welcome_msg: str = Live.welcome(name)
    assert (actual_welcome_msg, expected_welcome_msg)  # add assertion here


def test_get_games():
    expected_games: List[str] = ["Memory Game", "Guess Game", "Currency Roulette"]
    games: List[Dict[str, Any]] = Live._get_games()

    assert games is not None
    assert type(games) == list

    actual_games_list: List[str] = list(map(lambda game: game['name'], games))
    assert actual_games_list == expected_games
