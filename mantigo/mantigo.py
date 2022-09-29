"""
Code that we are testing
"""

from timer import MantiTimer
from map_class import KOTTI, MantiMap
from player import Player
import enemy as en

class MantiGo:
    """Top-level class for the game logic."""
    def __init__(self, time_limit=(2,30)):
        minutes, seconds = time_limit
        self.timer = MantiTimer(minutes, seconds)
        self.timer.start()
        self.manti_map = MantiMap(KOTTI)
        self.player = Player(8, 8, MantiMap)
        self.enemies = self.create_enemies(50)


    @property
    def status(self):
        """Returns game status."""
        if self.timer.is_running():
            return "running"

        return "Game Over"


    def create_enemies(self,number=1):
        """Behavior of enemies."""
        enemies = []
        # create the enemy objects
        for enemy in range(number):
            enemies.append(en.Enemy(enemy))
        return enemies
