import logging
logging.basicConfig(filename="log.txt", filemode="w")

from random import randint, choice, choices

TYPES = ['police', 'seringe', 'zombie', 'ninja', 'biker', 'tornado']
MAP_FIELDS = ['W', 'E', 'm']
ALLOWED_FIELD = [None, 'm']
FOBRIDDEN_FIELD = ['W', 'E']


class Enemy:
    def __init__(self, manti_map):
        self.level_map = manti_map # assigning the levelmap to the enemy
        self.max_position = manti_map.max_position() # maximum position for y and x
        self.type = choice(TYPES)
        self.y, self.x = self.create_init_position()
        self.direction = choice([-1, 1])
        

    def __repr__(self):
        return f'{self.x} {self.y} {self.type}'

    
    def get_position_symbol(self, y, x):
        for symbol in MAP_FIELDS:
            if (y, x) in self.level_map.find_coordinates(symbol):
                return symbol
        return None      
    

    def create_init_position(self):
        '''creates y and x initial coordinates until it finds a combination which is not a Wall, manti or exit'''        
        while True:
            x = randint(1, self.max_position[1])
            y = randint(1, self.max_position[0])
            if self.get_position_symbol(y, x) == None:
                return y, x
                    
            
    def update_position(self):
        '''gets next valid enemy position'''
        old_position = (self.y, self.x)
        dict_func = {
            'police': self.move_police, 
            'zombie': self.move_zombie,
            'ninja': self.move_ninja,
            'biker': self.move_biker,
            'tornado': self.move_tornado,
            'seringe': self.no_move
            }
        dict_func[self.type]()
        self.handle_map_collisions(old_position) 


    def move_police(self):
        '''stops sometimes and stays mainly on his y-position'''
        moves_bin = randint(0, 1)    
        self.x = self.x + moves_bin * self.direction
        self.y = self.y + moves_bin * choices([-1, 0, 1], weights=(1, 98, 1), k=1)[0]

    
    def move_zombie(self):
        '''stops sometimes and acts crazy'''
        self.x = self.x + choices([-1, 0, 1], weights=(30, 30, 30), k=1)[0]
        self.y = self.y + choices([-1, 0, 1], weights=(30, 30, 30), k=1)[0]

    
    def move_ninja(self):
        '''stays for a while and then suddenly appears somewhere else'''
        move_bin = choices([0, 1], weights=(80, 20), k=1)[0]
        if move_bin == 1:
            self.x = randint(1, self.max_position[1])
            self.y = randint(1, self.max_position[0])

    
    def move_biker(self):
        '''goes fast in x direction'''
        bikespeed = 2
        self.x = self.x + bikespeed * self.direction
        if self.x <= 0: 
            self.x = 0
        elif self.x >= self.max_position[1]:
            self.x = self.max_position[1]

    def move_tornado(self):        
        '''stays for a while and then suddenly appears somewhere else'''
        move_bin = choices([0, 1], weights=(70, 30), k=1)[0]
        if move_bin == 1:
            self.x = self.x + choices([-1, 0, 1], weights=(30, 30, 30), k=1)[0]
            self.y = self.y + choices([-1, 0, 1], weights=(30, 30, 30), k=1)[0]


    def no_move(self):
        pass


    def handle_map_collisions(self, old_position):
        '''check for a collision of new position and assign a valid one'''
        field = self.get_position_symbol(self.y, self.x)
        if field != None and field in FOBRIDDEN_FIELD:
            # from your old position the only valid moves now are up, down, left, right
            options = [(old_position[0] + 1, old_position[1]), (old_position[0] - 1, old_position[1]), 
                    (old_position[0], old_position[1] + 1), (old_position[0], old_position[1] - 1)]
            # choose one option which is valid
            while True:
                self.y, self.x = choice(options)
                field = self.get_position_symbol(self.y, self.x)
                if field in ALLOWED_FIELD:
                    break
            # if you are police, zombie or biker, you should also change your direction
            # if the option chosen changed the x 
            if self.type in ['police', 'zombie', 'biker']:
                if old_position[1] != self.x:
                    self.direction *= -1

        
if __name__ == '__main__':
    for i in range(4):
        enemy = Enemy()
        print(enemy)
