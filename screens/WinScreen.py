import pygame
import settings


class WinScreen:
    TEXT_COLOR = (0, 140, 69)

    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font('fonts/Gogh-ExtraBold.otf', 24)
        if settings.STAGE == 'last_stage':
            you_win_text = self.font.render('YOU WIN', True, self.TEXT_COLOR)
            self.screen.blit(you_win_text, dest=(340, 300))
            # Restart button properties
            self.restart_button_area = pygame.draw.rect(self.screen,
                                                        settings.GREEN,
                                                        (311, 350, 165, 32), 1)
            # Restart button display
            self.restart_button_text = self.font.render('TRY AGAIN?', True,
                                                        self.TEXT_COLOR)
            self.screen.blit(self.restart_button_text, dest=(321, 350))
        else:
            you_win_text = self.font.render('LEVEL COMPLETED', True,
                                            self.TEXT_COLOR)
            self.screen.blit(you_win_text, dest=(279, 300))
            # Restart button properties
            self.next_stage_area = pygame.draw.rect(self.screen,
                                                    settings.GREEN,
                                                    (315, 350, 161, 32), 1)
            self.next_stage_text = self.font.render('NEXT LEVEL', True,
                                                    self.TEXT_COLOR)
            self.screen.blit(self.next_stage_text, dest=(321, 350))
