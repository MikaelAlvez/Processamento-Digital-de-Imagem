import cv2
import sys
import numpy as np

imagem = cv2.imread("implementacoes\images\lena.pgm")
cv2.imwrite("core\Imagens\lena_cor.jpg", imagem)
altura, largura = imagem.shape[:2]
cv2.imshow("Original", imagem)

cv2.waitKey(0)

#Translacao (deslocamento)
deslocamento = np.float32([[1, 0, 25], [0, 1, 50]])
deslocado = cv2.warpAffine(imagem, deslocamento, (largura, altura))
cv2.imshow("Baixo e direita", deslocado)

cv2.waitKey(0)

deslocamento = np.float32([[1, 0, -50], [0, 1, -90]])
deslocado = cv2.warpAffine(imagem, deslocamento, (largura, altura))
cv2.imshow("Cima e esquerda", deslocado)

cv2.waitKey(0)

#Rotação
altura, largura = imagem.shape[:2]

ponto = (0, 0)

angulos = [0, 15, 30, 45, 60, 75, 285, 300, 315, 330, 345, 360]

for angulo in angulos:
    rotacao = cv2.getRotationMatrix2D(ponto, angulo, 1.0)
    rotacionado = cv2.warpAffine(imagem, rotacao, (largura, altura))
    cv2.imshow(f"Rotacionado {angulo} graus", rotacionado)
    cv2.waitKey(0)

cv2.destroyAllWindows()

#Escala
escala = cv2.resize(imagem, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
cv2.imshow("Escala ampliada", escala)
cv2.waitKey(0)

escala = cv2.resize(imagem, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
cv2.imshow("Escala reduzida", escala)
cv2.waitKey(0)

#Reflexão
reflexao_horizontal = cv2.flip(imagem, 1)
reflexao_vertical = cv2.flip(imagem, 0)
cv2.imshow("Reflexao Horizontal", reflexao_horizontal)
cv2.imshow("Reflexao Vertical", reflexao_vertical)
cv2.waitKey(0)

#Cisalhamento
cisalhamento = np.float32([[1, 0.5, 0], [0.5, 1, 0]])
cisalhado = cv2.warpAffine(imagem, cisalhamento, (largura, altura))
cv2.imshow("Cisalhamento", cisalhado)
cv2.waitKey(0)

#Incluir menu de escolha de operações, e cada uma seja feita em ordem, alterando a imagem de acordo com a ultima alteração realizada