import pygame 
import random

class Frutas:
    
    def __init__(self,endereco_imagem):
        self.imagem = endereco_imagem
        self.imagem = pygame.transform.scale_by(self.imagem,0.22)
        self.mascara2 = pygame.mask.from_surface(self.imagem)
        
        self.pos_frutas_y = 0
        lista_lugares= [300,400,500,600,700,800,900,100]
        self.pos_frutas_x = random.choice(lista_lugares)
        self.velocidade = random.randint(4,5)

    def andar(self):
        self.pos_frutas_y += self.velocidade
        if self.pos_frutas_y > 1200:
            self.voltar()

    def exibir(self,tela_do_jogo):
        tela_do_jogo.blit(self.imagem,(self.pos_frutas_x,self.pos_frutas_y))

    def voltar(self):
        self.pos_frutas_y = 0
        lista_lugares= [300,400,500,600,700,800,900,100]
        self.pos_frutas_x = random.choice(lista_lugares)
        self.velocidade = random.randint(4,5)
