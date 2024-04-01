import pygame
from OPTIONS import *

class Text:
    """
    Cette classe permet de creer un texte (affichable) via pygame
    """
    def __init__(self, display, text:str, pos:tuple, width:float, col = (0,0,0)) -> None:
        self.display = display
        self.text = text
        self.pos = pos
        self.col = col
        self.font = pygame.font.SysFont("Futura", int(width))
        self.render = self.font.render(self.text, True, self.col)

    def get_text(self):
        return self.text
    
    def set_text(self, text:str):
        self.text = text
        self.render = self.font.render(self.text, True, self.col)
    
    def get_pos(self):
        return self.pos
    
    def set_pos(self, pos:tuple):
        self.pos = pos

    def get_size(self):
        return pygame.font.Font.size(self.font, self.text)

    def draw(self):
        self.display.blit(self.render, self.pos)