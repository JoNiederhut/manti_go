
import mantigo as mtg


TEST_LEVEL = """
WWWWWWWWWW
W        W
W  mmmmm E
W        W
WWWWWWWWWW"""


def count_manti(game):
    """helper function for counting symbols"""
    return len([m for y, x, m in game.get_symbols() if m == 'm'])


def test_collect_manti():
    """A player can collect Manti"""
    game = mtg.MantiGo(
        time_limit=(0, 3),
        level=TEST_LEVEL,
        player_start=(2, 2)
    )
    # there should be 5 Manti on the map
    assert count_manti(game) == 5
    assert game.status == "running"

    # after moving 5 times, there are no more manti left
    for _ in range(5):
        game.move("right")
    assert count_manti(game) == 0
    assert game.status == "running"

    # collecting 5 manti is enough to exit and win the game
    game.move("right")
    game.move("right")
    assert game.status == "won"
