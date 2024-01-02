import pygame

class TileMap():
    def __init__(self, listaImage, listaMap, janela, dimencao):
        self.listaMap = listaMap
        self.listaImage = listaImage
        self.janela = janela
        self.dimencao = dimencao

    def desenharTile(self):
        self.y = 0 
        for linha in self.listaMap:
            self.x = 0
            for tilemap in linha:
                #if tilemap == '0':
                    #self.janela.blit(self.listaImage[0], (self.x * self.dimencao, self.y * self.dimencao))
                if tilemap == 'x':
                    self.janela.blit(self.listaImage[1], (self.x * self.dimencao, self.y * self.dimencao))
                if tilemap == 'z':
                    self.janela.blit(self.listaImage[2], (self.x * self.dimencao, self.y * self.dimencao))

                if tilemap == 'w':
                    self.janela.blit(self.listaImage[3], (self.x * self.dimencao, self.y * self.dimencao))
                if tilemap == 'd':
                    self.janela.blit(self.listaImage[4], (self.x * self.dimencao, self.y * self.dimencao))
                if tilemap == 'a':
                    self.janela.blit(self.listaImage[5], (self.x * self.dimencao, self.y * self.dimencao))
                if tilemap == 's':
                    self.janela.blit(self.listaImage[6], (self.x * self.dimencao, self.y * self.dimencao))

                if tilemap == 'q':
                    self.janela.blit(self.listaImage[7], (self.x * self.dimencao, self.y * self.dimencao))
                
                if tilemap == 'e':
                    self.janela.blit(self.listaImage[8], (self.x * self.dimencao, self.y * self.dimencao))
                
                
                self.x += 1
            self.y += 1

    def verificarColisao(self, jogadorRect):
        for y, linha in enumerate(self.listaMap):
            for x, tilemap in enumerate(linha):
                if tilemap in ['w', 'd', 'a', 's', 'q', 'e','z']:
                    tileRect = pygame.Rect(x * self.dimencao, y * self.dimencao, self.dimencao, self.dimencao)
                    if jogadorRect.colliderect(tileRect):
                        return True
        return False