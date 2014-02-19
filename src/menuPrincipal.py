import pygame
from pygame.locals import *
from sys import exit
from time import sleep
from FixTk import ver
import animacao

largura, altura = 800,600

pygame.init()

screen = pygame.display.set_mode((largura,altura),0,32)
pygame.display.set_caption  ("Muttley Fight")

#Musica

pygame.mixer.init()
pygame.mixer.music.load('Audios/MusicaMenuPrincipal.wav')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)

#Audios

Cliquesom = pygame.mixer.Sound('Audios/mouse.wav')
vitoriasom = pygame.mixer.Sound('Audios/vitoria.wav')
vitoriasom.set_volume(0.2)

fundo = pygame.image.load('imagens/fundos/inicio_Jogo.png')
botaoVoltar = pygame.image.load("imagens/botoes/voltar.png").convert_alpha()

def verificaMouse(img_botao,pos_botao,pos_mouse):
    img_x, img_y = pos_botao 
    img_w, img_h = img_botao.get_size() 
    varia_x = img_x + img_w 
    varia_y = img_y + img_h 
    if pos_mouse[0] > img_x and pos_mouse[0] < varia_x and pos_mouse[1] > img_y and pos_mouse[1] < varia_y: 
        return True
    return False

def Instrucoes(): 
    
    fundo_instrucoes = pygame.image.load("imagens/fundos/instrucoes.png")   
    
    while True:
    
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
    
        xy = pygame.mouse.get_pos() #Recupera a posicao do mouse

        screen.blit(fundo_instrucoes,(0,0))
        screen.blit(botaoVoltar,(40,523))
        
        if verificaMouse(botaoVoltar,(30,505),xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                MenuInicial()
                Cliquesom.play()
         
        pygame.display.flip()

def Creditos():
    
    
    fundoCreditos = pygame.image.load("imagens/fundos/creditos.png")
    posBotaoVoltar = (41,525)
    
    while True:
    
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
    
        xy = pygame.mouse.get_pos() #Recupera a posicao do mouse

        screen.blit(fundoCreditos,(0,0))
        screen.blit(botaoVoltar,posBotaoVoltar)


        
        if verificaMouse(botaoVoltar,posBotaoVoltar,xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                MenuInicial()
                Cliquesom.play()
         
        pygame.display.update()

def Cenarios():
    
    
    botaoIniciar = pygame.image.load("imagens/botoes/iniciar.png").convert_alpha()
    fundoCenarios = pygame.image.load("imagens/fundos/cenario.png").convert_alpha()
    botaoSeguinte = pygame.image.load('imagens/botoes/setaDireita.png').convert_alpha()
    botaoAnterior = pygame.image.load('imagens/botoes/setaEsquerda.png').convert_alpha()
    
    cenario1 = pygame.image.load('imagens/fundos/imagemfundo1.jpg').convert_alpha()
    cenario2 = pygame.image.load('imagens/fundos/imagemfundo2.jpg').convert_alpha()
    cenario3 = pygame.image.load('imagens/fundos/imagemChesf.jpg').convert_alpha()
    
    posBotaoIniciar = (651,525)
    posBotaoVoltar = (39,525)
    
    cont = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        xy = pygame.mouse.get_pos()
        
        screen.blit(fundoCenarios,(0,0))
        screen.blit(botaoIniciar, posBotaoIniciar)
        screen.blit(botaoVoltar, posBotaoVoltar)
        screen.blit(botaoSeguinte,(705,280))
        screen.blit(botaoAnterior,(20,280))
            
        if cont == 0:
            screen.blit(cenario1,(112,151))
            if verificaMouse(botaoSeguinte,(705,280),xy) == True:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    cont += 1
                    Cliquesom.play()
                    sleep(0.5)
            elif verificaMouse(botaoAnterior,(20,280),xy) == True:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    cont = 2
                    Cliquesom.play()
                    sleep(0.5)
        else:
            if cont == 1:
                screen.blit(cenario2,(112,151))
                if verificaMouse(botaoSeguinte,(705,280),xy) == True:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        cont += 1
                        Cliquesom.play()
                        sleep(0.5)
                if verificaMouse(botaoAnterior,(20,280),xy) == True:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        cont -= 1
                        Cliquesom.play()
                        sleep(0.5)
            else:
                if cont == 2:
                    screen.blit(cenario3,(112,151))
                    if verificaMouse(botaoSeguinte,(705,280),xy) == True:
                        if event.type == MOUSEBUTTONDOWN and event.button == 1:
                            cont = 0
                            Cliquesom.play()
                            sleep(0.5)
                    if verificaMouse(botaoAnterior,(20,280),xy) == True:
                        if event.type == MOUSEBUTTONDOWN and event.button == 1:
                            cont -= 1
                            Cliquesom.play()
                            sleep(0.5)
        
        if verificaMouse(botaoVoltar,(30,505),xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                NovoJogo()
                Cliquesom.play()
                sleep(0.1)
        if verificaMouse(botaoIniciar, (651,525),xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                Cliquesom.play()
                if cont == 0:
                    animacao.fundo = pygame.image.load('imagens/fundos/mesa2.jpg').convert_alpha()
                elif cont == 1:
                    animacao.fundo = pygame.image.load('imagens/fundos/mesa1.jpg').convert_alpha()
                elif cont == 2:
                    animacao.fundo = pygame.image.load('imagens/fundos/fundoChesf.jpg').convert_alpha()

                pygame.mixer.music.stop()
                animacao.jogo()
        pygame.display.flip()

def NovoJogo():
    
    botaoAvancar = pygame.image.load("imagens/Botoes/avancar.png").convert_alpha()
    
    jogador1 = pygame.image.load("imagens/fundos/jogador1.png").convert_alpha()
    jogador2 = pygame.image.load("imagens/fundos/jogador2.png").convert_alpha()
    
    janelaVermelha = pygame.image.load('imagens/molduraVermelha.png').convert_alpha()
    janelaBranca = pygame.image.load('imagens/molduraAmarela.png').convert_alpha()
    
    matheus = pygame.image.load('imagens/imagensPersonagens/matheus.jpg')
    igor = pygame.image.load('imagens/imagensPersonagens/igor.png')
    muttley = pygame.image.load('imagens/imagensPersonagens/muttley.png')
    lucas = pygame.image.load('imagens/imagensPersonagens/lucas.png')
    tulio = pygame.image.load('imagens/imagensPersonagens/tulio.png')
    alan = pygame.image.load('imagens/imagensPersonagens/alan.png')
    francois = pygame.image.load('imagens/imagensPersonagens/matheus.jpg')
    pastor = pygame.image.load('imagens/imagensPersonagens/pastor.jpg')
    
    cont = 0
    
    coluna = [130,280,430,580]
    linha = [200,350]
    
    coordenadas = []
    selecionado = False
             
    while True:
    
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        
        xy = pygame.mouse.get_pos() #Recupera a posicao do mouse
        
        screen.blit(fundo,(0,0))
    
        janelas = {}
        
        
        def imagensPersonagens():
            screen.blit(matheus,(143,217))
            screen.blit(lucas,(143,367))
            screen.blit(muttley,(293,217))
            screen.blit(pastor,(293,367))
            screen.blit(francois,(443,217))
            screen.blit(alan,(443,367))
            screen.blit(igor,(593,217))
            screen.blit(tulio,(593,367))
        
        def quadroVermelho():
            k = 0
            for i in coluna:
                for j in linha:
                    k = k+1
                    screen.blit(janelaVermelha,(i,j))
                    coordenadas.append((i,j))
                    janelas[k] = (i,j)
                    
        
        if cont == 0:
            screen.blit(jogador1,(0,0))
            screen.blit(botaoVoltar,(30,505))
            quadroVermelho()
            imagensPersonagens()
    
            if verificaMouse(janelaVermelha, janelas[1], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    Cliquesom.play()
                    animacao.player1 = 'Matheus'
                    cont += 1
                    sleep(0.1)
                    
            if verificaMouse(janelaVermelha, janelas[2], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    Cliquesom.play()
                    animacao.player1 = 'Lucas'
                    cont += 1
                    sleep(0.1)
                    
            if verificaMouse(janelaVermelha, janelas[3], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    Cliquesom.play()
                    animacao.player1 = 'Muttley'
                    cont += 1
                    sleep(0.1)
                    
            if verificaMouse(janelaVermelha, janelas[4], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    Cliquesom.play()
                    animacao.player1 = 'Vitor'
                    cont += 1
                    sleep(0.1)
                    
            if verificaMouse(janelaVermelha, janelas[5], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    Cliquesom.play()
                    animacao.player1 = 'Francois'
                    cont += 1
                    sleep(0.1)
                    
            if verificaMouse(janelaVermelha, janelas[6], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    Cliquesom.play()
                    animacao.player1 = 'Alan'
                    cont += 1
                    sleep(0.1)
                    
            if verificaMouse(janelaVermelha, janelas[7], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    Cliquesom.play()
                    animacao.player1 = 'Igor'
                    cont += 1
                    sleep(0.1)
                    
            if verificaMouse(janelaVermelha, janelas[8], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    Cliquesom.play()
                    animacao.player1 = 'Tulio'
                    cont += 1
                    sleep(0.1)
        
            if verificaMouse(botaoVoltar,(30,505),xy) == True:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    Cliquesom.play()
                    MenuInicial()
       
        elif cont == 1:
            
            screen.blit(jogador2,(0,0))
            screen.blit(botaoVoltar,(30,505))
            screen.blit(botaoAvancar,(570,505))
            quadroVermelho()
            imagensPersonagens()
            
            if verificaMouse(janelaVermelha, janelas[1], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    Cliquesom.play()
                    animacao.player2 = 'Matheus'
                    Cenarios()
                    
            if verificaMouse(janelaVermelha, janelas[2], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    Cliquesom.play()
                    animacao.player2 = 'Lucas'
                    Cenarios()
                    
            if verificaMouse(janelaVermelha, janelas[3], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    Cliquesom.play()
                    animacao.player2 = 'Muttley'
                    Cenarios()
                    
            if verificaMouse(janelaVermelha, janelas[4], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    Cliquesom.play()
                    animacao.player2 = 'Vitor'
                    Cenarios()
                    
            if verificaMouse(janelaVermelha, janelas[5], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    Cliquesom.play()
                    animacao.player2 = 'Francois'
                    Cenarios()

            if verificaMouse(janelaVermelha, janelas[6], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    Cliquesom.play()
                    animacao.player2 = 'Alan'
                    Cenarios()
                    
            if verificaMouse(janelaVermelha, janelas[7], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    Cliquesom.play()
                    animacao.player2 = 'Igor'
                    Cenarios()
                
            if verificaMouse(janelaVermelha, janelas[8], xy):
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    Cliquesom.play()
                    animacao.player2 = 'Tulio'
                    Cenarios()
                    
            if verificaMouse(botaoVoltar,(30,505),xy) == True:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    Cliquesom.play()
                    cont -= 1
                    sleep(0.1)
                    
        pygame.display.flip()

def MenuInicial():
    
    botaoNovoJogo = pygame.image.load("imagens/Botoes/novojogo.png").convert_alpha()
    botaoInstrucoes = pygame.image.load("imagens/Botoes/instrucoes.png").convert_alpha()
    botaoCreditos = pygame.image.load("imagens/Botoes/creditos.png").convert_alpha()
    botaoSair = pygame.image.load("imagens/Botoes/sairNovo.png").convert_alpha()
    
    fundo = pygame.image.load("imagens/fundos/inicio_Jogo.png").convert()
    
    posBotaoNovoJogo = (552,221)
    posBotaoInstrucoes = (550,300)
    posBotaoCreditos = (565,371)
    posBotaoSair = (602,443)
    
    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
                
        xy = pygame.mouse.get_pos() #retorna a posicao do mouse
        
        screen.blit(fundo,(0,0))
        screen.blit(botaoNovoJogo, posBotaoNovoJogo)
        screen.blit(botaoInstrucoes, posBotaoInstrucoes)
        screen.blit(botaoCreditos, posBotaoCreditos)
        screen.blit(botaoSair, posBotaoSair)
        
        if verificaMouse(botaoNovoJogo,posBotaoNovoJogo,xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                Cliquesom.play()
                NovoJogo()
                
        elif verificaMouse(botaoInstrucoes,posBotaoInstrucoes,xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                Cliquesom.play()
                Instrucoes()
                
        elif verificaMouse(botaoCreditos,posBotaoCreditos,xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                Cliquesom.play()
                Creditos()
                
        elif verificaMouse(botaoSair,posBotaoSair,xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                Cliquesom.play()
                exit()
                  
        pygame.display.flip()
        
def telaGanhou(player):
    
    vitoria1 = pygame.image.load('imagens/vitoria1.jpg').convert()
    vitoria2 = pygame.image.load('imagens/vitoria2.jpg').convert()
        
    botaoNovoJogo = pygame.image.load("imagens/Botoes/novojogo.png").convert_alpha()
    botaoSair = pygame.image.load("imagens/Botoes/sairNovo.png").convert_alpha()
    
    posBotaoNovoJogo = (100,450)
    posBotaoSair = (450,450)
    
    tocando = True
    
    while True:
        
        xy = pygame.mouse.get_pos() #retorna a posicao do mouse
        
        if player == 'player1':
            
            screen.blit(vitoria1,(0,0))
            verificaFoto(player)
            if tocando:
                vitoriasom.play()
                tocando = False
            
            
        if player == 'player2':
            
            screen.blit(vitoria2,(0,0))
            verificaFoto(player)
            if tocando: 
                vitoriasom.play()
                tocando = False
        
        screen.blit(botaoNovoJogo,posBotaoNovoJogo)
        screen.blit(botaoSair,posBotaoSair)   
        
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        
        if verificaMouse(botaoNovoJogo,posBotaoNovoJogo,xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                Cliquesom.play()
                NovoJogo()
                
        elif verificaMouse(botaoSair,posBotaoSair,xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                Cliquesom.play()
                exit()
                
        pygame.display.flip()

def verificaFoto(player):
    
    matheus = pygame.image.load('imagens/imagensPersonagens/matheus.jpg')
    igor = pygame.image.load('imagens/imagensPersonagens/igor.png')
    muttley = pygame.image.load('imagens/imagensPersonagens/muttley.png')
    lucas = pygame.image.load('imagens/imagensPersonagens/lucas.png')
    tulio = pygame.image.load('imagens/imagensPersonagens/tulio.png')
    alan = pygame.image.load('imagens/imagensPersonagens/alan.png')
    francois = pygame.image.load('imagens/imagensPersonagens/matheus.jpg')
    pastor = pygame.image.load('imagens/imagensPersonagens/pastor.jpg')
    
    if player == 'player1':
        if player == 'Matheus':
            screen.blit(matheus,(350,300))
        elif animacao.player1 == 'Vitor':
            screen.blit(pastor,(350,300))
    elif player == 'player2':
        if player == 'Matheus':
            screen.blit(matheus,(350,300))
        elif animacao.player1 == 'Vitor':
            screen.blit(pastor,(350,300))