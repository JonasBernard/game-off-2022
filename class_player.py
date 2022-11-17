import pygame, sys
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprite = []
        self.sprite.append(pygame.image.load(r'assets/character/front.png'))
        self.sprite.append(pygame.image.load(r'assets/character/back.png'))
        self.sprite.append(pygame.image.load(r'assets/character/left.png'))
        self.sprite.append(pygame.image.load(r'assets/character/right.png'))
        self.current_sprite = 0
        self.image = self.sprite[self.current_sprite]

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update_view(self, dr):
        self.current_sprite = dr
        self.image = self.sprite[self.current_sprite]

    def move_right(self, step):
        self.pos_x += step
        self.rect.topleft = [self.pos_x, self.pos_y]

    def move_left(self, step):
        self.pos_x -= step
        self.rect.topleft = [self.pos_x, self.pos_y]

    def move_up(self, step):
        self.pos_y -= step
        self.rect.topleft = [self.pos_x, self.pos_y]

    def move_down(self, step):
        self.pos_y += step
        self.rect.topleft = [self.pos_x, self.pos_y]