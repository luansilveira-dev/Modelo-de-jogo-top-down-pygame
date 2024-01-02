import pygame
from game.file import spritePorta

class Porta(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritePorta
        self.rect = self.image.get_rect()
        self.rect.center  = [x, y]

        self.rect_collide = self.rect.inflate(-10, -10)
        self.rect_collide.move_ip(1, y/y-30)


    def update(self):
        
        self.image = spritePorta
