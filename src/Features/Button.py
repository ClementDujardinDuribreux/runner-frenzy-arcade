import pygame
import time
from OPTIONS import *
from Features.Image import Img
from Features.Text import Text
from Features.Features import *

class Button:
    """
    Cette classe permet de creer un boutton via pygame
    """
    def __init__(self, display, pos:tuple, width_height:tuple, col:tuple, col2:tuple, text:str, renvoi, img = '') -> None:
        self.display = display
        self.pos = pos[0], pos[0] + width_height[0], pos[1], pos[1] + width_height[1]
        self.widht_height = width_height
        self.colours = col, col2
        self.text = Text(self.display, text, (0,0), 35 * (SCREENINFO.RES[0]/720))
        self.sound = 'sounds/BUTTON SOUND.mp3'
        self.img = None
        self.decal = 9
        self.renvoi = renvoi
        self.clicked = False
        self.canBlit = True
        self.isDraw = False
        self.canDecal = True
        if img != '':
            self.decal = 45 * (SCREENINFO.RES[0]/720)
            self.img = Img(self.display, IMG[img], (self.pos[0] + self.widht_height[0] / 2 - self.widht_height[1] / 2 + 1, self.pos[2] - 6 * (SCREENINFO.RES[1]/450)), width_height[1], width_height[1])
            if self.text.get_text() is not '': 
                self.img.set_size(width_height[1] - 7, width_height[1] - 7)
                self.img.set_pos((self.pos[0] + 35*(SCREENINFO.RES[0]/720), self.pos[2] - SCREENINFO.RES[1]/(450/3)))
        if type(self.img).__name__ is 'Img': self.has_img = True
        else: self.has_img = False
               
    def draw(self):
        if not self.isDraw:
            self.isDraw = True
            self.array = pygame.surfarray.array2d(self.display)
        if not self.clicked: 
            self.canBlit = True
            decal_click = 5*(SCREENINFO.RES[0]/720)
            if not self.canDecal and self.has_img:
                self.img.set_pos((self.img.get_pos()[0], self.img.get_pos()[1] - 5*(SCREENINFO.RES[0]/720)))
                self.canDecal = True
        else:
            if self.canBlit:
                pygame.surfarray.blit_array(self.display, self.array)
                self.canBlit = False
            decal_click = 0
            if self.canDecal and self.has_img:
                self.img.set_pos((self.img.get_pos()[0], self.img.get_pos()[1] + 5*(SCREENINFO.RES[0]/720)))
                self.canDecal = False
        pygame.draw.rect(self.display, self.colours[1], pygame.Rect(self.pos[0], self.pos[2], self.widht_height[0], self.widht_height[1]),border_radius=int(15*(SCREENINFO.RES[0]/720)))
        pygame.draw.rect(self.display, self.colours[0], pygame.Rect(self.pos[0], self.pos[2] - decal_click, self.widht_height[0], self.widht_height[1]), border_radius=int(15*(SCREENINFO.RES[0]/720)))                
        self.text.set_pos((self.pos[0] + self.widht_height[0]/2 + self.decal - self.text.get_size()[0]/2, self.pos[2] + self.widht_height[1]/2 - self.text.get_size()[1]/2 - decal_click))
        self.text.draw()
        if self.has_img:
                self.img.draw()

    def undraw(self):
        self.isDraw = False

    def update(self, event):
        self.draw()
        self.isClicked(event) 
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.clicked:                
            self.clicked = False
            self.draw()
            if pygame.mouse.get_pos()[0] > self.pos[0] and pygame.mouse.get_pos()[0] < self.pos[1] and pygame.mouse.get_pos()[1] > self.pos[2]-7 and pygame.mouse.get_pos()[1] < self.pos[3]-7:
                time.sleep(0.15)
                return self.renvoi

    def isClicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] > self.pos[0] and pygame.mouse.get_pos()[0] < self.pos[1] and pygame.mouse.get_pos()[1] > self.pos[2]-7 and pygame.mouse.get_pos()[1] < self.pos[3]-7:
                if pygame.mouse.get_pressed(3)[0]:
                    self.clicked = True
                    sound_button = pygame.mixer.Sound(self.sound)
                    sound_button.set_volume(1)
                    sound_button.play()