from random import randint, choice, choices

class Enemy:
    def __init__(self):
        images = {'police': '\U0001F46E', 'seringe': '\U0001F489', 'zombie': '\U0001F9DF',              
          'ninja': '\U0001F977', 'biker': '\U0001F6B4', 'tornado': '\U0001F32A'}
        self.type = choice(list(images.keys()))
        self.x = randint(1, 50)
        self.y = randint(1, 20)
        self.img = images[self.type]
        # self.img = 'X'
        self.direction = choice([-1, 1])

    def __repr__(self):
        return f'{self.x} {self.y} {len(self.img)} {self.type}'


    def update_position(self):
        # self.x = self.x - 1
        # if self.x == 0:
        #     self.x = 100
        #     self.y = randint(0, 20)
        self.x = self.x + self.direction
        self.y = self.y + choices([-1, 0, 1], weights=(10, 80, 10), k=1)[0]
        if self.x == 0 or self.x == 50:
            self.direction *= -1
        if self.y == 0 or self.y == 20:
            self.y = 10

    
    def collision_player(self):
        self.img = "\U0001F4A5"

        
if __name__ == '__main__':
    for i in range(4):
        enemy = Enemy()
        print(enemy)
