import pygame
import settings


class HealthBar(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((settings.HEALTH, 10))
        self.image.fill((194, 30, 86))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (10, 640)

    def update(self):
        if settings.HEALTH > 0:
            self.image = pygame.Surface((settings.HEALTH, 10))
            self.image.fill((194, 30, 86))
            self.rect = self.image.get_rect()
            self.rect.bottomleft = (10, 640)
        else:
            self.image = pygame.Surface((0, 0))
