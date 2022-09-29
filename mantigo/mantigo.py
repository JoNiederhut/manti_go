"""
Code that we are testing
"""

from mantigo.timer import MantiTimer
from mantigo.player import Player
import mantigo.enemy as en

class MantiGo:

    def __init__(self, time_limit=(2,30)):
        minutes, seconds = time_limit
        self.timer = MantiTimer(minutes, seconds)
        self.timer.start()
        self.player = Player()
        self.enemies = self.create_enemies(50)
        
    @property
    def status(self):
        if self.timer.is_running():
            return "running"

        else:
            return "Game Over"



    def create_enemies(self,number=1):
        enemies = []
        # create the enemy objects
        for enemy in range(number):
            enemies.append(en.Enemy())
        return enemies