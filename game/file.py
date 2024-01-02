from utils.const import *
import pygame
import os 

#################### Busca de diretorios ##############
pastaImgens = os.path.join(os.getcwd(), 'imagens')
pastaImagens_TileMap = os.path.join(os.getcwd(), 'imagens/tileMap') ### Mapa 
pastaImagens_Jogador = os.path.join(os.getcwd(), 'imagens/jogador')  ## Jogador
pastaImagens_Inimigos = os.path.join(os.getcwd(), 'imagens/inimigos') ## Inimigos


########################################################
ambienteEscuro = pygame.Surface((LARGURA+500, ALTURA+500)) # Criando anbientação/ definir tamanho 

imagemDaLuz = pygame.image.load(os.path.join(pastaImgens, 'luz.png'))
imagemDaLuz = pygame.transform.scale(imagemDaLuz, (600/5, 600/5))

################### Busca  de Imagens Mapa ###################
spriteMap = pygame.image.load(os.path.join(pastaImagens_TileMap, 'tilemepParede.png'))

###############################################################
escalaTile = 2.5
spriteTetoW = pygame.transform.scale(spriteMap.subsurface((16*2, 16, 16, 16)), (16*escalaTile, 16*escalaTile))
spriteTetoD = pygame.transform.scale(spriteMap.subsurface((16*2, 0, 16, 16)), (16*escalaTile, 16*escalaTile))
spriteTetoA = pygame.transform.scale(spriteMap.subsurface((16*3, 0, 16, 16)), (16*escalaTile, 16*escalaTile))
spriteTetoS = pygame.transform.scale(spriteMap.subsurface((16*3, 16, 16, 16)), (16*escalaTile, 16*escalaTile))
spriteTetoQ = pygame.transform.scale(spriteMap.subsurface((16*5, 0, 16, 16)), (16*escalaTile, 16*escalaTile))
spriteTetoQ = pygame.transform.scale(spriteMap.subsurface((16*5, 0, 16, 16)), (16*escalaTile, 16*escalaTile))
spriteTetoE = pygame.transform.scale(spriteMap.subsurface((16*5, 16, 16, 16)), (16*escalaTile, 16*escalaTile))
spritePiso = pygame.transform.scale(spriteMap.subsurface((16, 16*1, 16, 16)), (16*escalaTile, 16*escalaTile))
spriteParede = pygame.transform.scale(spriteMap.subsurface((0, 0, 16, 16)), (16*escalaTile, 16*escalaTile))
spriteParede2 = pygame.transform.scale(spriteMap.subsurface((16, 0, 16, 16)), (16*escalaTile, 16*escalaTile))
###############################################################


################### Buscar Imagens do Jogador #################
###########  personagem parado 
spriteParadoFrente = pygame.image.load(os.path.join(pastaImagens_Jogador, 'paradoDeFrente.png'))
spriteParadoCosta = pygame.image.load(os.path.join(pastaImagens_Jogador, 'paradoDeCosta.png'))

########## personagem em movimento 
spriteAndarFrente = pygame.image.load(os.path.join(pastaImagens_Jogador, 'correndoDeFrente.png'))
spriteAndarCosta = pygame.image.load(os.path.join(pastaImagens_Jogador, 'correndoDeCosta.png'))
spriteAndarLado = pygame.image.load(os.path.join(pastaImagens_Jogador, 'CorrendoDeLado.png'))
###############################################################



################ porta #########
spritePorta = pygame.transform.scale(spriteMap.subsurface((16*4, 0, 16, 16)), (16*4, 16*4))