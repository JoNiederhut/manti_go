"""
Proof-of-concept: move around in a 2D frame
"""
import curses

from mantigo.mantisound import MantiDj
from mantigo.mantigo_game import MantiGo

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
SYMBOLS = dict(W="🚧", m="🦄", E="\U0001F6AA", player="P", police='\U0001F46E', seringe='\U0001F489'
    , zombie='\U0001F9DF', ninja='\U0001F977', biker='\U0001F6B4', tornado='\U0001F32A' ) # add other symbols (enemies, etc.)
win = curses.newwin(40, 20, 0, 0)   
win.nodelay(True)


def draw(win, game):
    screen.clear()

    for y, x, symbol in game.get_symbols():
         screen.addch(y,x*2, SYMBOLS.get(symbol, "?"), curses.color_pair(1))

    screen.addstr(0,85, f"Timer: {game.timer.get_time_str}", curses.color_pair(1))
    screen.addstr(0,100, f'Lives: {game.player.lives}', curses.color_pair(1))
    # check if enemy hits player
    # if (enemy.y, enemy.x) == (player.y, player.x*2):
    #     enemy.collision_player()  
    win.refresh()
    screen.refresh()


def move_player(win, game):
    char = win.getch()
    direction = KEY_COMMANDS.get(char)
    if direction is None:
        return False
    else:
        game.move(direction)
    return True


def game_loop(screen):
    """called by curses"""

    game = MantiGo()
    MantiDj().play_music()
    draw(win, game)
    
    counter = 0

    while game.status == "running" :
        if move_player(win,game):
            draw(win, game)

        counter += 1
        if counter % 100000 == 0:
            game.update()
            draw(win, game)      



def main():                     # makes program callable in a different environement ("mantigo")
    curses.wrapper(game_loop)
    curses.endwin()
    
if __name__ == "__main__":       # makes program executable ("python prototype.py")
    main()