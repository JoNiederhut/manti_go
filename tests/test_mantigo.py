"""
We want to write a program that checks wether Manti Go! works.
We will use pytest.

TDD Cycle (Test Driven Development)

0. Hypothesis: the program is working
1. Write a test that fails (disprove the hypothesis)
2. Change the code so that the test passes (re-establish the hypothesis)
3. repeat
"""

import time
import mantigo as mtg
import pytest


TEST_LEVEL = """
WWWWWWWWWW
W       EW
W        W
W        W
W     m  W
W m      W
WWWWWWWWWW
"""


def count_symbols(game, symbol):
    """helper function for counting symbols"""
    return len([s for y, x, s in game.get_symbols() if s == symbol])


def get_player_position(game):
    """helper function finding the player symbol"""
    for y, x, symbol in game.get_symbols():
        if symbol == 'player':
            return y, x


@pytest.fixture
def game():
    """helper function preparing a MantiGo object for testing"""
    return mtg.MantiGo(
        time_limit=(0, 2),  # 0 min 2 sec
        level=TEST_LEVEL,
        player_start=(2, 2)
    )


def test_mantigo_timer(game):
    """Waiting for too long loses the game"""
    assert game.status == "running"
    time.sleep(2.1)
    assert game.status == "Game Over"


def test_get_symbols(game):
    """The get_symbols method returns a long list of symbols"""
    # count symbols on the test map
    assert count_symbols(game, 'W') == 34
    assert count_symbols(game, 'E') == 1
    assert count_symbols(game, 'm') == 2
    assert count_symbols(game, 'player') == 1
    # do not count enemies, because they are placed randomly


def test_player_move(game):
    """Moving changes the player position"""
    assert get_player_position(game) == (2, 2)
    game.move("right")
    assert get_player_position(game) == (2, 3)
    game.move("down")
    assert get_player_position(game) == (3, 3)
    game.move("left")
    assert get_player_position(game) == (3, 2)
    game.move("up")
    assert get_player_position(game) == (2, 2)


def test_player_move_into_wall(game):
    """When there is a wall, no movement is possible"""
    assert get_player_position(game) == (2, 2)
    game.move("left")
    assert get_player_position(game) == (2, 2)


def test_update(game):
    """update() can be called. Not testing details here"""
    game.update()
