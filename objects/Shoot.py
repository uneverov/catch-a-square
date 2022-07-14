import random

import pygame
import settings
from core.Music_Changer import rocket_sound, laser_sound


def singleton(class_):
    def getinstance(*args, **kwargs):
        if kwargs['type'] == 'rocket':
            if class_ not in settings.ROCKET:
                settings.ROCKET[class_] = class_(*args, **kwargs)
            return settings.ROCKET[class_]
        if kwargs['type'] == 'laser':
            if class_ not in settings.LASER:
                settings.LASER[class_] = class_(*args, **kwargs)
            return settings.LASER[class_]

    return getinstance


@singleton
class Rocket:
    def __init__(self, screen, type=''):
        self.type = type
        self.radius = 50
        rocket_sound()
        self.screen = screen
        self.range = 0
        self.mouse_position = pygame.mouse.get_pos()

    def __call__(self):
        self.range += 0.6
        self.rocket = pygame.draw.circle(self.screen,
                                         random.choice(settings.COLORS),
                                         (self.mouse_position[0],
                                          self.mouse_position[1]),
                                         5 + self.range)


@singleton
class Laser:
    def __init__(self, screen, type=''):
        self.type = type
        laser_sound()
        self.range = 0
        self.screen = screen
        self.mouse_position = pygame.mouse.get_pos()
        self.laser = pygame.draw.rect(self.screen,
                                      random.choice(settings.COLORS),
                                      (settings.WIDTH - self.range,
                                       self.mouse_position[1],
                                       20,
                                       5))

    def __call__(self):
        self.laser = pygame.draw.rect(self.screen,
                                      random.choice(settings.COLORS),
                                      (settings.WIDTH - self.range,
                                       self.mouse_position[1],
                                       20,
                                       5))
        self.range += 12