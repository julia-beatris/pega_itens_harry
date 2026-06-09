import pygame 

class Jogador:
    def __init__(self):
        self.imagem = pygame.image.load("src/img/mini_harry.png")
        self.imagem =  pygame.transform.scale_by(self.imagem,0.4)
        self.pos_x = 460
        self.pos_y = 550
        self.mascara = pygame.mask.from_surface(self.imagem)

    def andar (self,tecla_pressionada):
            if tecla_pressionada [pygame.K_RIGHT]:
                if self.pos_x < 1200 - self.imagem.get_width():
                #Faz a sereia ir para a direita
                    self.pos_x = self.pos_x + 5
            
            
            if tecla_pressionada [pygame.K_LEFT]:
                if self.pos_x > 0:
                #Faz a sereia ir para a esquerda
                    self.pos_x = self.pos_x - 5

    def exibir(self,capa_do_jogo):
            capa_do_jogo.blit(self.imagem,(self.pos_x,self.pos_y))
