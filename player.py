

class Player:

    def __init__(self, x, y, manti_map):
        self.x = x
        self.y = y
        self.img = "\U0001F9C0"
        self.num_manti = 10
        self.manti_map = manti_map

    @property
    def position(self):
        return self.x,self.y

    def player_move(self,direction):
        old_position = (self.y, self.x)
        if direction == "left":
            self.x -= 1
        elif direction == "right":
            self.x += 1
        elif direction == "up":
            self.y -= 1
        elif direction == "down":
            self.y += 1
        #check the wall
        if (self.y, self.x) in self.manti_map.find_coordinates("W"):
            self.y = old_position[0]
            self.x = old_position[1]


    def collision_player(self):
        self.img = "\U0001F4A5"

    def get_status(self):
        ...
        return 'alive'
        
