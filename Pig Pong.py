import pygame
from pygame.locals import *
from sys import exit
from time import sleep



# controle
# jagador 1 => w s
# jagador 2 => i K

pygame.init()

largura = 640
altura = 480
velocidade_do_jogo = 50
movimentar1 = movimentar2 = 240
bola_x = 320
bola_y = 240
pontos_j1= pontos_j2=0
direita = True
cima = True
ponto = False
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('JOGO 00001')
velocidade_do_jogo = pygame.time.Clock()
v_jogo=50
x = 1
inicil_jogo = True
# textos
fonte = pygame.font.SysFont('arial',20,True,True)
font_ganhador = pygame.font.SysFont('arial',50,True,True)
texto_j1 = fonte.render('JOGADOR 1', True, (0, 255, 0))
texto_j2 = fonte.render('JOGADOR 2',True,(0,0,250))
ganhador_1 = font_ganhador.render('JOGADOR 1 VENCEU',True,(150,150,150))
ganhador_2 = font_ganhador.render('JOGADOR 2 VENCEU',True,(150,150,150))
texto_inicial = font_ganhador.render('Faça 7 pontos primeiro',True,(250,250,250))
texto_pontos = fonte.render('PONTOS',True,(255,255,255))
while True:
    velocidade_do_jogo.tick(v_jogo)
    tela.fill((0,0,0))
    #tecla de saida
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()


    #movimentação
    if cima:
        bola_y-=3
        if bola_y<10:
            cima = False
    else:
        bola_y+=3
        if bola_y>470:
            cima = True

    if direita:
        bola_x+=3
    else:
        bola_x-=3

    #pontos
    if bola_x<=0:
        pontos_j2+=1
        ponto = True
        if pontos_j2==7:
            tela.blit(ganhador_2,(70,200))
            pontos_j1 = pontos_j2 = 0
            ponto = False
            x = 1
    if bola_x>=640:
        pontos_j1+=1
        ponto = True
        if pontos_j1==7:
            tela.blit(ganhador_1,(70,200))
            pontos_j1 = pontos_j2 = 0
            ponto = False
            x = 1

    #  iniciar lançe
    if ponto:
        bola_x = 320
        bola_y = 240
        v_jogo = 50
    # botois
    if pygame.key.get_pressed()[K_w] and movimentar1>0:
        movimentar1-=5
    if pygame.key.get_pressed()[K_s] and movimentar1<430:
        movimentar1+=5
    if pygame.key.get_pressed()[K_i] and movimentar2>0:
        movimentar2-=5
    if pygame.key.get_pressed()[K_k] and movimentar2<430:
        movimentar2+=5

    # personagens
    bola = pygame.draw.circle(tela,(250,0,0,),(bola_x,bola_y),10)
    jogador1 = pygame.draw.rect(tela,(0,250,0),(0,movimentar1,20,50))
    jogador2 = pygame.draw.rect(tela,(0,0,250),(620,movimentar2,20,50))

    if jogador1.colliderect(bola):
        direita = True
        v_jogo+=5
    if jogador2.colliderect(bola):
        direita = False
        v_jogo+=5


    tela.blit(texto_j1, (10, 0))
    tela.blit(texto_j2, (490, 0))
    texto_ponto = fonte.render(f'{pontos_j1} | {pontos_j2}', True, (255, 250, 255))
    tela.blit(texto_ponto,(270,20))
    tela.blit(texto_pontos, (245, 0))

    if inicil_jogo:
        tela.blit(texto_inicial, (30, 200))
        inicil_jogo = False

    pygame.display.update()
    # atualizar
    if ponto:
        sleep(3)
        ponto = False
    if x==1:
        sleep(5)
        x+=1
        bola_x = 320
        bola_y = 240
        v_jogo = 50
    # original flp




