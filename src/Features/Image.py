import pygame
from Features.Features import *

class Img:
    """
    Cette classe permet de creer une image via pygame
    """
    def __init__(self, display, path:str, pos:tuple, width:int, height:int) -> None:
        self.display = display
        self.file = path
        if path != '':
            self.img = pygame.image.load(path)
        self.set_size(width, height)
        self.pos_init = pos
        self.pos = pos

    def get_pos(self):
        return self.pos

    def set_pos(self, pos:tuple):
        self.pos = pos
        self.pos_init = pos
    
    def set_size(self, width:int, height:int):
        self.img = pygame.transform.scale(self.img, (width, height))

    def set_img(self, path):
        self.img = pygame.image.load(path)
    
    def __str__(self) -> str:
        return self.file
    
    def draw(self):
        self.display.blit(self.img, (self.pos[0], self.pos[1]))