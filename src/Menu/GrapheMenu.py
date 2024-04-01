import pygame
from OPTIONS import *
from Menu.SD.Graphe import Graphe
from Menu.SD.Pile import Pile
from Menu.MainMenu import MainMenu
from Web.Connexion.WindowConnection import WindowConnection
from Menu.SceneMenu import SceneMenu
from Menu.PauseMenu import PauseMenu
from Menu.OptionMenu import OptionMenu
from Menu.DeathMenu import DeathMenu

class GrapheMenu(Graphe):

    """
    Cette classe permet de creer un graphe qui centralise tous le menus et les connectent entre eux
    """

    def __init__(self, oriente:bool, args):
        Graphe.__init__(self, oriente)
        self.RUNNING = True
        self.args = args
        self.display = args[0]
        self.draw_PauseMenu = False
        self.dico_menu = {'MainMenu':MainMenu(args), 
                          'SceneMenu':SceneMenu(args),
                          'PauseMenu':PauseMenu(args), 
                          'OptionMenu':OptionMenu(args),
                          'DeathMenu':DeathMenu(args)}
        for i in self.dico_menu.values():
            self.ajouter_sommet(i)
        self.ajouter_arete(self.dico_menu['MainMenu'], self.dico_menu['SceneMenu'])
        self.ajouter_arete(self.dico_menu['MainMenu'], self.dico_menu['OptionMenu'])
        self.ajouter_arete(self.dico_menu['OptionMenu'], self.dico_menu['MainMenu'])
        self.ajouter_arete(self.dico_menu['SceneMenu'], self.dico_menu['MainMenu'])
        self.ajouter_arete(self.dico_menu['SceneMenu'], self.dico_menu['DeathMenu'])
        self.ajouter_arete(self.dico_menu['DeathMenu'], self.dico_menu['SceneMenu'])
        self.ajouter_arete(self.dico_menu['DeathMenu'], self.dico_menu['MainMenu'])
        self.ajouter_arete(self.dico_menu['PauseMenu'], self.dico_menu['SceneMenu'])
        self.ajouter_arete(self.dico_menu['PauseMenu'], self.dico_menu['MainMenu'])

        self.pile_menu = Pile()
        self.scene = self.dico_menu['MainMenu']

    def get_scene(self):
        return self.scene
    
    def get_RUNNING(self):
        return self.RUNNING
    
    def set_RUNNING_False(self):
        self.RUNNING = False

    def change_scene(self, retour_boutton:str):
        if retour_boutton is None:
            return None
        if retour_boutton is 'Quit':
            self.set_RUNNING_False()
        elif retour_boutton is 'Back':
            self.scene = self.dico_menu[self.pile_menu.depiler()]
            self.draw_PauseMenu = False
        elif retour_boutton is 'Restart':
            self.draw_PauseMenu = False
            self.scene.stop_music()
            self.scene = self.dico_menu['SceneMenu']
            self.scene.restart()
        elif retour_boutton is 'Connection':
            self.win_connect = WindowConnection()
            pass
        elif retour_boutton is 'Fullscreen':
            SCREENINFO.switch_FULLSCREEN()
            SCREENINFO.set_RES((720,450))
            if SCREENINFO.FULLSCREEN : self.display = pygame.display.set_mode(SCREENINFO.RES, pygame.FULLSCREEN)
            else: self.display = pygame.display.set_mode(SCREENINFO.RES)
            for scene in self.dico_menu.values():
                scene.re_init()
        elif retour_boutton is 'Sound':
            OPTIONS.switch_sound()
            self.dico_menu['OptionMenu'].re_init()
            if OPTIONS.SOUND_ON:
                pygame.mixer.music.set_volume(0.05)
            else: pygame.mixer.music.set_volume(0.0)
        elif self.dico_menu[retour_boutton] in self.get_dico()[self.dico_menu[type(self.scene).__name__]]:
            if retour_boutton is 'MainMenu':
                self.dico_menu['SceneMenu'].restart()
            if type(self.scene).__name__ is 'PauseMenu' and retour_boutton is 'SceneMenu':
                self.pause_menu()
            else:
                self.draw_PauseMenu = False
                self.pile_menu.empiler(type(self.scene).__name__)
                self.scene = self.dico_menu[retour_boutton]
                self.scene.stop_music()

    def pause_menu(self):
        if self.draw_PauseMenu:
            self.dico_menu['SceneMenu'].unpause()
            self.draw_PauseMenu = False
            self.scene = self.dico_menu[self.pile_menu.depiler()]
            self.scene.unpause_music()
        else:
            self.dico_menu['SceneMenu'].pause()
            self.draw_PauseMenu = True
            self.pile_menu.empiler(type(self.scene).__name__)
            self.scene = self.dico_menu['PauseMenu']
            self.scene.pause_music()