import numpy as np
import pygame
import math

# Variaveis globais
angulo = 0

fov = 90
near = 0.1
far = 1000

matrix_de_projecao = [[1,0,0],
					  [0,1,0]]

w, h = 1200, 650


# Criando as vertices de um cubo
vertices = [n for n in range(8)]

# Definindo as coordenadas das vertices
vertices[0] = [[-1],[1],[1]]
vertices[1] = [[-1],[-1],[1]]
vertices[2] = [[1],[1],[1]]
vertices[3] = [[1],[-1],[1]]

vertices[4] = [[-1],[1],[-1]]
vertices[5] = [[-1],[-1],[-1]]
vertices[6] = [[1],[1],[-1]]
vertices[7] = [[1],[-1],[-1]]

velocidade = 0.01

# Inicializacao do pygame
pygame.init()

# Configurando a tela
pygame.display.set_caption("Projecao 3D")
tela = pygame.display.set_mode((w,h))

clock = pygame.time.Clock()

def desenharFaces(i,j,facesProjetadas):
	a = facesProjetadas[i]
	b = facesProjetadas[j]

	pygame.draw.line(tela, (255,255,255), (a[0],a[1]), (b[0],b[1]), 10)

# Loop principal
while True:
	fps = clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	tela.fill((0,0,0))

	# Rotacao de matriz no eixo X
	rotacaoX = [[1,0,0],
				[0,math.cos(angulo),-math.sin(angulo)],
				[0,math.sin(angulo),math.cos(angulo)]]
	
	rotacaoY = [[math.cos(angulo),0,math.sin(angulo)],
				[0,1,0],
				[-math.sin(angulo),0,math.cos(angulo)]]

	rotacaoZ = [[math.cos(angulo),-math.sin(angulo),0],
				[math.sin(angulo),math.cos(angulo),0],
				[0,0,1]]

	# Criando uma matriz com todas os conteudos dos vertices
	index = 0
	facesProjetadas = [l for l in range(len(vertices))]

	# Basicamente para projetar algo tridimensional em uma tela bidimensional...
	# Basta multiplicar a matriz de projecao pelos eixos das vertices desejadas.
	# Fazendo isso o resultado sera uma matriz 2x1.
	# O valor dessa matriz sera o X e Y das vertices...
	for vertice in vertices:
		projetado_rotacaoX = np.dot(rotacaoX, vertice)
		projetado_rotacaoXY = np.dot(rotacaoY, projetado_rotacaoX)

		projetado = np.dot(matrix_de_projecao, projetado_rotacaoXY)

		x = int(projetado[0][0] * 100) + w//2
		y = int(projetado[1][0] * 100) + h//2

		# A matriz vai receber o x e y, e cada posicao dos vertices
		facesProjetadas[index] = [x,y]

		pygame.draw.circle(tela, (255,255,255), (x,y), 1)

		# Todas as posicoes dos vertices
		index += 1

	desenharFaces(0,1,facesProjetadas)
	desenharFaces(0,2,facesProjetadas)
	desenharFaces(1,3,facesProjetadas)
	desenharFaces(1,5,facesProjetadas)
	desenharFaces(2,6,facesProjetadas)
	desenharFaces(3,7,facesProjetadas)
	desenharFaces(4,6,facesProjetadas)
	desenharFaces(6,7,facesProjetadas)
	desenharFaces(5,4,facesProjetadas)
	desenharFaces(4,0,facesProjetadas)
	desenharFaces(2,3,facesProjetadas)
	desenharFaces(5,7,facesProjetadas)

	angulo += velocidade
	pygame.display.update()

pygame.quit()
