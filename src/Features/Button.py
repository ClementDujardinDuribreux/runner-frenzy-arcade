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
        self.initial_colour = col
        self.colours = col, col2
        self.selected = False
        self.text = Text(self.display, text, (0,0), 35 * (SCREENINFO.RES[0]/720))
        self.sound = pygame.mixer.Sound('sounds/BUTTON SOUND.mp3')
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
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE and self.clicked:
            self.clicked = False
            self.draw()
            time.sleep(0.15)
            return self.renvoi

    def isClicked(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.selected:
            self.clicked = True
            self.sound.play()

    def on(self):
        if not self.selected:
            if self.colours[0][0] <= 255 - 200: col1 = self.colours[0][0] + 200
            else: col1 = self.colours[0][0] + (200 - (self.colours[0][0] + 200)%255)
            if self.colours[0][1] <= 255 - 200: col2 = self.colours[0][1] + 200
            else: col2 = self.colours[0][1] + (200 - (self.colours[0][1] + 200)%255)
            if self.colours[0][2] <= 255 - 200: col3 = self.colours[0][2] + 200
            else: col3 = self.colours[0][2] + (200 - (self.colours[0][2] + 200)%255)
            self.selected = True
            self.colours = (col1, col2, col3), self.colours[1]

    def reset_colour(self):
        self.colours = self.initial_colour, self.colours[1]
        self.selected = False