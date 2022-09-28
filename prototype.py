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
import Player as pl

from timer import MantiTimer
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

win = curses.newwin(20, 20, 0, 0)
win.nodelay(True)


# prepare the timer
target_time = (2,5)
clock = MantiTimer(min=3,sec=5)
clock.start()

def draw(screen, win, time_to_draw:str, enemies):
    screen.clear()
    for enemy in enemies:
        move_enemies(enemies)
        screen.addch(enemy.y, enemy.x, enemy.img, curses.color_pair(1)) 
    screen.addch(player.y, player.x, player.img, curses.color_pair(1))
    screen.addstr(0,85, time_to_draw, curses.color_pair(1))
    # check if enemy hits player
    if (enemy.y, enemy.x) == (player.y, player.x):
        enemy.collision_player()  
    win.refresh()
    screen.refresh()


def move_player(win, player):
    char = win.getch()
    direction = KEY_COMMANDS.get(char)
    if direction is None:
        return false
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

    enemies = create_enemies(50)
    player = pl.Player(5, 5)
    draw(screen,win,'00:00', enemies)
    
    while clock.is_running():
        if move_player(player):
           draw(screen,win,clock.get_time_str, enemies)
        else:
           time.sleep(0.1)
           draw(screen,win,clock.get_time_str, enemies)

if __name__ == "__main__":
    curses.wrapper(game_loop)
    curses.endwin()
