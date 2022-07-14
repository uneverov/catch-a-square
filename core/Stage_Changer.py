import pygame
import settings
from screens.FirstStage import FirstStage
from screens.SecondStage import SecondStage
from screens.StartScreen import StartScreen

from core.Music_Changer import menu_button_sound


def restart_game():
    settings.instances = {}
    settings.ENEMY = 50
    settings.HEALTH = 780
    settings.STAGE = 0


def first_stage():
    settings.ENEMY = 50
    settings.STAGE = 1


def second_stage():
    settings.ENEMY = 60
    settings.HEALTH = 780
    settings.STAGE = 2


class GameStage:
    def __init__(self, screen):
        self.screen = screen

    def intro(self, events):
        pygame.mouse.set_visible(True)
        self.screen.fill(settings.BLACK)
        s = StartScreen(self.screen)
        for event in events:
            # Start game
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if s.start_button_area.collidepoint(event.pos):
                    menu_button_sound()
                    first_stage()
            # Quit game
            if event.type == pygame.QUIT:
                settings.running = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if s.exit_button_area.collidepoint(event.pos):
                    settings.running = False

    def first_stage(self, events):
        pygame.mouse.set_visible(False)
        stage_1 = FirstStage(self.screen)
        stage_1.play(events)

    def second_stage(self, events):
        pygame.mouse.set_visible(False)
        stage_2 = SecondStage(self.screen)
        stage_2.play(events)

    def stage_manager(self):
        events = pygame.event.get()
        if settings.STAGE == 0:
            self.intro(events)
        if settings.STAGE == 1:
            self.first_stage(events)
        if settings.STAGE == 2:
            self.second_stage(events)
