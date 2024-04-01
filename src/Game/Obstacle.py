from Features.Entity import Entity

class Obstacle(Entity):

    def __init__(self, sprite, x_sprite = 32, y_sprite = 32):
        Entity.__init__(self, sprite, x_sprite, y_sprite)
        self.sprite = sprite

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom