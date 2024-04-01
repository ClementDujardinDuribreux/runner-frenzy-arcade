import pygame
from Features.Entity import Entity

class Player(Entity):

    def __init__(self, speed_side:float, sprite:str):
        Entity.__init__(self, sprite)
        self.speed = 1
        self.speed_side = speed_side
        self.old_position = self.position.copy()
        self.current_time = pygame.time.get_ticks()
        self.last_update = pygame.time.get_ticks()
        self.animation_delay = 175
        self.animation_steps = 3
        self.frame = 0
        self.coord_list = []
        for x in range(self.animation_steps):
            self.coord_list.append(32*x)

    def set_animation_delay(self):
        if self.animation_delay > 75:
            self.animation_delay /= self.speed

    def set_current_time(self):
        self.current_time = pygame.time.get_ticks()
    
    def set_last_update(self, value):
        self.last_update = value

    def set_player_position(self, x, y):
        self.position = [x, y]
    
    def set_old_position(self):
        self.old_position = self.position.copy()

    def increment_speed(self):
        self.speed += 0.1

    def reverse_animation(self):
        list_reversed = []
        for coord in range(len(self.coord_list)-1, -1, -1):
            list_reversed.append(self.coord_list[coord])
        self.coord_list = list_reversed
    
    def reset_position(self):
        self.position[0]= self.old_position[0]
        self.rect.topleft = self.position
    
    def move_right(self): self.position[0] += self.speed_side

    def move_left(self): self.position[0] -= self.speed_side

    def move_forward(self): self.position[1] -= self.speed

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom
    
    def animation(self):
        if self.current_time - self.last_update >= self.animation_delay:
            self.frame += 1
            self.set_last_update(self.current_time)
            if self.frame >= self.animation_steps:
                self.frame = 0
                self.reverse_animation()
        self.image = self.get_image(self.coord_list[self.frame], 0)
        self.image.set_colorkey([0, 0, 0])

    def get_damage(self):
        self.health -= 1