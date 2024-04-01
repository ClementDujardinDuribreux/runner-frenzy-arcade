import pygame
from OPTIONS import *
from Menu.Menu import Menu
from Menu.SceneMenu import SceneMenu
from Menu.MainMenu import MainMenu
from Features.Button import Button

class PauseMenu(Menu):

    """
    Cette classe permet de creer le menu pause
    """

    def __init__(self, args: list) -> None:
        super().__init__(args)
        button_play = Button(self.display, (SCREENINFO.RES[0]*0.2, SCREENINFO.RES[1]*0.20), (SCREENINFO.RES[0]*0.6, SCREENINFO.RES[1]*0.15), (255,255,0), (0,0,0), 'REPRENDRE', 'SceneMenu', 'Arrow_b')
        button_restart = Button(self.display, (SCREENINFO.RES[0]*0.2, SCREENINFO.RES[1]*0.45), (SCREENINFO.RES[0]*0.6, SCREENINFO.RES[1]*0.15), (255,255,0), (0,0,0), 'RELANCER', 'Restart', 'Restart')
        button_quit = Button(self.display, (SCREENINFO.RES[0]*0.2, SCREENINFO.RES[1]*0.70), (SCREENINFO.RES[0]*0.6, SCREENINFO.RES[1]*0.15), (255,255,0), (0,0,0), 'MENU PRINCIPAL', 'MainMenu', 'Quit')

        self.item_list = [button_play, button_restart, button_quit]