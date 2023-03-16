import pygame


def main_theme():
    pygame.mixer.fadeout(1)
    pygame.mixer.Channel(1).set_volume(0.1)
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(
        'sounds/Enigma-Long-Version-Complete-Version.mp3'), loops=-1)


def menu_button_sound():
    pygame.mixer.Channel(0).set_volume(1)
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(
        'sounds/menu_button_sound.mp3'))


def rocket_sound():
    pygame.mixer.Channel(2).set_volume(0.5)
    pygame.mixer.Channel(2).play(pygame.mixer.Sound(
        'sounds/zvuk2.ogg'))


def laser_sound():
    pygame.mixer.Channel(4).set_volume(0.2)
    pygame.mixer.Channel(4).play(pygame.mixer.Sound(
        'sounds/laser.mp3'))


def kill_sound():
    pygame.mixer.Channel(0).set_volume(0.15)
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(
        'sounds/kill_enemy.ogg'))


def fail_sound():
    pygame.mixer.Channel(3).set_volume(0.1)
    pygame.mixer.Channel(3).play(pygame.mixer.Sound(
        'sounds/fail_sound.ogg'))
