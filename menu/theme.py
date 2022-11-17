from pygame_menu.themes import THEME_DARK
import pygame_menu
from constants import colors


menu_theme = THEME_DARK.copy()
menu_theme.background_color=colors.DARK_BLUE
menu_theme.title_background_color=colors.LIGHT_BLUE
menu_theme.border_color = colors.MID_BLUE
menu_theme.border_width = 3
menu_theme.scrollbar_thick = 3

menu_theme.title_font_shadow = False
menu_theme.title_font = pygame_menu.font.FONT_MUNRO

menu_theme.width_font = pygame_menu.font.FONT_MUNRO
menu_theme.widget_padding = 20
menu_theme.widget_selection_color = colors.MID_GREEN

menu_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_UNDERLINE
