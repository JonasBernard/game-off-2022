import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Éscape')


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprite = []
        self.sprite.append(pygame.image.load(r'assets/character/front.png'))
        self.current_sprite = 0
        self.image = self.sprite[self.current_sprite]

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

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

    sprite = []
    sprite.append(pygame.image.load(r'assets/character/front.png'))
    current_sprite = 0
    image = sprite[current_sprite]
    image = image.get_rect()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        gedrueckt = pygame.key.get_pressed()
        if gedrueckt[pygame.K_UP]:
            if border_tb(player.pos_y, 3):
                player.pos_y += geschw
        if gedrueckt[pygame.K_RIGHT]:
            if border_lr(player.pos_x, 3):
                player.pos_x += geschw
        if gedrueckt[pygame.K_DOWN]:
            if border_tb(player.pos_y, -3):
                player.pos_y += geschw
        if gedrueckt[pygame.K_LEFT]:
            if border_lr(player.pos_x, -3):
                player.pos_x -= geschw
        
        DISPLAYSURF.fill(color=WHITE)

        pygame.draw.rect(DISPLAYSURF, image, (player_pos_x, player_pos_y, 20, 20), 40, 0)
        # moving_sprites.draw(DISPLAYSURF)
        # pygame.image.
        # draw_map()

        pygame.display.flip()
        clock.tick(fps)
        # print(player_pos_x, player_pos_y)
        pygame.display.update()
