import random
from pygame.sprite import Sprite


class PowerUp(Sprite):
    def __init__(self,image,type):
        self.image = image
        self.rect=self.image.get_rect()
        self.rect.x=random.randint(800, 900)
        self.rect.y=random.randint(100, 150)
        self.type = type
        self.start_type=0

    def update(self, game_speed, power_ups):
        self.rect.x -=game_speed
        if self.rect.x <-self.rect.width:
            power_ups.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)