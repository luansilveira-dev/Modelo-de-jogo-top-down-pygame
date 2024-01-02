from levels.level_1 import *
from levels.level_2 import *
from levels.level_3 import *

corrente_nivel = 1


class Level():
    def __init__(self, janela):
        self.janela = janela
        

    def level_1(self):
        global corrente_nivel
        if corrente_nivel == 1: 
            level_1 = Level_1(self.janela)
            level_1.run()
            if level_1.colisao_porta():
                corrente_nivel = 2
            

    def level_2(self):
        global corrente_nivel
        if corrente_nivel == 2:
            level_2 = Level_2(self.janela)
            level_2.run()
            if level_2.colisao_porta():
                corrente_nivel = 3

    def level_3(self):
        global corrente_nivel
        if corrente_nivel == 3:
            level_3 = Level_3(self.janela)
            level_3.run()
            if level_3.colisao_porta():
                corrente_nivel = 1
    


    def verLevels(self):
        self.level_1()
        self.level_2()
        self.level_3()

