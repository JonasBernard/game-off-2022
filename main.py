import pygame
from pygame.locals import *
from player.player import Player
from menu.menu import MainMenu
from game.mainloop import MainLoop

pygame.init()

DISPLAYSURF = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Éscape')


class Map():
    def __init__(self) -> None:
        pass

def draw_map():
    # pygame.draw.rect(DISPLAYSURF, BLACK, (400, 30, 20, 70), 40, 0)
    floor = pygame.image.load(r'assets/floor.png').get_rect()
    pygame.draw.rect(DISPLAYSURF, floor)

def border_tb(pp, direction):
    if pp + direction <= -3 or pp + direction >= 480:
        return False
    else:
        return True

def border_lr(pp, direction):
    if pp + direction <= -3 or pp + direction >= 785:
        return False
    else:
        return True

    # if pp + direction <= 400:
    #     return True
    # else:
    #     return False


if __name__ == '__main__':
    player = Player(380, 230)
    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(player)
    
    main_game_loop = MainLoop(player, DISPLAYSURF, moving_sprites)

    menu = MainMenu()
    menu.init(DISPLAYSURF, main_game_loop.main_game)

    menu.menu_loop()
