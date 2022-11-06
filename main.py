import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Éscape')


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

fps = 60
clock = pygame.time.Clock()
geschw = 3
player_pos_x = 380
player_pos_y = 230


class Map():
    def __init__(self) -> None:
        pass

def draw_map():
    pygame.draw.rect(DISPLAYSURF, BLACK, (400, 30, 20, 70), 40, 0)

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
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        gedrueckt = pygame.key.get_pressed()
        if gedrueckt[pygame.K_UP]:
            if border_tb(player_pos_y, 3):
                player_pos_y -= geschw
        if gedrueckt[pygame.K_RIGHT]:
            if border_lr(player_pos_x, 3):
                player_pos_x += geschw
        if gedrueckt[pygame.K_DOWN]:
            if border_tb(player_pos_y, -3):
                player_pos_y += geschw
        if gedrueckt[pygame.K_LEFT]:
            if border_lr(player_pos_x, -3):
                player_pos_x -= geschw
        
        DISPLAYSURF.fill(color=WHITE)

        pygame.draw.rect(DISPLAYSURF, BLACK, (player_pos_x, player_pos_y, 20, 20), 40, 0)
        # pygame.image.
        draw_map()

        pygame.display.flip()
        clock.tick(fps)
        print(player_pos_x, player_pos_y)
        pygame.display.update()
