import os, sys, pygame

BASE_DIR = os.path.abspath('')
IMAGE_PATH = 'assets/1x/bomb50.png'


class Enemy(pygame.sprite.Sprite):
    
    """
    # use os.path.join to load files from subdirectories for portability
    # image.load returns a surface object
    """

    def __init__(self, screen_dims):
        self.surface = pygame.image.load(os.path.join(BASE_DIR, IMAGE_PATH))
        self.rect = self.surface.get_rect(center=(25, screen_dims[1] / 1.5))
        self.speed = [4, 0]

    def move(self):
        self.rect = self.rect.move(self.speed)