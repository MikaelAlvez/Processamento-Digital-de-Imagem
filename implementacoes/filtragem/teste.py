import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread(cv.samples.findFile(
    "/home/caiovinicius/repos/pdi/Processamento-Digital-de-Imagem/implementacoes/images/lena.pgm"), cv.IMREAD_UNCHANGED)

matriz = np.array([[12, 51, 34, 121], [78, 254, 10, 97], [
                  45, 113, 110, 16], [90, 200, 206, 34]])
matriz2 = np.array([[0, 60, 0, 60], [45, 110, 45, 110],
                   [0, 60, 0, 60], [45, 110, 45, 110]])
mul = matriz2 * matriz
altura, largura = mul.shape
maior_valor = max(max(linha) for linha in mul)
menor_valor = min(min(linha) for linha in mul)
normalizado = np.zeros_like(mul).astype('uint8')
for x in range(altura):
    for y in range(largura):
        a = 255 / (maior_valor - menor_valor)
        b = -a * menor_valor
        normalizado[x, y] = round(a * mul[x, y] + b)
altura, largura = matriz.shape
resultado = np.zeros_like(normalizado)
for x in range(altura):
    for y in range(largura):
        if (normalizado[x, y] < matriz[x, y]):
            resultado[x, y] = 0
        else:
            resultado[x, y] = 255
print(resultado)
