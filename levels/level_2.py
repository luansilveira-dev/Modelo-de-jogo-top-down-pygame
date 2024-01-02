from classes.tileMap import *
from utils.map import mapLevel_2
from game.file import *
from classes.jogador import *
from classes.portas import *
from utils.conf import *
from classes.visual_effects import *



jogador = Jogador()




class Level_2:
    def __init__(self, janela):
        self.janela = janela
        self.todas_as_sprite = pygame.sprite.Group()
        self.listaImagem = [spritePiso, spriteParede, spriteParede2, spriteTetoW, spriteTetoD, spriteTetoA, spriteTetoS, spriteTetoQ, spriteTetoE]
        self.tile = TileMap(self.listaImagem, mapLevel_2, self.janela, 16*escalaTile)
        self.porta = Porta(LARGURA/1.11, ALTURA/2.90)
        self.todas_as_sprite.add(self.porta, jogador) 
        self.ambiente()



    def colisao_porta(self):
        global verificarPosicao
        
        collide = False
        if self.porta.rect_collide.colliderect(jogador.rect_collide):
            verificarPosicao = True
            collide = True

        #pygame.draw.rect(self.janela, (255, 0, 0), self.porta.rect_collide, 2) 
        #pygame.draw.rect(self.janela, (255, 0, 0), jogador.rect_collide, 2) 

        return collide

    def ambiente(self):
       
        for _ in range(particula):
            particle = Particula(random.randint(0, LARGURA), random.randint(0, ALTURA))
            self.todas_as_sprite.add(particle)   

        ambienteEscuro.set_alpha(transparecia) # definhir as transparência da superfices


    def run(self): 
        global verificarPosicao, nivelAtual, transparecia

        if verificarPosicao:
            jogador.rect.center = [LARGURA/3, 500]
            verificarPosicao = False

        ############# DESENHAR TILE MAPA  DO JOGO ####################
        self.tile.desenharTile()
        jogador_antigo_rect = jogador.rect.copy()
        ##############################################################

        ## LÓGICA 

        
        
        ### desenhar e atualizar o jogador ###
        self.todas_as_sprite.draw(self.janela)
        self.todas_as_sprite.update()
        #####################################
        
        if self.tile.verificarColisao(jogador.rect_collide):
            jogador.rect = jogador_antigo_rect 
            
    
        
    

