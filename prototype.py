"""
Proof-of-concept: move around in a 2D frame

TODO:
 - program an actual game
 - add instructions for the user
 - add docstrings
 - add comments
 - use arrow key instead
 - do not crash when you move outside window
 - remove code duplicate (draw) and make it a function
 - create a prepare_screen function
 - no option to quit the game e.g. 'Q'
 - make smaller functions
"""
import curses
import player as pl

from timer import MantiTimer
from mantisound import MantiDj
from map_class import MantiMap
from map_class import KOTTI

import enemy as en
import time
import logging
logging.basicConfig(filename="log.txt", filemode="w")


# WASD keys
KEY_COMMANDS = {97: "left", 100: "right", 119: "up", 115: "down"}

# prepare the screen
screen = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.curs_set(0)
curses.noecho()
curses.raw()
screen.keypad(False)

#SYMBOLS = dict(W="\U0001F9F1", m="\U0001F95F", E="\U0001F6AA")
SYMBOLS = dict(W="🚧", m="🥟", E="🚪")

win = curses.newwin(40, 20, 0, 0)
win.nodelay(True)


# prepare the timer
clock = MantiTimer(min=3,sec=5)
clock.start()



def draw(level, player, screen, win, time_to_draw:str, enemies):
    screen.clear()
    for symbol in "WmE":
        for y,x in level.find_coordinates(symbol):
        
            screen.addch(y,x*2, SYMBOLS[symbol], curses.color_pair(1))
            
    for enemy in enemies:
        move_enemies(enemies)
        screen.addch(enemy.y, enemy.x*2, enemy.img, curses.color_pair(1)) 
    screen.addch(player.y, player.x*2, player.img, curses.color_pair(1))
    screen.addstr(0,85, time_to_draw, curses.color_pair(1))
    # check if enemy hits player
    if (enemy.y, enemy.x) == (player.y, player.x*2):
        enemy.collision_player()  
    win.refresh()
    screen.refresh()


def move_player(win, player):
    char = win.getch()
    direction = KEY_COMMANDS.get(char)
    if direction is None:
        return False
    else:
        player.player_move(direction)
    return True

def create_enemies(number=1):
    enemies = []
    # create the enemy objects
    for enemy in range(number):
        enemies.append(en.Enemy())
    return enemies
   
def move_enemies(enemies):
    # move enemies when user input
    for enemy in enemies:
        enemy.update_position()  
        logging.warning(str(enemy))


def game_loop(screen):
    """called by curses"""

    MantiDj().play_music()
    level = MantiMap(KOTTI)
    enemies = create_enemies(10) #, level
    player = pl.Player(5, 5, level)
    
    draw(level, player, screen,win,'00:00', enemies)

    
    while clock.is_running():
        if move_player(win,player):
           draw(level, player, screen,win,clock.get_time_str, enemies)
        else:
           time.sleep(0.1)
           draw(level, player, screen,win,clock.get_time_str, enemies)

if __name__ == "__main__":
    curses.wrapper(game_loop)
    curses.endwin()
