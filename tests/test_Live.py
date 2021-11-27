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
    assert(actual_welcome_msg, expected_welcome_msg)  # add assertion here
