import pygame
import settings


class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        # Start button properties
        self.start_button_area = pygame.draw.rect(self.screen, settings.BLACK,
                                                  (50, 270, 205, 32), 1)
        # Exit button properties
        self.exit_button_area = pygame.draw.rect(self.screen, settings.BLACK,
                                                 (50, 316, 70, 32))
        # Start button display
        self.font = pygame.font.Font('fonts/Paradigma Regular Trial.otf', 36)
        self.start_game_text = self.font.render('START GAME', True,
                                                (150, 90, 100, 50))
        self.screen.blit(self.start_game_text, dest=(50, 270))
        # Exit button display
        self.exit_game_text = self.font.render('EXIT', True,
                                               (150, 90, 100, 50))
        self.screen.blit(self.exit_game_text, dest=(50, 317))
        # Version button display
        self.font_small = pygame.font.Font(None, 14)
        self.version_text = self.font_small.render('version 1.0', True,
                                                   (150, 90, 100, 50))
        self.screen.blit(self.version_text, dest=(730, 630))
        # Tips
        self.font_small = pygame.font.Font('fonts/Gogh-ExtraBold.otf', 12)
        self.laser_text = self.font_small.render('Left Mouse Button  -  Laser', True,
                                                   (150, 90, 100, 50))
        self.screen.blit(self.laser_text, dest=(52, 210))
        self.font_small = pygame.font.Font('fonts/Gogh-ExtraBold.otf',
                                           12)
        self.boom_text = self.font_small.render('Right Mouse Button  -  BOOM',
                                                   True,
                                                   (150, 90, 100, 50))
        self.screen.blit(self.boom_text, dest=(52, 230))
