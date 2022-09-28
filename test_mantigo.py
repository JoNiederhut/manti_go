"""
We want to write a program that checks wether Manti Go! works.
We will use pytest.

TDD Cycle (Test Driven Development)

0. Hypothesis: the program is working
1. Write a test that fails (disprove the hypothesis)
2. Change the code so that the test passes (re-establish the hypothesis)
3. repeat
"""

from logging import _Level
import time
from webbrowser import get
import mantigo as mtg

def test_mantigo_class():
    game= mtg.MantiGo()

def test_mantigo_timer():
    game = mtg.MantiGo(time_limit=(0,2)) # 0 min 2 sec
    assert game.status == "running"
    time.sleep(2.1)
    assert game.status == "Game Over"


TEST_LEVEL = """
WWWWWWWWWW
W        W
W        W
W        W
W        W
W        W
WWWWWWWWWW
""".strip().split("\n")


def test_player_move():
    game= mtg.MantiGo(
        time_limit=(0,1),
        level=TEST_LEVEL,
        player_start=(3,3)
    )
    assert game.get_map() == """
WWWWWWWWWW
W        W
W        W
W  P     W
W        W
W        W
WWWWWWWWWW
"""
    game.player_command("right")
    assert game.get_map() == """
WWWWWWWWWW
W        W
W        W
W   P    W
W        W
W        W
WWWWWWWWWW
"""