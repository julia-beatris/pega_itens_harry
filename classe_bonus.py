import pygame
import random


class Bonus:
    def __init__(self,endereco_imagem):
        self.imagem = endereco_imagem
        self.imagem = pygame.transform.scale_by(self.imagem,0.20)
        self.mascara = pygame.mask.from_surface(self.imagem)
            
        self.pos_bonus_y = 0
        lista_lugares= [300,400,500,600,700,800,900,100]
        self.pos_bonus_x = random.choice(lista_lugares)
        self.velocidade = random.randint(5,14)

    def andar(self):
        self.pos_bonus_y += self.velocidade
        if self.pos_bonus_y > 1200:
            self.voltar()

    def exibir(self,tela_do_jogo):
        tela_do_jogo.blit(self.imagem,(self.pos_bonus_x,self.pos_bonus_y))

    def voltar(self):
        self.pos_bonus_y = 0
        lista_lugares= [300,400,500,600,700,800,900,100]
        self.pos_bonus_x = random.choice(lista_lugares)
        self.velocidade = random.randint(5,14)