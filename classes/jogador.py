import pygame
from game.file import spriteParadoFrente, spriteAndarFrente, spriteAndarCosta, spriteAndarLado, spriteParadoCosta

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        ############ Lista de Animações #######
        self.escala = 3.2
        ##### animações do personagem Parado
        self.paradoFrente = [pygame.transform.scale(spriteParadoFrente.subsurface(32*i, 0, 32, 32), (32*self.escala, 32*self.escala)) for i in range(10)]
        self.paradoCosta = [pygame.transform.scale(spriteParadoCosta.subsurface(32*i, 0, 32, 32), (32*self.escala, 32*self.escala)) for i in range(10)]


        ##### animações do jogador em movimentos
        self.andarFrente = [pygame.transform.scale(spriteAndarFrente.subsurface(32*i, 0 , 32, 32), (32*self.escala, 32*self.escala)) for i in range(8)] 
        self.andarCosta = [pygame.transform.scale(spriteAndarCosta.subsurface(32*i, 0 , 32, 32), (32*self.escala, 32*self.escala)) for i in range(8)]
        self.andarLado = [pygame.transform.scale(spriteAndarLado.subsurface(32*i, 0, 32, 32), (32*self.escala, 32*self.escala)) for i in range(8)]
        ######################################

        self.indexLista = 0
        self.estado = 'PARADO'
        self.image = self.paradoFrente[self.indexLista]
        self.rect = self.image.get_rect()
        self.rect.center = (200, 200)
        self.frema = 9
        self.invertida, self.frente  = False, True
        self.velocidade = 12
        self.velAnima = .3


    def moverJogador(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.invertida = False
            self.estado = 'ANDANDO_LADO'
            self.frema = 7
            self.rect.x += self.velocidade

        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.invertida = True
            self.estado = 'ANDANDO_LADO'
            self.frema = 7
            self.rect.x -= self.velocidade

        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.frente = True
            self.frema = 7
            self.estado = 'ANDANDO'
            self.rect.y += self.velocidade
        elif keys[pygame.K_w] or keys[pygame.K_UP]:
            self.frente = False
            self.frema = 7
            self.estado = 'ANDANDO'
            self.rect.y -= self.velocidade
        
        else:
            self.estado = 'PARADO'
    

    def animarJogador(self):
        if self.indexLista > self.frema:
            self.indexLista = 0

        if self.estado == 'ANDANDO': 
            if self.frente:
                self.image = self.andarFrente[int(self.indexLista)]
            if not self.frente:
                self.image = self.andarCosta[int(self.indexLista)]
        
        elif self.estado == 'ANDANDO_LADO':
            if self.invertida:
                self.image = pygame.transform.flip(self.andarLado[int(self.indexLista)], True, False)
            if not self.invertida:
                self.image = self.andarLado[int(self.indexLista)]

        
        elif self.estado == 'PARADO':
            if self.frente:
                self.image = self.paradoFrente[int(self.indexLista)]
            else:
                self.image = self.paradoCosta[int(self.indexLista)]
        
        
        self.indexLista += self.velAnima

    def update(self):
        self.moverJogador()
        self.animarJogador()
        self.rect_collide = self.rect.inflate(-40, -24)
        self.rect_collide.move_ip(1, 10)


