"""
Code that we are testing
"""

from timer import MantiTimer

class MantiGo:

    def __init__(self, time_limit=(2,30)):
        minutes, seconds = time_limit
        self.timer = MantiTimer(minutes, seconds)
        self.timer.start()
        
    @property
    def status(self):
        if self.timer.is_running():
            return "running"

        else:
            return "Game Over"




        self.status = "Game Over"