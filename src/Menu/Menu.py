import pygame
from OPTIONS import*
from Features.Image import Img
from Features.Features import *

class Menu:

    """
    Cette classe permet de creer un menu
    """

    def __init__(self, args:list) -> None:
        self.args = args
        self.display = args[0]
        self.item_list = []
        self.music = ''
        self.play = True
        self.has_background = False
        self.firstDraw = False

    def draw(self, event):
        retour = []
        for item in self.item_list:
            if type(item).__name__ is 'Button':
                retour.append(item.update(event))
            else: item.draw()
        pygame.display.flip()
        return retour
    
    def re_init(self):
        self.__init__(self.args)

    def set_backgroud(self, img:str):
        item_list = [Img(self.display, IMG[img], (0,0), SCREENINFO.RES[0], SCREENINFO.RES[1])]
        for item in self.item_list:
            item_list.append(item)
        self.item_list = item_list
        self.has_background = True

    def draw_items(self):
        for item in self.item_list:
            item.draw()
        self.firstDraw = True

    def undraw(self):
        for item in self.item_list:
            if type(item).__name__ is 'Button':
                item.undraw()
        self.firstDraw = False
    
    def play_music(self):
        if self.music is not '' and self.play:
            self.play = False
            pygame.mixer.music.load(self.music)
            pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

    def pause_music(self):
        pygame.mixer.music.pause()

    def unpause_music(self):
        pygame.mixer.music.unpause()