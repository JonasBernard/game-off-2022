import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Hello World!')


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

fps = 60
clock = pygame.time.Clock()
geschw = 3
x = 200
y = 150

if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        gedrueckt = pygame.key.get_pressed()
        if gedrueckt[pygame.K_UP]:
            y -= geschw
        if gedrueckt[pygame.K_RIGHT]:
            x += geschw
        if gedrueckt[pygame.K_DOWN]:
            y += geschw
        if gedrueckt[pygame.K_LEFT]:
            x -= geschw
        
        DISPLAYSURF.fill(color=WHITE)

        pygame.draw.rect(DISPLAYSURF, BLACK, (x, y, 20, 20), 40, 0)

        pygame.display.flip()
        clock.tick(fps)

        pygame.display.update()
