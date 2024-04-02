from OPTIONS import *
from Menu.Menu import Menu
from Features.Button import Button
from Features.Image import Img
from Features.Features import *

class DeathMenu(Menu):

    """
    Cette classe permet de creer le menu de Game Over
    """

    def __init__(self, args):
        super().__init__(args)
        img_go = Img(self.display, IMG['GameOver'], (SCREENINFO.RES[0]*0.26, SCREENINFO.RES[1]*0.03), SCREENINFO.RES[0]*0.5, SCREENINFO.RES[1]*0.5)
        button_restart = Button(self.display, (SCREENINFO.RES[0]*0.2, SCREENINFO.RES[1]*0.55), (SCREENINFO.RES[0]*0.6, SCREENINFO.RES[1]*0.15), (255,255,0), (0,0,0), 'RELANCER', 'Restart', 'Restart')
        button_MainMenu = Button(self.display, (SCREENINFO.RES[0]*0.2, SCREENINFO.RES[1]*0.75), (SCREENINFO.RES[0]*0.6, SCREENINFO.RES[1]*0.15), (255,255,0), (0,0,0), 'MENU PRINCIPAL', 'MainMenu', 'Quit')
        self.item_list = [img_go, button_restart, button_MainMenu]
        self.make_button_list()