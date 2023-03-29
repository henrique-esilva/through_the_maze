#! python3.8
import os, sys

# obs.: tive alguns problemas de print na tela ao utilizar a versao 3.11 do python

dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

import pygame, math
from pygame.locals import *

pygame.init()

tamanho_da_sala = [ 10, 15 ]
tamanho_dos_tiles = [ 32, 32 ]

tamanho_da_tela_pequena = []
tamanho_da_tela_grande = []

escala = 2

for i in range( len(tamanho_da_sala) ):
    tamanho_da_tela_pequena.append( tamanho_da_sala[i] * tamanho_dos_tiles[i] )
    tamanho_da_tela_grande.append( tamanho_da_sala[i] * tamanho_dos_tiles[i] * escala )

tela_pequena = pygame.surface.Surface( tamanho_da_tela_pequena )
tela_grande = pygame.display.set_mode( tamanho_da_tela_grande )

chao_de_masmorra = pygame.image.load( "tiles\\chao_de_masmorra.png" )
parede_de_masmorra = pygame.image.load( "tiles\\parede_de_masmorra.png" )
tile_porta = pygame.image.load( "tiles\\porta.png" )
chave = pygame.image.load( "tiles\\chave.png" )
coracao_imagem = pygame.image.load( "tiles\\coracao.png" )


tileset_chao = [
[1, 1], [1, 2], [2, 1], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [8, 3], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7], [6, 7], [5, 7], [4, 7], [4, 6], [4, 5], [3, 5], [2, 5], [1, 5], [1, 4], [2, 4], [3, 4], [4, 4], [2, 6], [2, 7], [2, 8], [1, 8], [1, 9], [2, 9], [1, 10], [1, 11], [2, 11], [3, 11], [5, 10], [6, 10], [7, 10], [4, 11], [5, 11], [6, 11], [7, 11], [5, 12], [6, 12], [7, 12], [5, 13], [6, 13], [7, 13], [2, 13], [2, 14],
[2, 15], [2, 16], [2, 17], [2, 18], [2, 19], [2, 20], [3, 20], [4, 20], [5, 20], [5, 19], [4, 18], [5, 18], [6, 18], [4, 17], [5, 17], [6, 17], [4, 16], [5, 16], [6, 16], [7, 17], [8, 17], [8, 18], [8, 19], [8, 20], [8, 21], [8, 22], [8, 23], [8, 24], [8, 25], [7, 25], [6, 23], [6, 24], [6, 25], [6, 26], [6, 27], [5, 23], [5, 24], [5, 25], [5, 26], [5, 27], [4, 23], [4, 24], [4, 25], [4, 26], [4, 27], [3, 23], [3, 24], [3, 25], [3, 26], [3, 27], [2, 23], [2, 24], [2, 25], [2, 26], [2, 27], [4, 29],
[-1, 55],[-2, 55],[-3, 55],[-4, 55],[-5, 55],[-6, 55],[-6, 53],[-7, 55],[-8, 55],[-9, 55],[-9, 54],[-9, 53],[-9, 52],[-9, 51],[-9, 50],[-9, 49],[-9, 48],[-8, 48],[-7, 48],[-6, 48],[-5, 48],[-4, 48],[-2, 48],[-3, 48],[-3, 51],[-3, 53],[-3, 55],[-9, 58],[-8, 58],[-7, 58],[-6, 58],[-5, 58],[-4, 58],[-3, 58],[-2, 58],
[10, 55],[11, 55],[12, 55],[13, 55],[14, 55],[15, 55],[16, 55],[17, 55],[18, 55],[20, 55],[21, 55],[12, 57],[12, 56],[12, 54],[12, 53],[12, 52],[12, 51],[12, 50],[12, 49],[12, 48],[14, 57],[14, 56],[14, 54],[14, 53],[14, 52],[14, 51],[14, 50],[14, 49],[14, 48],[16, 57],[16, 56],[16, 54],[16, 53],[16, 52],[16, 51],[16, 50],[16, 49],[16, 48],[18, 54],[18, 53],[18, 52],[18, 51],
[4, 30], [4, 31], [3, 32], [4, 32], [5, 32], [6, 32], [3, 33], [4, 33], [5, 33], [6, 33], [3, 34], [4, 34], [5, 34], [6, 34],    [6, 36], [6, 37], [6, 38], [6, 39], [6, 40],    [5, 39], [5, 40], [3, 40], [3, 39], [3, 38], [3, 37], [3, 36], [4, 36], [4, 39], [4, 40],    [1, 32], [1, 33], [1, 34], [1, 35], [1, 36], [1, 37], [3, 37], [1, 38], [1, 39], [1, 40],    [5, 42], [5, 43], [5, 44],
[0, 55], [1, 55], [2, 55], [3, 55], [4, 55], [5, 55], [6, 55], [7, 55], [8, 55], [5, 54], [5, 53], [5, 52], [5, 51], [5, 50], [5, 49], [5, 48], [5, 47], [5, 46], [5, 45]
]

tileset_moeda = []
for x in range(22, 28):
    for y in range(47, 58):
        tileset_moeda.append([x,y])
        tileset_chao.append([x, y])

tileset_chave = [ [6, 13], [4, 25], [1, 19], [ 4, 33], [-2, 48], [-2, 58], [4, 36], [1, 40] ]
tileset_porta = [ [2, 12], [1, 19], [4, 28], [ 6, 35], [-3, 49], [ 9, 55], [1, 35], [5, 41], [-6, 54], [12, 56], [14, 56], [16, 56] ]
coracao = [100, 100]

tiros = []
inimigos = []

def retorna_retangulo( arg ):
    return pygame.Rect( arg[0] * tamanho_dos_tiles[0], arg[1] * tamanho_dos_tiles[1], tamanho_dos_tiles[0], tamanho_dos_tiles[1] )

def espera(tempo = 80):
    pygame.time.wait(tempo)

def debug():
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

def pega_chave( personagem ):
    for i in range( len(tileset_chave) ):
        if Rect( tileset_chave[i][0] *tamanho_dos_tiles[0], tileset_chave[i][1] *tamanho_dos_tiles[1], tamanho_dos_tiles[0], tamanho_dos_tiles[1] ).colliderect( personagem.retorna_retangulo() ):

            print(i)

            tileset_chave.pop(i)
            tileset_chao.append( tileset_porta[i] )
            tileset_porta.pop(i)
            break

def comportamento_das_moedas():
    if len( tileset_moeda ) == 0:
        tileset_chave.append([ 1, 10 ])
        tileset_moeda.append([ 10, -15])
    for i in tileset_moeda:
        if retorna_retangulo( i ).colliderect( jogador1.retorna_retangulo() ):
            tileset_moeda.remove( i )

def transicao_entre_fases():
    global fase
    if not jogador1.retorna_retangulo().colliderect(tela_pequena.get_rect()): # traducao: 'jogador saiu da tela?'
        if jogador1.retorna_retangulo().centerx > tamanho_da_tela_pequena[0]: #jogador mais 'a direita
            for j in range(tamanho_da_sala[0]):
                espera()
                debug()
                jogador1.posicao[0] -= 1
                princesa.posicao[0] -= 1
                placa.posicao[0] -= 1
                coracao[0] -= 1
                for i in inimigos:
                    i.posicao[0] -= 1
                for i in tileset_chao:
                    i[0] -= 1
                for i in tileset_chave:
                    i[0] -= 1
                for i in tileset_porta:
                    i[0] -= 1
                for i in tileset_moeda:
                    i[0] -= 1
                preenche_a_tela()

        if jogador1.retorna_retangulo().centerx < 0: # jogador mais 'a esquerda
            for j in range(tamanho_da_sala[0]):
                espera()
                debug()
                jogador1.posicao[0] += 1
                princesa.posicao[0] += 1
                placa.posicao[0] += 1
                coracao[0] += 1
                for i in inimigos:
                    i.posicao[0] += 1
                for i in tileset_chao:
                    i[0] += 1
                for i in tileset_chave:
                    i[0] += 1
                for i in tileset_porta:
                    i[0] += 1
                for i in tileset_moeda:
                    i[0] += 1
                preenche_a_tela()

        if jogador1.retorna_retangulo().centery > tamanho_da_tela_pequena[1]: # jogador abaixo
            for j in range(tamanho_da_sala[1]):
                espera()
                debug()
                jogador1.posicao[1] -= 1
                princesa.posicao[1] -= 1
                placa.posicao[1] -= 1
                coracao[1] -= 1
                for i in inimigos:
                    i.posicao[1] -= 1
                for i in tileset_chao:
                    i[1] -= 1
                for i in tileset_chave:
                    i[1] -= 1
                for i in tileset_porta:
                    i[1] -= 1
                for i in tileset_moeda:
                    i[1] -= 1
                preenche_a_tela()

        if jogador1.retorna_retangulo().centery < 0: # jogador acima
            for j in range(tamanho_da_sala[1]):
                espera()
                debug()
                princesa.posicao[1] += 1
                jogador1.posicao[1] += 1
                placa.posicao[1] += 1
                coracao[1] += 1
                for i in inimigos:
                    i.posicao[1] += 1
                for i in tileset_chao:
                    i[1] += 1
                for i in tileset_chave:
                    i[1] += 1
                for i in tileset_porta:
                    i[1] += 1
                for i in tileset_moeda:
                    i[1] += 1
                preenche_a_tela()

def preenche_a_tela():
    coordenada_x = 0
    coordenada_y = 0
    for i in range( tamanho_da_sala[0] ):
        coordenada_x = tamanho_dos_tiles[0] * i
        for j in range( tamanho_da_sala[1] ):
            coordenada_y = tamanho_dos_tiles[1] * j
            tela_pequena.blit( parede_de_masmorra , Rect( coordenada_x, coordenada_y, 0, 0 ) )

    for i in tileset_chao:
        tela_pequena.blit( chao_de_masmorra , Rect( i[0] *tamanho_dos_tiles[0], i[1] *tamanho_dos_tiles[1], 0, 0) )

    pygame.draw.circle( tela_pequena, jogador1.cor, jogador1.retorna_retangulo().center, tamanho_dos_tiles[0] /2, 0 )

    for i in tileset_moeda:
        pygame.draw.circle( tela_pequena, ( 255, 200, 51 ), retorna_retangulo( i ).center, tamanho_dos_tiles[0]/4, int(tamanho_dos_tiles[0]/8) )

    for i in inimigos:
        pygame.draw.circle( tela_pequena, i.cor, i.retorna_retangulo().center, tamanho_dos_tiles[0] /2, 0 )

    for i in tileset_chave:
        tela_pequena.blit( chave , Rect( i[0] *tamanho_dos_tiles[0], i[1] *tamanho_dos_tiles[1], 0, 0) )

    pygame.draw.circle( tela_pequena, princesa.cor, princesa.retorna_retangulo().center, tamanho_dos_tiles[0] /2, 0 )

    for i in range(2):
        tela_pequena.blit( coracao_imagem, Rect( (coracao[0] +i) * tamanho_dos_tiles[0], coracao[1] * tamanho_dos_tiles[1], 0, 0 ) )

    for i in tileset_porta:
        tela_pequena.blit( tile_porta , Rect( i[0] *tamanho_dos_tiles[0], i[1] *tamanho_dos_tiles[1], 0, 0) )

    tela_grande.blit( pygame.transform.scale( tela_pequena, tamanho_da_tela_grande ), Rect( 0, 0, 0, 0 ) )

    pygame.display.flip()
    tela_grande.fill( (0, 0, 0) )


def controla_com_setas( player ):
    teclas = {K_UP: [1, -1], K_DOWN: [1, +1], K_LEFT: [0, -1], K_RIGHT: [0, +1]}
    velocidade = [[1, -1] , [1, +1] , [0, -1] , [0, +1]]
    posicao = [[0, -1], [0, +1], [-1, 0], [+1, 0]]
    a = pygame.key.get_pressed()

    for i in teclas.keys():
        if a[i]:
            player.posicao[teclas[i][0]] += teclas[i][1]
            if not player.estou_colidindo():
                pass
                player.posicao[teclas[i][0]] -= teclas[i][1]

class Placa_de_pressao():
    def __init__(self):
        self.estado = True
        self.posicao = [18, 51]
        self.portas = [ [2, 11], [4, 11], [6, 11] ]
        self.estado = True
        tileset_porta.append([19, 55])
    def retorna_retangulo(self):
        return pygame.Rect( self.posicao[0] * tamanho_dos_tiles[0], self.posicao[1] * tamanho_dos_tiles[1], tamanho_dos_tiles[0], tamanho_dos_tiles[1] )
    def coloca_portas(self):
        if self.estado:
            for i in tileset_porta:
                if i in self.portas:
                    i[0] += 100
                    i[1] += 100
            for i in self.portas:
                i[0] += 100
                i[1] += 100
        else:
            for i in tileset_porta:
                if i in self.portas:
                    i[0] -= 100
                    i[1] -= 100
            for i in self.portas:
                i[0] -= 100
                i[1] -= 100
    def comportamento(self):
        if inimigo5.posicao == [6, 12] and inimigo4.posicao == [4, 12] and inimigo3.posicao == [2, 12] and self.estado:
            self.portas = []
            for i in tileset_porta:
                if i == [9, 10]:
                    i[0] = 100
                    i[1] = 100
            tileset_chao.append([9, 10])
        if jogador1.retorna_retangulo().colliderect(self.retorna_retangulo()):
            jogador1.posicao[1] += 1
            if self.estado:
                self.estado = False
                self.coloca_portas()
            else:
                self.estado = True
                self.coloca_portas()

class Princesa():
    def __init__(self):
        self.cor = ( 210, 0, 210 )
        self.posicao = [-6, 53]
    def retorna_retangulo(self):
        return pygame.Rect( self.posicao[0] * tamanho_dos_tiles[0], self.posicao[1] * tamanho_dos_tiles[1], tamanho_dos_tiles[0], tamanho_dos_tiles[1] )
    def comportamento(self):

        if self.posicao[0] == jogador1.posicao[0] and self.posicao[1] == jogador1.posicao[1]-1:
            for i in range(8):
                espera(120)
                debug()
                self.posicao[1] -= 1
                jogador1.posicao[1] -= 1
                preenche_a_tela()
            jogador1.posicao = [3, -8]
            self.posicao = [6, -8]
            global coracao
            coracao = [4, -9]

class Jogador():
    def __init__(self):
        self.demora_do_tiro = 10
        self.cor = ( 255, 240, 51 )
        self.posicao = [1, 1]
        self.direcao = [1, 1]
    def estou_colidindo(self):
        for i in tileset_chao:
            if self.retorna_retangulo().colliderect(Rect(i[0] *tamanho_dos_tiles[0],i[1] *tamanho_dos_tiles[1], tamanho_dos_tiles[0], tamanho_dos_tiles[1])):
                return True
        return False
    def retorna_retangulo(self):
        return pygame.Rect( self.posicao[0] * tamanho_dos_tiles[0], self.posicao[1] * tamanho_dos_tiles[1], tamanho_dos_tiles[0], tamanho_dos_tiles[1] )
    def comportamento(self):
        tecla = pygame.key.get_pressed()
        controla_com_setas( self )
        pega_chave(self)

class Tiro():
    def __init__(self, pos, direcao):
        self.cor = (255, 0, 0)
        self.posicao = pos
        self.direcao = direcao
    def retorna_retangulo(self):
        return pygame.Rect( self.posicao[0] * tamanho_dos_tiles[0], self.posicao[1] * tamanho_dos_tiles[1], tamanho_dos_tiles[0], tamanho_dos_tiles[1] )
    def comportamento(self):
        for i in range( 2 ):
            self.posicao[i] += self.direcao[i]

class Inimigo1():
    def __init__(self):
        self.cor = ( 255, 0, 0 )
        self.posicao = [ 4, 16 ]
        self.velocidade = [ 0, 0 ]

        self.inicio_e_fim = [ [4, 1], [6, 1], [6, 3], [4, 3] ]
        self.velocidades = [ [1, 0], [0, 1], [-1, 0], [0, -1] ]
    def retorna_retangulo(self):
        return pygame.Rect( math.floor(self.posicao[0]) * tamanho_dos_tiles[0], math.floor(self.posicao[1]) * tamanho_dos_tiles[1], tamanho_dos_tiles[0], tamanho_dos_tiles[1] )
    def comportamento(self):
        if self.retorna_retangulo().colliderect(jogador1.retorna_retangulo()):
            sys.exit()
        for i in range(len(self.inicio_e_fim)):
            if self.posicao == self.inicio_e_fim[i]:
                self.velocidade = self.velocidades[i].copy()
                break
        self.posicao[0] += self.velocidade[0]
        self.posicao[1] += self.velocidade[1]

class Inimigo2(): # persgue o jogador na sala final
    def __init__(self):
        self.cor = ( 255, 0, 0 )
        self.posicao = [ -2, 52 ]
        self.velocidade = [ 0, 0 ]

        self.inicio_e_fim = [ [8, 10], [1, 10], [1, 3], [7, 3], [7, 13], [1, 13] ]
        self.velocidades = [ [-1, 0], [0, -1], [1, 0], [0, 1], [0, 0], [0, 0] ]
        self.estagio = 0
    def retorna_retangulo(self):
        return pygame.Rect( self.posicao[0] * tamanho_dos_tiles[0], self.posicao[1] * tamanho_dos_tiles[1], tamanho_dos_tiles[0], tamanho_dos_tiles[1] )
    def comportamento(self):
        if jogador1.posicao == [4, 10] and self.estagio == 0:
            self.estagio = 1
            for i in range(3):
                espera( 100 )
                debug()
                self.posicao[1] += 1
                preenche_a_tela()
            espera( 200 )
        if self.posicao == [7, 13] and self.estagio == 1:
            self.velocidade = [0, 0]
            self.estagio = 2
        if self.estagio == 2 and jogador1.posicao[1] == 10:
            if jogador1.posicao[0] > self.posicao[0] and self.posicao[0] < 8:
                self.posicao[0] += 1
            if jogador1.posicao[0] < self.posicao[0] and self.posicao[0] > 1:
                self.posicao[0] -= 1
        pega_chave(self)
        if self.retorna_retangulo().colliderect(jogador1.retorna_retangulo()):
            jogador1.posicao = [9, 10]
            self.cor = ( 255, 0, 0 )
            self.posicao = [ 8, 7 ]
            self.velocidade = [ 0, 0 ]

            self.inicio_e_fim = [ [8, 10], [1, 10], [1, 3], [7, 3], [7, 13], [1, 13] ]
            self.velocidades = [ [-1, 0], [0, -1], [1, 0], [0, 1], [0, 0], [0, 0] ]
            self.estagio = 0
        for i in range(len(self.inicio_e_fim)):
            if self.posicao == self.inicio_e_fim[i]:
                self.velocidade = self.velocidades[i].copy()
                break
        self.posicao[0] += self.velocidade[0]
        self.posicao[1] += self.velocidade[1]

class Inimigo3(): # semelhante a Inimigo1(), mas colide com portas
    def __init__(self):
        self.cor = ( 255, 0, 0 )
        self.posicao = [ 4, 16 ]
        self.velocidade = [ 0, 0 ]

        self.inicio_e_fim = [ [4, 1], [6, 1], [6, 3], [4, 3] ]
        self.velocidades = [ [1, 0], [0, 1], [-1, 0], [0, -1] ]
    def retorna_retangulo(self):
        return pygame.Rect( self.posicao[0] * tamanho_dos_tiles[0], self.posicao[1] * tamanho_dos_tiles[1], tamanho_dos_tiles[0], tamanho_dos_tiles[1] )
    def comportamento(self):
        if self.retorna_retangulo().colliderect(jogador1.retorna_retangulo()):
            sys.exit()
        for i in range(len(self.inicio_e_fim)):
            if self.posicao == self.inicio_e_fim[i]:
                self.velocidade = self.velocidades[i].copy()
                break
        self.posicao[0] += self.velocidade[0]
        self.posicao[1] += self.velocidade[1]

        pega_chave(self)

        for i in tileset_porta:
            if self.posicao == i:
                self.posicao[0] -= self.velocidade[0]
                self.posicao[1] -= self.velocidade[1]
                self.velocidade[0] = -self.velocidade[0]
                self.velocidade[1] = -self.velocidade[1]
                break

class InimigoPerseguidor():
    def __init__(self):
        self.cor = ( 255, 0, 0 )
        self.posicao = [ 1, 32 ]
        self.velocidade = [ 0, 0 ]
    def retorna_retangulo(self):
        return pygame.Rect( self.posicao[0] * tamanho_dos_tiles[0], self.posicao[1] * tamanho_dos_tiles[1], tamanho_dos_tiles[0], tamanho_dos_tiles[1] )
    def comportamento(self):
        
        if jogador1.posicao[1] > self.posicao[1]:
            self.posicao[1] += 1
            for i in tileset_porta:
                if i == self.posicao:
                    self.posicao[1] -= 1
        elif jogador1.posicao[1] < self.posicao[1]:
            self.posicao[1] -= 1
            for i in tileset_porta:
                if i == self.posicao:
                    self.posicao[1] += 1

        if self.posicao[1] < 2:
            self.posicao[1] = 2
        if self.posicao[1] > 10:
            self.posicao[1] = 10

        pega_chave(self)


inimigos.append(Inimigo1())
inimigos.append(Inimigo2())
inimigo3 = Inimigo3()
inimigo3.posicao = [12, 48]
inimigo3.inicio_e_fim = [[2, 3], [2, 12]]
inimigo3.velocidades = [[0, 1], [0, -1]]
inimigo4 = Inimigo3()
inimigo4.posicao = [14, 50]
inimigo4.velocidade = [0, 1]
inimigo4.inicio_e_fim = [[4, 3], [4, 12]]
inimigo4.velocidades = [[0, 1], [0, -1]]
inimigo5 = Inimigo3()
inimigo5.posicao = [16, 52]
inimigo5.velocidade = [0, 1]
inimigo5.inicio_e_fim = [[6, 3], [6, 12]]
inimigo5.velocidades = [[0, 1], [0, -1]]
inimigos.append(inimigo3)
inimigos.append(inimigo4)
inimigos.append(inimigo5)
inimigo6 = Inimigo3()
inimigo6.posicao = [6, 36]
inimigo6.velocidade = [0, 1]
inimigo6.inicio_e_fim = [[6, 2], [6, 10]]
inimigo6.velocidades =  [[0, 1], [0,-1]]
inimigos.append(inimigo6)
inimigos.append(InimigoPerseguidor())


placa = Placa_de_pressao()
jogador1 = Jogador()
princesa = Princesa()

while True:
    espera()
    debug()
    if placa.retorna_retangulo().colliderect( tela_pequena.get_rect() ):
        placa.comportamento()
    for i in inimigos:
        if i.retorna_retangulo().colliderect( tela_pequena.get_rect() ):
            i.comportamento()
    princesa.comportamento()
    jogador1.comportamento()
    comportamento_das_moedas()
    transicao_entre_fases()
    for i in tiros:
        i.comportamento()
    preenche_a_tela()
