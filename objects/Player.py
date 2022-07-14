import pygame
import settings


class Player(pygame.sprite.Sprite):
    COLOR = settings.GREEN

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/player.png')
        self.image = pygame.transform.scale(self.image, (12, 12))
        self.rect = self.image.get_rect()
        self.rect.center = (settings.WIDTH / 2, settings.HEIGHT / 2)

    def move(self, x, y):
        self.rect.x = x - 16 / 2
        self.rect.y = y - 16 / 2
