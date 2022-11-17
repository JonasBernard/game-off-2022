import pygame
import sys
from pygame.locals import QUIT
from constants import colors
from render_options import fps, clock
from player.player_options import geschw
from render_options import game_scale

class MainLoop:
    def __init__(self, player, DISPLAYSURF, moving_sprites):
        self.player = player
        self.DISPLAYSURF = DISPLAYSURF
        self.moving_sprites = moving_sprites


    def main_game(self):
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
                self.player.move_up(geschw)
                self.player.update_view(1)
            if gedrueckt[pygame.K_RIGHT]:
                # if border_lr(player.pos_x, 3):
                #     player.pos_x += geschw
                self.player.move_right(geschw)
                self.player.update_view(2)
            if gedrueckt[pygame.K_DOWN]:
                # if border_tb(player.pos_y, -3):
                #     player.pos_y += geschw
                self.player.move_down(geschw)
                self.player.update_view(0)
            if gedrueckt[pygame.K_LEFT]:
                # if border_lr(player.pos_x, -3):
                #     player.pos_x -= geschw
                self.player.move_left(geschw)
                self.player.update_view(3)
            
            self.DISPLAYSURF.fill(color=colors.WHITE)

            self.moving_sprites.draw(self.DISPLAYSURF)
            # pygame.image.
            # draw_map()

            pygame.display.flip()
            clock.tick(fps)
            # print(player_pos_x, player_pos_y)
            pygame.display.update()
