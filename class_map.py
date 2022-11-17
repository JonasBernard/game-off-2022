import pygame, sys
from pygame.locals import *

class Map(pygame.sprite.Sprite):
    def __init__(self, felder_anzahl):
        super().__init__()
        self.felder_anzahl = felder_anzahl

        self.sprites = []

class Floor(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprite = pygame.image.load('r(assert/floor.png)')
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

class Wall(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprite = pygame.image.load('r(assert/wall.png)')
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]