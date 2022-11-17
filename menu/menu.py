import pygame_menu
import pygame
from render_options import fps, clock
from constants.colors import BLUE_GREY
from menu.theme import menu_theme

class MainMenu:
    def init(self, DISPLAYSURF, game_loop):
        self.menu = pygame_menu.Menu('Main Menu', 500, 400,
                            theme=menu_theme)
        self.DISPLAYSURF = DISPLAYSURF

        self.menu.add.button('Play', game_loop)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)

        # self.menu.mainloop(DISPLAYSURF)

    def menu_loop(self):
        while True:
            self.DISPLAYSURF.fill(color=BLUE_GREY)

            events = pygame.event.get()
            if self.menu.is_enabled():
                self.menu.update(events)
                self.menu.draw(self.DISPLAYSURF)

            pygame.display.flip()
            clock.tick(fps)
            # print(player_pos_x, player_pos_y)
            pygame.display.update()
