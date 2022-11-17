import pygame

def rescale(image, factor):
    size = image.get_size()
    return pygame.transform.scale(image, (int(size[0]*factor), int(size[1]*factor)))