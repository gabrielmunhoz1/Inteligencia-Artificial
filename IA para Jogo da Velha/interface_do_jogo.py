import pygame
from pygame.locals import *
from sys import exit

#iniciando as funcoes ee variaveis do pygame
pygame.init()

#altura e largura da nossa tela
altura = 500  
largura = 500

#crição da tela 
tela = pygame.display.set_mode((largura, altura))
#setar o nome do jogo
pygame.display.set_caption('Jogo da Velha')

#loop infinito para rodar o jogo
while True:
    #verifica se o jogo foi fechado
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    #linhas que separam cada "célula" do jogo da velha
    '''
    pygame.draw.line(tela, (255, 0, 255),  )
    pygame.draw.line(tela, (255, 0, 255),  )
    pygame.draw.line(tela, (255, 0, 255),  )
    '''
    #linhas verticais
    pygame.draw.line(tela, (255, 0, 255), (150, 500), (150, 80), 10)
    pygame.draw.line(tela, (255, 0, 255), (340, 500), (340, 80), 10)
    #linhas horizontais
    pygame.draw.line(tela, (255, 0, 255), (0, 200), (500, 200), 10)
    pygame.draw.line(tela, (255, 0, 255), (0, 360), (500, 360), 10)
    

    
    pygame.display.update()


    