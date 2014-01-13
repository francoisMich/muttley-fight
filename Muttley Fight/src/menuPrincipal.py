import pygame
from pygame.locals import *
from sys import exit

pygame.init()


screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption  ("mopa")


botaoNovoJogo = pygame.image.load("imagens/novojogo.png").convert()
botaoOpcoes = pygame.image.load("imagens/opcoes.png").convert()
botaoCreditos = pygame.image.load("imagens/creditos.png").convert()
botaoSair = pygame.image.load("imagens/sair.png").convert()
logo = pygame.image.load("imagens/logo.png").convert()

def verificaMouse(img_botao,pos_botao,pos_mouse):
    img_x, img_y = pos_botao 
    img_w, img_h = img_botao.get_size() 
    varia_x = img_x + img_w 
    varia_y = img_y + img_h 
    if pos_mouse[0] > img_x and pos_mouse[0] < varia_x and pos_mouse[1] > img_y and pos_mouse[1] < varia_y: 
        return True
    return False


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
            
    xy = pygame.mouse.get_pos() #retorna a posicao do mouse
    
    screen.blit(logo,(10,10))
    screen.blit(botaoNovoJogo, (550,200))
    screen.blit(botaoOpcoes, (550,300))
    screen.blit(botaoCreditos, (550,400))
    screen.blit(botaoSair, (550,500))
    
    
    if verificaMouse(botaoNovoJogo,(550,200),xy) == True:
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            print "pegou"
    elif verificaMouse(botaoOpcoes,(550,300),xy) == True:
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            Opcoes()
    elif verificaMouse(botaoCreditos,(550,400),xy) == True:
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            print "pegouCreditos"
    elif verificaMouse(botaoSair,(550,500),xy) == True:
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            exit()  
    pygame.display.update()
        


def Opcoes():
    pass
    
