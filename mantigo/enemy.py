from random import randint, choice, choices
import movements as mv

class Enemy:
    def __init__(self, manti_map):
        IMAGES = {'police': '\U0001F46E', 'seringe': '\U0001F489', 'zombie': '\U0001F9DF',              
          'ninja': '\U0001F977', 'biker': '\U0001F6B4', 'tornado': '\U0001F32A'}
        self.type = choice(list(IMAGES.keys()))
        self.y, self.x = self.create_init_position()
        self.img = IMAGES[self.type]
        self.direction = choice([-1, 1])
        self.level_map = manti_map
        self.max_position = (20, 50) # maximum position for y and x


    def __repr__(self):
        return f'{self.x} {self.y} {len(self.img)} {self.type}'

    
    def check_map_collision(self, y, x):
        for symbol in "WmE":
            if (y, x) in self.level_map.find_coordinates(symbol):
                return symbol
                
    
    def create_init_position(self):
        # creates y and x initial coordinates until it finds a combination which is not a Wall, manti or exit
        while True:
            x = randint(1, self.max_position[1])
            y = randint(1, self.max_position[0])
            if self.check_map_collision(y, x) not in "WmE":
                return y, x
                
            
    def update_position(self):
        old_position = (self.y, self.x)
        if self.type == 'police':
            # stops sometimes and stays mainly on his y-position
            moves_bin = randint(0, 1)    
            self.x = self.x + moves_bin * self.direction
            self.y = self.y + moves_bin * choices([-1, 0, 1], weights=(1, 98, 1), k=1)[0]

        elif self.type == 'sering':
            pass
            # doesn't move

        elif self.type == 'zombie':
            # stops sometimes and acts crazy
            if self.x == 0 or self.x == self.max_position[1]:
                self.direction *= -1
                self.x = self.x + self.direction
            else:
                self.x = self.x + choices([-1, 0, 1], weights=(30, 30, 30), k=1)[0]
            self.y = self.y + choices([-1, 0, 1], weights=(30, 30, 30), k=1)[0]

        elif self.type == 'ninja':
            # stays for a while and then suddenly appears somewhere else
            move_bin = choices([0, 1], weights=(80, 20), k=1)[0]
            if move_bin == 1:
                self.x = randint(1, self.max_position[1])
                self.y = randint(1, self.max_position[0])

        elif self.type == 'biker':
            # goes fast in x direction
            bikespeed = 2
            self.x = self.x + bikespeed * self.direction
            if self.x <= 0: 
                self.x = 0
            elif self.x >= self.max_position[1]:
                self.x = self.max_position[1]

        elif self.type == 'tornado':
            # stays for a while and then suddenly appears somewhere else
            move_bin = choices([0, 1], weights=(70, 30), k=1)[0]
            if move_bin == 1:
                # if self.x == 0:
                #     self.direction *= -1
                #     self.x = self.x + self.direction
                # else:
                self.x = self.x + choices([-1, 0, 1], weights=(30, 30, 30), k=1)[0]
                self.y = self.y + choices([-1, 0, 1], weights=(30, 30, 30), k=1)[0]

        # react on map obstacles
        # react ion Wall and exit with random free position
        if self.check_map_collision(self, self.y, self.x) in "WE":
            # from your old position the only valid moves now are up, down, left, right
            options = [(old_position[0] + 1, old_position[1]), (old_position[0] - 1, old_position[1]), 
                    (old_position[0], old_position[1] + 1), (old_position[0], old_position[1] - 1)]
            # choose one option which is valid
            while True:
                self.y, self.x = choice(options)
                if self.check_map_collision(self.y, self.x) not in "WE":
                    break
            # if you are police, zombie or biker, you should also change your direction
            # if the option chosen changed the x 
            if self.type in ['police', 'zombie', 'biker'] :
                if old_position[1] != self.x:
                    self.direction *= -1

        # prevention of running out of bounds
        # if self.x <= 0:
        #     self.x = 0
        #     self.direction *= -1
        # elif self.x >= self.max_position[1]:
        #     self.x = self.max_position[1]
        #     self.direction *= -1
        # if self.y <= 0 or self.y >= self.max_position[0]:
        #     TODO 
        #     self.y = 10


    
    def collision_player(self):
        self.img = "\U0001F4A5"

        
if __name__ == '__main__':
    for i in range(4):
        enemy = Enemy()
        print(enemy)
