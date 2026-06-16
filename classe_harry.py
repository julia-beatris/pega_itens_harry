import pygame

class Jogador:

    def __init__(self):
        self.lista_sprites = [pygame.image.load("src/img/harry01.png"),
                         pygame.image.load("src/img/harry02.png"),
                         pygame.image.load("src/img/harry03.png")]
        
        contador =0
        for sprite in self.lista_sprites:
            self.lista_sprites[contador] = pygame.transform.scale_by(sprite,0.6)
            contador = contador + 1
        
        self.sprite_atual = 0
        
        self.imagem = self.lista_sprites[self.sprite_atual]

        self.pos_x = 0
        self.pos_y = 586
        
        self.velocidade = 8

        self.mascara = pygame.mask.from_surface(self.imagem)
    

    def andar(self, teclas_pressionadas):
        #TROCA DE SPRITE
        if teclas_pressionadas[pygame.K_LEFT] or teclas_pressionadas[pygame.K_RIGHT]:
                self.sprite_atual = self.sprite_atual + 0.2
                if self.sprite_atual > len(self.lista_sprites)-1:
                    self.sprite_atual = 0
                    
        if teclas_pressionadas[pygame.K_LEFT]:
            if self.pos_x > 0:
                self.imagem = pygame.transform.flip(self.lista_sprites[int(self.sprite_atual)], True, False)
                self.mascara = pygame.mask.from_surface(self.imagem)
                self.pos_x = self.pos_x - self.velocidade
                
        if teclas_pressionadas[pygame.K_RIGHT]:
            if self.pos_x < 1100-self.imagem.get_width():
                self.imagem = self.lista_sprites[int(self.sprite_atual)]
                self.mascara = pygame.mask.from_surface(self.imagem)
                self.pos_x = self.pos_x + self.velocidade
                
    def mostrar(self, tela):
        tela.blit(self.imagem,(self.pos_x,self.pos_y))
        
    def voltar(self):
        self.pos_x = 0
        self.pos_y = 586