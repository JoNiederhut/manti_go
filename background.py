

MAZE1= """WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
W                 WWWWWWWWW          WWWWWW
W                 WWWWWWWWW          WWWWWW
W  WWWWWW         WWWWWWWWW          WWWWWW
W  WWWWWW         WWWWWWWWW               W
W  WWWWWW                                 W
W                 WWWWWWWWW               W
W  WWWWWW         WWWWWWWWW          WWWWWW
W  WWWWWW         WWWWWWWWW          WWWWWW
W  WWWWWW         WWWWWWWWW          WWWWWW
W  WWWWWW         WWWWWWWWW          WWWWWW
W  WWWWWW         WWWWWWWWW               W
W                                         W
W                                         W
W  WWWWWW         WWWWWWWWW          WWWWWW
W  WWWWWW         WWWWWWWWW          WWWWWW
W  WWWWWW         WWWWWWWWW          WWWWWW
W  WWWWWW         WWWWWWWWW          WWWWWW
W                                    WWWWWW
W                                         E
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
"""

def find_y_x(maze:str, char:str):
    for y, string in enumerate(maze.splitlines()):
        for x, c in enumerate(string):
            if c == char:
                yield (y,x)


POSITION_WALL = list(find_y_x(MAZE1,"W"))
POSITION_EXIT = list(find_y_x(MAZE1,"E"))

NEW_MAZE = MAZE1.replace("W","🚧").replace(" ","🚥").replace("E","🎥")

if __name__ == '__main__':
    print(POSITION_EXIT)
    print(MAZE1.replace("W","🚧").replace(" ","🚥").replace("E","🎥"))

