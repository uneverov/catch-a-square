import pygame
import settings

import core.Music_Changer as Music_Changer
from core.Stage_Changer import GameStage

# Init game
pygame.init()
Music_Changer.main_theme()
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption("catch a square")
game_stage = GameStage(screen)
clock = pygame.time.Clock()
# Group sprites
while settings.running:
    pygame.display.update()
    clock.tick(settings.FPS)
    game_stage.stage_manager()

