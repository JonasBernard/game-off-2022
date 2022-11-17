from render_options import game_scale
from util.image import rescale
import pygame

def importimage(path):
    image = pygame.image.load(path)
    return rescale(image, game_scale)