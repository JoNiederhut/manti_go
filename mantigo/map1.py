'''This script is to initiate the map for the game Manti GO!'''
import os
import random
import pygame

#map of the colors or textured tiles
level1tile = ["------------------------------------",
         "-  $$$$$$$$$--------- --   $ $ $ $E-",
         "- $  $$$$$$$$-------^^^^         $$-",
         "-$ $$$$$$$$ --     ^^^^    XXX    $-",
         "-  $$$$$$$ --  $  ^^^^    XXXXX    -",
         "-    $$$$$$$      ^^^^   XXXXXXX   -",
         "- $$$$$$$$$$      ^^^^   XXXXXX    -",
         "-    $$$$$$$$     ^^^^   XXXXXXX   -",
         "-$$$$$$$$$$$$$$  ^^^^     XXXXXX   -",
         "-     $$$$$$$   ^^^^         XX    -",
         "-  $ $$$       ^^^^        $ $ $ $ -",
         "- $$$$$$     ^^^^-         $$$$$$$$-",
         "-  $$$$$$   ^^^^---      $$$$$ $ $ -",
         "- $$$$$    ^^^^-----        $$$$$$$-",
         "- $$$$$$$  ^^^^-----       $ $ $ $ -",
         "- $$$$$$$ ^^^^-----       $$$$$$ $$-",
         "-  $$$$$$ ^^^^ ------      $ $ $ $ -",
         "- $$$$$$$$  ^^^^  ---            $$-",
         "------------------------------------"]
#a simple mapping: char -> color
colors = {'X': pygame.color.THECOLORS['blue'],
          '-': pygame.color.THECOLORS['grey'],
          '$': pygame.color.THECOLORS['green'],
          '^': pygame.color.THECOLORS['brown'],
          'E': pygame.color.THECOLORS['black']
          }

blocksize = 32
#map of the walls and level exits
level1wall = ["WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
         "W           WWWWWWWWW WW          EW",
         "W               WWWW               W",
         "W           WW             WWW     W",
         "W          WW             WWWWW    W",
         "W                        WWWWWWW   W",
         "W                        WWWWWW    W",
         "W                        WWWWWWW   W",
         "W                         WWWWWW   W",
         "W                            WW    W",
         "W                                  W",
         "W                W                 W",
         "W               WWW                W",
         "W              WWWWW               W",
         "W              WWWWW               W",
         "W             WWWWW                W",
         "W              WWWWWW              W",
         "W                 WWW              W",
         "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"]

level1wall = [
         "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
         "W                WWWWWWWW         EW",
         "W                WWWWWWWw     WWWWWW",
         "W                WWwwwwww     WWWWWW",
         "W                                   ",
         "W                                   ",
         "W                                   ",
         "WWWWWWW          WWWWWWWW     WWWWWW",
         "WWWWWWW          WWWWWWWw     WWWWWW",
         "WWWWWWW          WWwwwwww     WWWWWW",
         "W                                  W",
         "W                W                 W",
         "W               WWW                W",
         "W              WWWWW               W",
         "W              WWWWW               W",
         "W             WWWWW                W",
         "W              WWWWWW              W",
         "W                 WWW              W",
         "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"]

# Class for the Player object
class Player(object):

    def __init__(self):
        self.rect = pygame.Rect(64, 64, 32, 32)

    def move(self, dx, dy):

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # collide right
                    self.rect.right = wall.rect.left
                if dx < 0: # collide left
                    self.rect.left = wall.rect.right
                if dy > 0: # collide top
                    self.rect.bottom = wall.rect.top
                if dy < 0: # collide bottom
                    self.rect.top = wall.rect.bottom

# Nice class to hold a wall rect
class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
#level1wall is collision detection W = wall, E = exit, P = Player

#Block
class Block(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block, and its x and y position
    def __init__(self, color, width, height, x, y):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)
       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect(top=y, left=x)

pygame.init()


# Set up the display
pygame.display.set_caption("Tiles and Walls!")
screen = pygame.display.set_mode((len(level1tile[0])* blocksize, len(level1wall*blocksize)))
#screen = pygame.display.set_mode((1150, 600))

clock = pygame.time.Clock()
walls = [] # List to hold the walls
player = Player() # Create the player


combined_list = []  # initialize a blank list
for i in range(len(level1tile)):  # build your new list
  combined_list.append(zip(level1tile[i], level1wall[i]))

    # Parse the level string above. W = wall, E = exit
x = y = 0
for row in level1wall:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 32, 32)
        x += 32
    y += 32
    x = 0

running = True
while running:

    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
    if key[pygame.K_UP]:
        player.move(0, -2)
    if key[pygame.K_DOWN]:
        player.move(0, 2)

    # Just added this to make it slightly fun ;)
    if player.rect.colliderect(end_rect):
        raise SystemExit("Next Level!")

    # Draw the scene
    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    pygame.draw.rect(screen, (255, 0, 0), end_rect)
    pygame.draw.rect(screen, (255, 200, 0), player.rect)
    pygame.display.flip()
