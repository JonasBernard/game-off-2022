import pygame, sys
from pygame.locals import *
from class_player import Player
from menu.menu import MainMenu
from render_options import fps, clock
from constants.colors import WHITE, BLACK

pygame.init()

DISPLAYSURF = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Éscape')


geschw = 3
player_pos_x = 380
player_pos_y = 230


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

def main_game():
    while True:
        events = pygame.event.get()

        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        gedrueckt = pygame.key.get_pressed()
        if gedrueckt[pygame.K_UP]:
            # if border_tb(player.pos_y, 3):
            #     player.pos_y += geschw
            player.move_up(geschw)
            player.update_view(1)
        if gedrueckt[pygame.K_RIGHT]:
            # if border_lr(player.pos_x, 3):
            #     player.pos_x += geschw
            player.move_right(geschw)
            player.update_view(2)
        if gedrueckt[pygame.K_DOWN]:
            # if border_tb(player.pos_y, -3):
            #     player.pos_y += geschw
            player.move_down(geschw)
            player.update_view(0)
        if gedrueckt[pygame.K_LEFT]:
            # if border_lr(player.pos_x, -3):
            #     player.pos_x -= geschw
            player.move_left(geschw)
            player.update_view(3)
        
        DISPLAYSURF.fill(color=WHITE)

        moving_sprites.draw(DISPLAYSURF)
        # pygame.image.
        # draw_map()

        pygame.display.flip()
        clock.tick(fps)
        # print(player_pos_x, player_pos_y)
        pygame.display.update()


if __name__ == '__main__':
    player = Player(380, 230)
    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(player)
    
    menu = MainMenu()
    menu.init(DISPLAYSURF, main_game)

    menu.menu_loop()
