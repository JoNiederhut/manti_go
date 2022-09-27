from random import randint, choice, choices

class Enemy:
    def __init__(self):
        images = ["\U0001F984", "\U0001F959", "\U0001F37A", "\U0001F959"]
        self.x = randint(0, 100)
        self.y = randint(0, 20)
        self.img = images[randint(0, 3)]
        self.direction = choice([-1, 1])


    def update_position(self):
        # self.x = self.x - 1
        # if self.x == 0:
        #     self.x = 100
        #     self.y = randint(0, 20)
        self.x = self.x + self.direction
        self.y = self.y + choices([-1, 0, 1], weights=(10, 80, 10), k=1)[0]
        if self.x == 0 or self.x == 100:
            self.direction *= -1
        if self.y == 0 or self.y == 20:
            self.y = 10

    
    def collision_player(self):
        self.img = "\U0001F4A5"
        

