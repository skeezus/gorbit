import os, sys, pygame

BASE_DIR = os.path.abspath('')
IMAGE_PATH = 'assets/1x/trex100.png'


class Hero(pygame.sprite.Sprite):
    
    """
    # use os.path.join to load files from subdirectories for portability
    # image.load returns a surface object
    """

    def __init__(self, screen_dims):
        self.surface = pygame.image.load(os.path.join(BASE_DIR, IMAGE_PATH))
        self.rect = self.surface.get_rect(center=(screen_dims[0] / 2, screen_dims[1] / 1.5))
        self.speed = [0, 2]

    def move(self):
        self.rect = self.rect.move(self.speed)