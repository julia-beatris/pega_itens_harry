import pygame 
from classe_jogador import Jogador
from classe_frutas import Frutas
from classe_inimigo import Inimigo
from classe_bonus import Bonus
pygame.init()

clock = pygame.time.Clock()

#Criando a janela do jogo 
tela = pygame.display.set_mode((1200,700))

#Mudando o nome da janela 
pygame.display.set_caption("Beco das Frutas")

#colocando a tela de inicio 
capa = pygame.image.load("src/img/capa_inicio.jpg")
capa = pygame.transform.scale(capa,(1200,700))
#colocando o jardim (tela de fundo)
jardim = pygame.image.load("src/img/fundo_jradim.jpg")
jardim = pygame.transform.scale(jardim,(1200,700))
#tela de vitoria
capa_vitoria = pygame.image.load("src/img/capa_vitoria.jpg")
capa_vitoria = pygame.transform.scale(capa_vitoria,(1200,700))
#tela de game over
capa_perda = pygame.image.load("src/img/capa_perdeu.jpg")
capa_perda = pygame.transform.scale(capa_perda,(1200,700))

#criando o jogador 
mini_harry = Jogador()

#colocando as frutas 
lista_frutas = [Frutas(pygame.image.load("src/img/fruta_1.jpg")),
                Frutas(pygame.image.load("src/img/fruta_2.jpg")),
                Frutas(pygame.image.load("src/img/fruta_3.jpg")),
                Frutas(pygame.image.load("src/img/fruta_4.jpg")),
                Frutas(pygame.image.load("src/img/fruta_5.jpg")),
                Frutas(pygame.image.load("src/img/fruta_6.jpg"))]
    
#colocando o inimigo 
lista_inimigo = [Inimigo(pygame.image.load("src/img/cobra_inimigo.jpg")),
                 Inimigo(pygame.image.load("src/img/cobra_inimigo.jpg")),
                 Inimigo(pygame.image.load("src/img/cobra_inimigo.jpg"))]

#colocando o bonus 
lista_bonus = [Bonus(pygame.image.load("src/img/salva_vidas.jpg")),
               Bonus(pygame.image.load("src/img/salva_vidas.jpg")),
               Bonus(pygame.image.load("src/img/salva_vidas.jpg")),]



fonte_texto = pygame.font.SysFont("arial",24,True)
fonte_textop = pygame.font.SysFont("arial",24,True)

som_itens= pygame.mixer.Sound("src/som/som_itens.mp3")
som_cobra= pygame.mixer.Sound("src/som/som_cobra.mp3")

#contadores
contador_pontos = 0 
contador_mortes = 0 
status_jogo = "INICIO"

rodando = True
while rodando:

    tecla_pressionada = pygame.key.get_pressed()#retorna a tecla que eu estou pressionando
     #Pego todos os eventos que aconteceu na janela 
    lista_eventos = pygame.event.get()
    #Percorrro os eventos para encontrar aquele que eu quiser 
    for evento in lista_eventos:
        #Se um dos eventos for ter clicado no X eu encerro o programa 
        if evento.type == pygame.QUIT:
            rodando = False

    if status_jogo == "INICIO":
        tela.blit(capa,(0,0))
        if tecla_pressionada[pygame.K_RETURN] or tecla_pressionada[pygame.K_KP_ENTER]:
            status_jogo = "JOGANDO"


    if status_jogo == "JOGANDO":
        #inserindo a imagem        
        tela.blit(jardim,(0,0))
        texto_morte = fonte_texto.render(f"MORTES:{contador_mortes}",False,[0,0,0]) 
        tela.blit(texto_morte,(600,10))
        texto_pontos = fonte_texto.render(f"PONTOS:{contador_pontos}",False,[0,0,0])
        tela.blit(texto_pontos,(450,10))



        #colocando a harry
        mini_harry.andar(tecla_pressionada)
        mini_harry.exibir(tela)

        #colocando o inimigo 
        for inimigo in lista_inimigo:
            inimigo.andar()
            inimigo.exibir(tela)

        #colocando o bonus  
        for bonus in lista_bonus:
            bonus.andar()
            bonus.exibir(tela)

        #frutas dando certo 
        for frutas in lista_frutas:
            frutas.andar()
            frutas.exibir(tela)
            if frutas.mascara2.overlap(mini_harry.mascara,(mini_harry.pos_x-frutas.pos_frutas_x,mini_harry.pos_y-frutas.pos_frutas_y)):
                contador_pontos = contador_pontos + 1
                som_itens.play()
                frutas.voltar()

        #inimigo funcionando
        for inimigo in lista_inimigo:
            inimigo.andar()
            inimigo.exibir(tela)
            if  inimigo.mascara3.overlap(mini_harry.mascara,(mini_harry.pos_x-inimigo.pos_inimigo_x,mini_harry.pos_y-inimigo.pos_inimigo_y)):
                contador_mortes = contador_mortes + 1
                som_cobra.play()
                inimigo.voltar()
        if contador_mortes == 5 :
            status_jogo = "FIM"

        if status_jogo == "FIM" :
            tela.blit(capa_perda,(0,0))
            if tecla_pressionada[pygame.K_RETURN] or tecla_pressionada[pygame.K_KP_ENTER] :
                contador_mortes = 0 
                contador_pontos = 0 
                status_jogo = "JOGANDO"
                
        #bonus funcionando
        for bonus in lista_bonus:
            bonus.andar()
            bonus.exibir(tela)
            if  bonus.mascara4.overlap(mini_harry.mascara,(mini_harry.pos_x-bonus.pos_bonus_x,mini_harry.pos_y-bonus.pos_bonus_y)):
                contador_pontos = contador_pontos + 3
                som_itens.play()
                bonus.voltar()

            if tecla_pressionada[pygame.K_SPACE] :
                bonus.pos_bonus_x,bonus.pos_bonus_y = mini_harry.pos_x,mini_harry.pos_y
                poder = True
                if  bonus.mascara4.overlap(mini_harry.mascara,(mini_harry.pos_x-bonus.pos_bonus_x,mini_harry.pos_y-bonus.pos_bonus_y)):
                    contador_pontos =+ 3
                    bonus.voltar()
                    

    
    if status_jogo == "FIM":
        tela.blit(capa_perda,(0,0))
        if tecla_pressionada[pygame.K_RETURN] or tecla_pressionada[pygame.K_KP_ENTER]:
            status_jogo = "INICIO"
            contador_pontos = 0
            contador_mortes = 0 

    if contador_pontos == 20:
        status_jogo = "FIM"
        tela.blit(capa_vitoria,(0,0))
        if tecla_pressionada[pygame.K_RETURN] or tecla_pressionada[pygame.K_KP_ENTER]:
            status_jogo = "INICIO"
            contador_pontos = 0 
            contador_mortes = 0 
            
    pygame.display.update() 
    clock.tick(60)


