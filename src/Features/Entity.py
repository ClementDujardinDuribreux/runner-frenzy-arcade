import pygame

class Entity(pygame.sprite.Sprite):

    def __init__(self, sprite, x_sprite=32, y_sprite=32, x=0, y=0):
        super().__init__()
        self.dimension_x = x_sprite
        self.dimension_y = y_sprite
        self.sprite_sheet = pygame.image.load(sprite)
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.feet = pygame.Rect(0, 0, self.rect.width - 6, 10)

    def get_image(self, x, y):
        image = pygame.Surface([self.dimension_x, self.dimension_y])
        image.blit(self.sprite_sheet, (0, 0), (x, y, self.dimension_x, self.dimension_y))
        return image
    
    def set_entity_spawn(self, x, y):
        self.position = [x-16, y]