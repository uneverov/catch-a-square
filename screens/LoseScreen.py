import pygame
import settings


class LoseScreen:
    TEXT_COLOR = (0, 140, 69)
    running = True

    def __init__(self, screen):
        self.screen = screen
        # Game over text
        self.font = pygame.font.Font('fonts/Gogh-ExtraBold.otf', 24)
        self.game_over_text = self.font.render('GAME OVER', True,
                                               self.TEXT_COLOR)
        self.screen.blit(self.game_over_text, dest=(320, 300))
        # Restart button properties
        self.restart_button_area = pygame.draw.rect(self.screen,
                                                    settings.GREEN,
                                                    (311, 350, 165, 32), 1)
        # Restart button display
        self.restart_button_text = self.font.render('TRY AGAIN?', True,
                                                    self.TEXT_COLOR)
        self.screen.blit(self.restart_button_text, dest=(321, 350))
