from random import randrange as r

import pygame
import settings
from core.Music_Changer import kill_sound, menu_button_sound
import core.Stage_Changer as Stage_Changer

from objects.Enemy import Enemy, enemy_count_display
from objects.HealthBar import HealthBar
from objects.Player import Player
from objects.Shoot import Rocket, Laser
from screens.LoseScreen import LoseScreen
from screens.WinScreen import WinScreen


def singleton(class_):
    def getinstance(*args, **kwargs):
        if class_ not in settings.instances:
            settings.instances[class_] = class_(*args, **kwargs)
        return settings.instances[class_]

    return getinstance


@singleton
class SecondStage:
    def __init__(self, screen):
        self.laser = None
        self.rocket = None
        self.screen = screen
        self.player_sprite, self.enemy, self.healthbar_sprite = (
            [pygame.sprite.Group() for _ in range(3)])
        self.player = Player()
        self.healthbar = HealthBar()
        enemies = ([Enemy(r(-3700, 50), r(50, 600), self.screen)
                    for _ in range(0, settings.ENEMY)])
        self.player_sprite.add(self.player)
        self.enemy.add(*enemies)
        self.healthbar_sprite.add(self.healthbar)

    def play(self, events):
        self.enemy.update()
        self.healthbar_sprite.update()
        # Quit game
        for event in events:
            if event.type == pygame.QUIT:
                settings.running = False
        # player_moves
        self.change_player_pos(events)
        # Rendering
        self.screen.fill(settings.BLACK)
        enemy_count_display(self.screen)
        self.player_sprite.draw(self.screen)
        self.enemy.draw(self.screen)
        self.healthbar_sprite.draw(self.screen)
        # Kill enemy
        self.kill_enemy(events)
        # Lose_screen
        if settings.HEALTH < 0:
            lose_screen = LoseScreen(self.screen)
            for event in events:
                if event.type == pygame.QUIT:
                    settings.running = False
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if lose_screen.restart_button_area.collidepoint(event.pos):
                        menu_button_sound()
                        Stage_Changer.restart_game()

        # Win_screen
        if settings.ENEMY <= 0 and settings.HEALTH > 0:
            win_screen = WinScreen(self.screen)
            for event in events:
                if event.type == pygame.QUIT:
                    settings.running = False
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if win_screen.next_stage_area.collidepoint(event.pos):
                        menu_button_sound()
                        Stage_Changer.second_stage()

    def change_player_pos(self, events):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                mouse_position = pygame.mouse.get_pos()
                self.player.move(mouse_position[0], mouse_position[1])

    def kill_enemy(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                self.rocket = Rocket(self.screen, type='rocket')
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.laser = Laser(self.screen, type='laser')
        if self.rocket:
            hits_rocket = []
            if self.rocket.radius >= self.rocket.range:
                self.rocket()
                for k in self.enemy.spritedict.keys():
                    if self.rocket.rocket.colliderect(k):
                        hits_rocket.append(k)
            else:
                settings.ROCKET = {}
            if hits_rocket:
                for _ in hits_rocket:
                    self.enemy.remove(_)
                    settings.ENEMY -= 1
                    kill_sound()
        if self.laser:
            hits_laser = []
            if self.laser.laser.x > 0:
                self.laser()
                for k in self.enemy.spritedict.keys():
                    if self.laser.laser.colliderect(k):
                        hits_laser.append(k)
            else:
                settings.LASER = {}
            if hits_laser:
                for _ in hits_laser:
                    self.enemy.remove(_)
                    settings.ENEMY -= 1
                    kill_sound()
                    self.laser = None
                    settings.LASER = {}

