


def test_import_mantigo():
    import mantigo


def test_mantigo_class():
    import mantigo
    game = mantigo.MantiGo()

def test_mantigo_timer():
    import mantigo
    import time
    game = mantigo.MantiGo(time_limit=(0,2))
    assert game.status == "running"
    time.sleep(2.1)
    assert game.status == "Game Over"
TEST_LEVEL= """
WWWWWWWWWWWWWWW
W             W
W             W
W             W
WWWWWWWWWWWWWWW""".strip().split('\n')

def test_player_move():
    game= mtg.MantiGo(
        time_limit = (0,1),
        level = TEST_LEVEL,
        player_start= (3,3)

    )
    assert game.get_map() == """
WWWWWWWWWWWWWWW
W             W
W       P     W
W             W
WWWWWWWWWWWWWWW"""

    game.player_command("right")
    assert game.get_map() == """
WWWWWWWWWWWWWWW
W             W
W       P     W
W             W
WWWWWWWWWWWWWWW"""