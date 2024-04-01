import pygame
from Game.Player import Player
from Game.Obstacle_Area import Obstacle_Area
from Game.Map import Map
from Features.Text import Text
from OPTIONS import *
from Web.Connexion.Sql import Sql

class Game:

    def __init__(self, args):
        self.screen = args[0]
        self.score = 0
        self.player = Player(2.5, "sprites/character.png")
        self.speed = self.player.speed
        self.is_pause = False
        self.map = Map("tile/map_test.tmx", self.screen)
        self.spawn_position = [self.map.get_spawn_point().x, self.map.get_spawn_point().y]
        self.player.set_entity_spawn(self.spawn_position[0], self.spawn_position[1] + 70)
        self.area_obstacle_list = []
        self.dead = False
        self.is_increment = False
        self.text_score = Text(self.screen, str(self.score), (75 * (SCREENINFO.RES[0]/720), 20 * (SCREENINFO.RES[0]/720)), 100 * (SCREENINFO.RES[0]/720), (255,255,255))
        for area in self.map.get_obstacle_area():
            new_area = Obstacle_Area(self.map, area.y, area.height)
            self.area_obstacle_list.append(new_area)
        self.map.add_in_group(self.player)

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
            pass
        elif keys[pygame.K_RIGHT]:
            self.player.move_right()
        elif keys[pygame.K_LEFT]:
            self.player.move_left()

    def set_camera_pos(self):
        if self.player.position[1] >= self.spawn_position[1]:
            self.map.group.center((self.spawn_position[0], self.spawn_position[1]))
        self.map.group.center((self.spawn_position[0], self.player.position[1]-40))

    def increment_score(self):
        self.score += 1
        self.text_score.set_text(str(self.score))
    
    def refresh_area(self):
        for area in self.area_obstacle_list:
            area.delete_obstacles()
            area.generate_obstacles()

    def pause(self):
        self.is_pause = True
        self.speed = self.player.speed
        self.player.speed = 0

    def unpause(self):
        self.is_pause = False
        self.player.speed = self.speed

    def update(self):
        self.map.group.update()
        for sprite in self.map.group.sprites():
            if sprite == self.player:
                if sprite.rect.collidelist(self.map.get_collision_object()) > -1:
                    sprite.reset_position()
                if sprite.rect.collidelist(self.map.get_respawn_obj()) > -1:
                    sprite.set_player_position(self.player.position[0], self.spawn_position[1])
                    self.player.increment_speed()
                    self.player.set_animation_delay()
                    self.refresh_area()
                for area in self.area_obstacle_list:
                    if sprite.feet.collidelist(area.get_obstacle_list()) > -1:
                        self.dead = True
                        if Sql.connected:
                            Sql.add_score(self.score)
                if sprite.feet.collidelist(self.map.get_obstacle_area()) > -1:
                    if self.is_increment == False:
                        self.increment_score()
                        self.is_increment = True
                else: self.is_increment = False


    def restart(self):
        self.refresh_area()
        self.player.set_player_position(self.spawn_position[0]-16, self.spawn_position[1]+70)
        self.player.speed = 1

    def run(self):
        self.map.group.draw(self.screen)
        self.player.move_forward()
        self.set_camera_pos()
        self.update()
        self.player.set_old_position()
        if not self.is_pause:
            self.handle_keys()
            self.player.animation()
        self.player.set_current_time()
        self.text_score.draw()
        pygame.display.flip()