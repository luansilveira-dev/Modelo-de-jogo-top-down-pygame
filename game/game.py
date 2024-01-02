import pygame 
import sys
from game.orgLevel import *
from game.orgLevel import *
pygame.init()


## imagens teste 

### Creindo janela 
janela = pygame.display.set_mode((LARGURA, ALTURA), pygame.FULLSCREEN)
pygame.display.set_caption("Projeto")



fps = pygame.time.Clock()
def main():
    while True: 
      janela.fill(ROXO_ESCURO)
      for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
              pygame.quit()
              sys.exit()
      
      ## definir Nivels do joogo 
      Level(janela).verLevels()
        
      #Level(janela).nivel_2()


      ## fim dos nivels 
      janela.blit(ambienteEscuro, (0,0))## Mostrar ambientação 
      
      fps.tick(FPS) / 1000.0
  
      
      pygame.display.flip()