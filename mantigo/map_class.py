
""" The Map Class """

KOTTI =  """WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
W                 WWWWWWWWW          WWWWWW
W                 WWWWWWWWW     m    WWWWWW
W  WWWWWW         WWWWWWWWW          WWWWWW
W  WWWWWW    m    WWWWWWWWW               W
W  WWWWWW                                 W
W                 WWWWWWWWW               W
W  WWWWWW         WWWWWWWWW          WWWWWW
W  WWWWWW         WWWWWWWWW    m     WWWWWW
W  WWWWWW         WWWWWWWWW          WWWWWW
W  WWWWWW         WWWWWWWWW          WWWWWW
W  WWWWWW         WWWWWWWWW               W
W     m                               m   W
W                                         W
W  WWWWWW         WWWWWWWWW          WWWWWW
W  WWWWWW         WWWWWWWWW          WWWWWW
W  WWWWWW         WWWWWWWWW          WWWWWW
W  WWWWWW         WWWWWWWWW          WWWWWW
W         m                          WWWWWW
W                                      m  E
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
"""


class MantiMap:
    def __init__(self, map_str):
        self.map= map_str

    def find_coordinates(self, chr):
        """with this function you can find the coordinates of the forbidden area, manti, and exit point
        chrachter description:
        W = wall
        E = exit
        m = manti
        """
        
        wall_position = []
        for y, item in enumerate(self.map.splitlines()):
            for x, chracter in enumerate(item):
                if chracter == chr:
                    wall_position.append((y,x))
        return wall_position


    def max_position(self):
        lines = self.map.splitlines()
        y_max = len(lines) - 1
        x_max = len(lines[0]) - 1
        return y_max, x_max