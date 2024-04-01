import random
from OPTIONS import *
from Menu.Menu import *
from Game.Game import Game
from Features.Features import *
from Features.Button import Button
from Features.Text import Text

class SceneMenu(Game, Menu):

    """
    Cette classe permet de creer le menu scene (le menu du jeu)
    """

    def __init__(self, args) -> None:
        Game.__init__(self, args)
        Menu.__init__(self, args)
        self.args = args
        music =  random.randint(0,len(MUSICS) - 1)
        self.music = MUSICS[music]
        self.item_list = []

    def restart(self):
        self.__init__(self.args)