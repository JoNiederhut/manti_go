"""
Proof-of-concept: move around in a 2D frame
"""
import curses
from random import randint
import enemy as en
import time

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

def create_enemies(number=1):
    enemies = []
    # create the enemy objects
    for enemy in range(number):
        enemies.append(en.Enemy())
    return enemies

def game_loop(screen):
    """called by curses"""
    x, y = 5, 5
    enemies = create_enemies(50)

    # draw
    screen.clear()
    # draw the enemy objects
    for enemy in enemies:
        screen.addch(enemy.y, enemy.x, enemy.img, curses.color_pair(1))
        # check if enemy hits player
        if (enemy.y, enemy.x) == (y, x):
            enemy.collision_player()    
    screen.addch(y, x, "O", curses.color_pair(1))
    win.refresh()
    screen.refresh()


    while True:

        # handle moves
        char = win.getch()
        direction = KEY_COMMANDS.get(char)

        if direction == "left":
            x -= 1
        elif direction == "right":
            x += 1
        elif direction == "up":
            y -= 1
        elif direction == "down":
            y += 1
        else:
            # move enemies when user didn'T input anything
            time.sleep(0.1)
            screen.clear()
            for enemy in enemies:
                enemy.update_position()
                # check if enemy hits player
                if (enemy.y, enemy.x) == (y, x):
                    enemy.collision_player()    
                screen.addch(enemy.y, enemy.x, enemy.img, curses.color_pair(1)) 
            screen.addch(y, x, "O", curses.color_pair(1))
            win.refresh()
            screen.refresh()
            continue
        print(x, y)

        # draw
        screen.clear()
        # move enemies when user input
        for enemy in enemies:
            enemy.update_position()
            # check if enemy hits player
            if (enemy.y, enemy.x) == (y, x):
                enemy.collision_player()    
            screen.addch(enemy.y, enemy.x, enemy.img, curses.color_pair(1)) 
        screen.addch(y, x, "O", curses.color_pair(1))
        win.refresh()
        screen.refresh()


if __name__ == "__main__":
    curses.wrapper(game_loop)
    curses.endwin()
