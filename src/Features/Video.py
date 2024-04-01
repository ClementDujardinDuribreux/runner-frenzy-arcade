import pygame
import os
from OPTIONS import *
from Features.Image import Img

class Video:

    """
    Cette classe permet de creer une video a partir d'une serie d'image (affichable) via pygame
    """

    def __init__(self, path_folder:str) -> None:
        self.path_folder = path_folder
        self.liste_img = os.listdir(path_folder)
        self.liste_img.sort()
        self.as_sound = False
        self.clock = pygame.time.Clock()

    def play(self, display, pos:tuple, width:float, height:float):
        running = True
        n_image = 1
        if n_image + 1 <= len(self.liste_img):
            img = Img(display, self.path_folder + '/' + self.liste_img[n_image], pos, 0, 0)
        if self.as_sound:
            self.sound.play()
        while running:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    running = False
                    if self.as_sound:
                        self.sound.stop()
            if n_image < len(self.liste_img):
                img.set_img(self.path_folder + '/' + self.liste_img[n_image])
                img.set_size(width, height)
                img.draw()
                n_image += 1
            else: running = False
            pygame.display.flip()

    def add_sound(self, path:str):
        self.sound = pygame.mixer.Sound(path)
        self.as_sound = True

    def set_volume(self, vol:float):
        if self.as_sound:
            self.sound.set_volume(vol)