"""
Code that we are testing
"""

from typing import List
from mantigo.timer import MantiTimer
from mantigo.map_class import KOTTI, MantiMap
from mantigo.player import Player
import mantigo.enemy as en

class MantiGo:
    """Top-level class for the game logic."""
    def __init__(
        self, time_limit=(2,30),
        level=KOTTI, player_start = (8,8),
        number_enemies= 5
    ):
        minutes, seconds = time_limit
        self.timer = MantiTimer(minutes, seconds)
        self.timer.start()
        self.manti_map = MantiMap(level)
        self.player = Player(player_start[0],player_start[1], self.manti_map)
        self.enemies = self.create_enemies(number_enemies)


    @property
    def status(self):
        """Returns game status."""
        if self.timer.is_running():
            return "running"

        return "Game Over"


    def create_enemies(self, number=1):
     
        enemies = []
        # create the enemy objects
        for _ in range(number):
            enemies.append(en.Enemy(self.manti_map))
        return enemies

    def get_symbols(self) -> list:
        results = []
        for symbol in "WmE":
            for y,x in self.manti_map.find_coordinates(symbol):
                results.append((y,x,symbol))
        for enemy in self.enemies:
            results.append((enemy.y,enemy.x,enemy.type))
        results.append((self.player.y, self.player.x, "player"))
        return results

    def update(self):
        for enemy in self.enemies:
            enemy.update_position()

        for e in self.enemies:
            if (e.x, e.y) == self.player.position:
                self.timer.time_penalty
                return True                     # later impute with "enemies.position"


    def move(self,direction):
        self.player.player_move(direction)


    
