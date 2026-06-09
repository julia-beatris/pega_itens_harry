import pygame
import random


class Inimigo:
    def __init__(self,endereco_imagem):
        self.imagem = endereco_imagem
        self.imagem = pygame.transform.scale_by(self.imagem,0.22)
        self.mascara = pygame.mask.from_surface(self.imagem)
            
        self.pos_inimigo_y = 0
        lista_lugares= [300,400,500,600,700,800,900,100]
        self.pos_inimigo_x = random.choice(lista_lugares)
        self.velocidade = random.randint(5,14)

    def andar(self):
        self.pos_inimigo_x += self.velocidade
        if self.pos_inimigo_x > 1200:
            self.voltar()

    def exibir(self,capa_do_jogo):
        capa_do_jogo.blit(self.imagem,(self.pos_inimigo_x,self.pos_inimigo_y))
