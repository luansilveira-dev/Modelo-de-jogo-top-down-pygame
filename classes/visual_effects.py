import pygame
import random
from utils.const import LARGURA, ALTURA, BRANCO


class Particula(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((random.randint(1, 15), random.randint(1, 2)))
        self.image.fill(BRANCO)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = random.randint(1, 5)
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > ALTURA:
            self.rect.y = 0
            self.rect.x  = random.randint(0, LARGURA)
    
        
