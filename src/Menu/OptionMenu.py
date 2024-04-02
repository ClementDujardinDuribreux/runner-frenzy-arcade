from Menu.Menu import *
from Features.Button import Button
from Features.Text import Text


class OptionMenu(Menu):

    """
    Cette classe permet de creer le menu d'options
    """

    def __init__(self, args: list) -> None:
        super().__init__(args)
        button_back = Button(self.display, (SCREENINFO.RES[0]*0.05, SCREENINFO.RES[1]*0.05), (65*(SCREENINFO.RES[0]*0.0013), 60*(SCREENINFO.RES[1]*0.002)), (255,255,0), (0,0,0), '', 'MainMenu', 'Arrow_b')
        button_fullscreen = Button(self.display, (SCREENINFO.RES[0]*0.2, SCREENINFO.RES[1]*0.25), (SCREENINFO.RES[0]*0.5, SCREENINFO.RES[1]*0.15), (255,255,0), (0,0,0), 'FULLSCREEN', 'Fullscreen')
        if SCREENINFO.FULLSCREEN: text = 'ON'
        else : text = 'OFF'
        if OPTIONS.SOUND_ON: image_sound = 'Sound_On'
        else : image_sound = 'Sound_Off'
        button_sound = Button(self.display, (SCREENINFO.RES[0]*0.2, SCREENINFO.RES[1]*0.45), (SCREENINFO.RES[0]*0.65, SCREENINFO.RES[1]*0.15), (255,255,0), (0,0,0), 'MUSIQUES', 'Sound', image_sound)
        text_fullscreen_on_off = Text(self.display, '('+text +')', (SCREENINFO.RES[0]*0.72, SCREENINFO.RES[1]*0.26), SCREENINFO.RES[0]*0.05)
        self.item_list = [button_back, button_fullscreen, button_sound, text_fullscreen_on_off]
        self.set_backgroud('Map')
        self.set_initial_select(1)
        self.make_button_list()