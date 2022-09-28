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
from timer import MantiTimer
#from multiprocessing import Process
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

def draw(x, y, screen, win, time_to_draw:str):
    screen.clear()
    screen.addch(y, x, "O", curses.color_pair(1))
    screen.addstr(0,85, time_to_draw, curses.color_pair(1))
    win.refresh()
    screen.refresh()

def handle_moves(win,x,y):
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
        pass
    return x,y

def game_loop(screen):
    """called by curses"""
    x, y = 5, 5
    draw(x,y,screen,win,'00:00')
    

    while clock.is_running():
        draw(x,y,screen,win,clock.get_time_str)
        # handle moves
        x,y = handle_moves(win,x,y)
        draw(x,y,screen,win,clock.get_time_str)


if __name__ == "__main__":
    curses.wrapper(game_loop)
    curses.endwin()
