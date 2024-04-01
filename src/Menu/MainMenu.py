from Menu.Menu import *
from Features.Features import *
from Features.Button import Button
from Features.Image import Img

class MainMenu(Menu):

    """
    Cette classe permet de creer le menu principal
    """

    def __init__(self, args) -> None:
        super().__init__(args)
        button_play = Button(self.display, (SCREENINFO.RES[0]*0.2, SCREENINFO.RES[1]*0.20), (SCREENINFO.RES[0]*0.6, SCREENINFO.RES[1]*0.15), (255,255,0), (0,0,0), 'JOUER', 'SceneMenu', 'Arrow_f')
        button_connection = Button(self.display, (SCREENINFO.RES[0]*0.2, SCREENINFO.RES[1]*0.45), (SCREENINFO.RES[0]*0.6, SCREENINFO.RES[1]*0.15), (255,255,0), (0,0,0), 'CONNEXION', 'Connection', 'Internet')
        button_quit = Button(self.display, (SCREENINFO.RES[0]*0.2, SCREENINFO.RES[1]*0.70), (SCREENINFO.RES[0]*0.6, SCREENINFO.RES[1]*0.15), (255,255,0), (0,0,0), 'QUITTER', 'Quit', 'Quit')
        button_option = Button(self.display, (SCREENINFO.RES[0] - SCREENINFO.RES[0]*0.05 - 65*(SCREENINFO.RES[0]*0.001), SCREENINFO.RES[1]*0.05), (65*(SCREENINFO.RES[0]*0.0013), 60*(SCREENINFO.RES[1]*0.002)), (255,255,0), (0,0,0), '', 'OptionMenu', 'Gear')
        self.item_list = [button_play, button_connection, button_quit, button_option]
        self.set_backgroud('Map')
