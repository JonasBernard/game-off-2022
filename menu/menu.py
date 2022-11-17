import pygame_menu
import pygame
from render_options import fps, clock

class MainMenu:
    def set_difficulty(self, value, difficulty):
        # Do the job here !
        pass

    def start_the_game(self):
        self.close()

    def init(self, DISPLAYSURF, game_loop):
        self.menu = pygame_menu.Menu('Main Menu', 400, 300,
                            theme=pygame_menu.themes.THEME_DARK)
        self.DISPALYSURF = DISPLAYSURF

        self.menu.add.text_input('Name: ', default='John Doe')
        self.menu.add.button('Play', game_loop)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)

        # self.menu.mainloop(DISPLAYSURF)

    def open(self):
        self.menu.enable()

    def close(self):
        self.menu.disable()

    def menu_loop(self):
        while True:
            events = pygame.event.get()
            if self.menu.is_enabled():
                self.menu.update(events)
                self.menu.draw(self.DISPALYSURF)

            pygame.display.flip()
            clock.tick(fps)
            # print(player_pos_x, player_pos_y)
            pygame.display.update()
