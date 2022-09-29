"""music downloaded from https://archive.org/details/md_music_tetris/02+-+Tetremix+A+-+Unknown.flac
"""

from os import path, listdir
from numpy.random import choice
from pygame import mixer

PATH = "./manti_music/"

MANTI_ARCADE_TONES = [path.join(PATH,file) for file in listdir(PATH)]

class MantiDj:
    """This class handles the music"""
    def __init__(self) -> None:
        self.filename = choice(MANTI_ARCADE_TONES)
        self.dj = mixer

    def play_music(self) -> None:
        """It starts the mixer, loads the file,
        and plays the music in endless loop"""
        # Starting the mixer
        self.dj.init()
        # Loading the file
        self.dj.music.load(self.filename)
        # Play the music in endless loop
        self.dj.music.play(loops=-1)

if __name__ == "__main__":
    manti_dj = MantiDj()
    manti_dj.play_music()
    # while loop needed to actually play the music
    while True:
        continue
