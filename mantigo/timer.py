'''Timer.py initialises the time functionality and timer for the game Manti GO!'''
from datetime import datetime

class MantiTimer():
    """This class handles the time in the game"""
    def __init__(self,minutes:int,sec:int) -> None:
        self.start_time = None
        self.current_time = None
        self.new_minutes = None
        self.new_sec = None
        self.minutes_ = minutes
        self.sec_ = sec

    @property
    def expiring_time(self):
        '''Returns the time left'''
        return f'{self.minutes_:02d}:{self.sec_:02d}'

    def start(self):
        '''Starts the timer'''
        self.start_time = datetime.now()
        return self.start_time

    @property
    def get_time_str(self):
        '''Returns the time'''
        self.current_time = datetime.now() - self.start_time
        self.new_minutes = int(self.current_time.total_seconds()//60)
        self.new_sec = int(self.current_time.total_seconds()%60)
        return f"{self.new_minutes:02d}:{self.new_sec:02d}"

    def is_running(self) -> bool:
        '''Runs the time'''
        return self.get_time_str != self.expiring_time


if __name__ == '__main__':
    timer=MantiTimer(minutes=3,sec=1)
    timer.start()
    while timer.is_running():
        print(timer.get_time_str)
