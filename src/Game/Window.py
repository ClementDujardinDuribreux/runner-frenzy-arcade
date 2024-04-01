import pygame
from Features.Text import Text
from OPTIONS import *
from Features.Features import *
from Menu.GrapheMenu import GrapheMenu
from Web.Connexion.Sql import Sql
from Features.Video import Video

class Window:
    """
    Cette classe permet de creer la fenetre pygame associé au jeu
    """
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()
        if OPTIONS.SOUND_ON: pygame.mixer.music.set_volume(100.0)
        else: pygame.mixer.music.set_volume(0.0)
        if SCREENINFO.FULLSCREEN:
            self.display = pygame.display.set_mode(SCREENINFO.RES, pygame.FULLSCREEN)
        else : self.display = pygame.display.set_mode(SCREENINFO.RES)
        pygame.display.set_caption(" - PROJECT NSI TERMINALE - ", "")
        self.clock = pygame.time.Clock()
        self.display_options = [self.display]
        self.graphe_menu = GrapheMenu(True, self.display_options)
        self.scene = self.graphe_menu.get_scene()
        self.scene.play_music()
        Sql.open_bdd()
        video = Video('video/intro/img')
        video.add_sound('video/intro/src/audio+.mp3')
        video.set_volume(0.4)
        video.play(self.display, (0,0), SCREENINFO.RES[0], SCREENINFO.RES[1])

    def run(self):
        while self.graphe_menu.get_RUNNING():
            self.clock.tick(SCREENINFO.FPS)
            self.update()
            if type(self.scene).__name__ in ['SceneMenu', 'SceneAIMenu']:
                self.scene.run()
                self.scene.draw_items()
                if self.scene.dead:
                    self.graphe_menu.change_scene('DeathMenu')
            for event in pygame.event.get():
                self.scene.draw_items()
                self.update_item(event)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    if type(self.scene).__name__ is 'MainMenu':
                        self.graphe_menu.set_RUNNING_False()
                    elif type(self.scene).__name__ in ['SceneMenu', 'SceneAIMenu', 'PauseMenu']:
                        self.graphe_menu.pause_menu()
                    else:
                        self.graphe_menu.change_scene('MainMenu')
                if event.type == pygame.QUIT:
                    self.graphe_menu.set_RUNNING_False()
            pygame.display.flip()     
        Sql.close_bdd()
        pygame.quit()

    def update_item(self, event):
        if type(self.scene).__name__ not in ['SceneMenu', 'SceneAIMenu']:
            pass
        returns = self.scene.draw(event)
        for r in returns:
            self.graphe_menu.change_scene(r)
    
    def update(self):
        self.scene.draw_items()
        scene = self.scene
        scene_update = self.graphe_menu.get_scene()
        if scene is not scene_update:
            self.scene = scene_update
            self.scene.play_music()
            pygame.display.update()
            if not self.scene.has_background:
                self.scene.undraw()
            if type(self.scene).__name__ in ['PauseMenu', 'DeathMenu']:
                self.fill_transparent()

    def fill_transparent(self):
        surf = pygame.Surface(pygame.Rect((0, 0, SCREENINFO.RES[0], SCREENINFO.RES[1])).size, pygame.SRCALPHA)
        pygame.draw.rect(surf, (0,0,0,127), surf.get_rect())
        self.display.blit(surf, (0, 0, SCREENINFO.RES[0], SCREENINFO.RES[1]))