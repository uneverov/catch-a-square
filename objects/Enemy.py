import pygame
import settings

from core.Music_Changer import fail_sound


def enemy_count_display(screen):
    pygame.font.init()
    font = pygame.font.Font('fonts/Gogh-ExtraBold.otf', 20)
    enemy_count_text = font.render(str(settings.ENEMY), True,
                                   (93, 94, 0, 0))
    screen.blit(enemy_count_text, dest=(40, 9))
    image = pygame.image.load('images/enemy.png')
    image = pygame.transform.scale(image, (21, 25))
    image_r = pygame.transform.rotate(image, 90)
    screen.blit(image_r, (10, 10))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/enemy.png')
        self.image = pygame.transform.scale(self.image, (31, 38))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.x += 2.8
        if self.rect.left > settings.WIDTH and self.image.get_size() == (
                31, 38):
            self.image = pygame.Surface((0, 0)).convert_alpha()
            settings.ENEMY -= 1
            settings.HEALTH -= 75
            if settings.HEALTH > 0:
                fail_sound()
