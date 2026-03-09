import pygame
from pygame.locals import *
from sys import exit
from time import sleep
import tkinter as tk



class PigPong:
    def __init__(self, jogador1='JOGADOR 1', jogador2='JOGADOR 2', velocidade_ini = 50, velo_acu=5):
        
        
        pygame.init()
        root = tk.Tk()
        self.largura = root.winfo_screenwidth()  # buscar o tamanho da tela
        self.altura = root.winfo_screenheight() # buscar o tamanho da tela

        self.largura = self.largura - ((self.largura*10) //100)
        self.altura = self.altura - ((self.altura*10)//100)


        
        self.movimentar1 = self.movimentar2 = self.altura // 2
        self.nome_jogador1 = jogador1
        self.nome_jogador2 = jogador2
        self.velocidade_inicial = velocidade_ini
        self.velocidade_para_acumular = velo_acu


        self.total_pontos = 7


    def teclas(self):
        if (pygame.key.get_pressed()[K_w]) and self.movimentar1>10:
            self.movimentar1-=5
        if (pygame.key.get_pressed()[K_s]) and self.movimentar1<(self.altura - 50):
            self.movimentar1+=5
        if (pygame.key.get_pressed()[K_i]) and (self.movimentar2>10):
            self.movimentar2-=5
        if (pygame.key.get_pressed()[K_k]) and self.movimentar2<(self.altura - 50):
            self.movimentar2+=5



    def jogo(self):
        bola_x = self.largura // 2
        bola_y = self.altura // 2
        pontos_j1 = pontos_j2=0
        direita = True
        cima = True
        ponto = False
        tela = pygame.display.set_mode((self.largura,self.altura))
        pygame.display.set_caption('Pig Pong 1.2')
        self.velocidade_do_jogo = pygame.time.Clock()
        v_jogo = self.velocidade_inicial
        x = 1
        inicil_jogo = True
        # textos
        fonte = pygame.font.SysFont('arial',20,True,True)
        font_ganhador = pygame.font.SysFont('arial',50,True,True)

        texto_j1 = fonte.render(self.nome_jogador1, True, (0, 255, 0))
        texto_j2 = fonte.render(self.nome_jogador2,True,(0,0,250))

        ganhador_1 = font_ganhador.render(f'{self.nome_jogador1} VENCEU',True,(150,150,150))
        ganhador_2 = font_ganhador.render(f'{self.nome_jogador2} VENCEU',True,(150,150,150))
        texto_inicial = font_ganhador.render(f'Faça {self.total_pontos} pontos primeiro',True,(250,250,250))
        texto_pontos = fonte.render('PONTOS',True,(255,255,255))

        while True:
            self.velocidade_do_jogo.tick(v_jogo)
            tela.fill((0,0,0))
            #tecla de saida
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()


            #movimentação
            if cima:
                bola_y-=3
                if bola_y<20:
                    cima = False
            else:
                bola_y+=3
                if bola_y>self.altura-10:
                    cima = True

            if direita:
                bola_x+=3
            else:
                bola_x-=3

            #pontos
            if bola_x<=0:
                pontos_j2+=1
                ponto = True
                if pontos_j2==self.total_pontos:
                    tela.blit(ganhador_2,(70,200))
                    pontos_j1 = pontos_j2 = 0
                    ponto = False
                    x = 1
            elif bola_x>=self.largura:
                pontos_j1+=1
                ponto = True
                if pontos_j1==self.total_pontos:
                    tela.blit(ganhador_1,(70,200))
                    pontos_j1 = pontos_j2 = 0
                    ponto = False
                    x = 1

            #  iniciar lançe
            if ponto:
                bola_x = self.largura // 2
                bola_y = self.altura // 2
                v_jogo = self.velocidade_inicial
            # botois
            self.teclas()
            

            # personagens
            bola = pygame.draw.circle(tela,(250,0,0,),(bola_x,bola_y),10)
            jogador1 = pygame.draw.rect(tela,(0,250,0),(0,self.movimentar1,20,50))
            jogador2 = pygame.draw.rect(tela,(0,0,250),(self.largura-20,self.movimentar2,20,50))

            if jogador1.colliderect(bola):
                direita = True
                v_jogo+=self.velocidade_para_acumular
            if jogador2.colliderect(bola):
                direita = False
                v_jogo+=self.velocidade_para_acumular


            tela.blit(texto_j1, (30, 0))
            tela.blit(texto_j2, (self.largura - 140, 0))
            texto_ponto = fonte.render(f'{pontos_j1} | {pontos_j2}', True, (255, 250, 255))
            tela.blit(texto_ponto,((self.largura//2)+15,20))
            tela.blit(texto_pontos, ((self.largura//2), 0))

            if inicil_jogo:
                tela.blit(texto_inicial, ((self.largura//2) - 200, (self.altura//2) - 90))
                inicil_jogo = False

            pygame.display.update()
            # atualizar
            if ponto:
                sleep(2)
                ponto = False
            if x==1:
                sleep(5)
                x+=1
                bola_x = self.largura // 2
                bola_y = self.altura // 2
                v_jogo = self.velocidade_inicial
        




PigPong(jogador1='Fabio', velo_acu=20, velocidade_ini=50).jogo()
# original flp
