from time import sleep

class MantiTimer():
    """This class hanles the time in the game"""
    def __init__(self, target_time):
        self.target_time = target_time
        self.min_ = 0
        self.sec_ = 0

    def get_time(self):
        return f'{self.min_:02d}:{self.sec_:02d}'

    def next_sec(self):
        self.sec_ = 1 + self.sec_
        self.min_ = self.min_ + self.sec_ // 60
        self.sec_ = self.sec_ % 60
        #sleep(1)
        return (self.min_, self.sec_)