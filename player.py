

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = "\U0001F9C0"
        self.num_manti = 10

    @property
    def position(self):
        return self.x,self.y

    def player_move(self,direction):
        if direction == "left":
            self.x -= 1
        elif direction == "right":
            self.x += 1
        elif direction == "up":
            self.y -= 1
        elif direction == "down":
            self.y += 1


    def collision_player(self):
        self.img = "\U0001F4A5"

    def get_status(self):
        ...
        return 'alive'
        
