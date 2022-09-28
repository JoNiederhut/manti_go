from datetime import datetime

class MantiTimer():
    """This class handles the time in the game"""
    def __init__(self,min:int,sec:int) -> None :
        self.min_ = min
        self.sec_ = sec
    
    @property
    def expiring_time(self):
        return f'{self.min_:02d}:{self.sec_:02d}'
    
    def start(self):
        self.start_time = datetime.now()
        return self.start_time

    @property
    def get_time_str(self):
        self.current_time = datetime.now() - self.start_time
        self.new_min = int(self.current_time.total_seconds()//60)
        self.new_sec = int(self.current_time.total_seconds()%60)
        return f"{self.new_min:02d}:{self.new_sec:02d}"
    
    def is_running(self) -> bool:
       return self.get_time_str != self.expiring_time


if __name__ == '__main__':
    timer=MantiTimer(min=3,sec=1)
    timer.start()
    while timer.is_running():
        print(timer.get_time_str)
        
