#! python3.8
import os, sys

# obs.: tive alguns problemas de print na tela ao utilizar a versao 3.11 do python

dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

import pygame, math
from pygame.locals import *
from map import *

pygame.init()

tamanho_da_sala = [ 10, 15 ]
tamanho_dos_tiles = [ 32, 32 ]

escala = 2

tamanho_da_tela_pequena = [tamanho_da_sala[i] * tamanho_dos_tiles[i] for i in range(2)]
tamanho_da_tela_grande = [tamanho_da_sala[i] * tamanho_dos_tiles[i] * escala for i in range(2)]

tela_pequena = pygame.surface.Surface( tamanho_da_tela_pequena )
tela_grande = pygame.display.set_mode( tamanho_da_tela_grande )

chao_de_masmorra = pygame.image.load( "tiles\\chao_de_masmorra.png" )
parede_de_masmorra = pygame.image.load( "tiles\\parede_de_masmorra.png" )
tile_porta = pygame.image.load( "tiles\\porta.png" )
chave = pygame.image.load( "tiles\\chave.png" )
coracao_imagem = pygame.image.load( "tiles\\coracao.png" )


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


class Personagem():
	cor = (0, 0, 0)
	posicao = [0, 0]
	def __init__(self, cor=None, posicao=None):
		self.cor = cor or self.cor
		self.posicao = posicao or self.posicao


class Princesa(Personagem):
	def __init__(self):
		super().__init__( ( 210, 0, 210 ), [-6, 53] )

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


class Jogador(Personagem):
    def __init__(self):
        self.demora_do_tiro = 10
        super().__init__( ( 255, 240, 51 ), [1, 1] )
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


class Inimigo1(Personagem):
	def __init__(self):
		super().__init__( ( 255, 0, 0 ), [ 4, 16 ] )
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


class Inimigo2(Personagem): # persegue o jogador na sala final
    def __init__(self):

        super().__init__( ( 255, 0, 0 ), [ -2, 52 ] )
        
        #self.cor = ( 255, 0, 0 )
        #self.posicao = [ -2, 52 ]
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

class Inimigo3(Personagem): # semelhante a Inimigo1(), mas colide com portas
    def __init__(self):
        super().__init__( ( 255, 0, 0 ), [ 4, 16 ] )
        #self.cor = ( 255, 0, 0 )
        #self.posicao = [ 4, 16 ]
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

class InimigoPerseguidor(Personagem):
    def __init__(self, pos=None, vel=None):
        super().__init__( ( 255, 0, 0 ), pos )
        #self.cor = ( 255, 0, 0 )
        #self.posicao = pos or [ 0, 0 ]
        self.velocidade = vel or [ 0, 0 ]
        self.limites = [[1, 1], [2, 12]]

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
        for i in range(2):
            if self.posicao[i] < self.limites[i][0]:
                self.posicao[i] = self.limites[i][0]
            if self.posicao[i] > self.limites[i][1]:
                self.posicao[i] = self.limites[i][1]
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
inimigos.append(InimigoPerseguidor([ 1, 32 ],))


placa = Placa_de_pressao()
jogador1 = Jogador()
princesa = Princesa()

# jogador1.posicao = [4, 30]

''' # script de teste
for j in range(30):
    #espera()
    #debug()
    princesa.posicao[1] -= 1
    jogador1.posicao[1] -= 1
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
    #preenche_a_tela()
'''

def main():
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

main()
