import numpy as np
import cv2 as cv
import math
import statistics


def somboonkaew(img):
    matriz_final = np.array(img)
    h, w = img.shape
    for x in range(1, h-2):
        for y in range(1, w-2):
            media = []
            variancia = []
            # 12 mascaras
            mascara1 = [img[x-2, y-2], img[x-1, y-1], img[x, y],
                        img[x+1, y+1], img[x+2, y+2], img[x-1, y+1], img[x+1, y-1]]
            media.append(statistics.mean(mascara1))
            variancia.append(statistics.variance(mascara1))
            mascara2 = [img[x-2, y+2], img[x-1, y+1], img[x, y],
                        img[x+1, y-1], img[x+2, y-2], img[x-1, y-1], img[x+1, y+1]]
            media.append(statistics.mean(mascara2))
            variancia.append(statistics.variance(mascara2))
            mascara3 = [img[x, y-2], img[x, y-1], img[x, y],
                        img[x, y+1], img[x, y+2], img[x+1, y], img[x-1, y]]
            media.append(statistics.mean(mascara3))
            variancia.append(statistics.variance(mascara3))
            mascara4 = [img[x-2, y], img[x-1, y], img[x, y],
                        img[x+1, y], img[x+2, y], img[x, y-1], img[x, y+1]]
            media.append(statistics.mean(mascara4))
            variancia.append(statistics.variance(mascara4))
            mascara5 = [img[x-1, y-1], img[x-1, y], img[x-1, y+1],
                        img[x, y], img[x+1, y-1], img[x+1, y], img[x+1, y+1]]
            media.append(statistics.mean(mascara5))
            variancia.append(statistics.variance(mascara5))
            mascara6 = [img[x-1, y-1], img[x, y-1], img[x+1, y-1],
                        img[x, y], img[x-1, y+1], img[x, y+1], img[x+1, y+1]]
            media.append(statistics.mean(mascara6))
            variancia.append(statistics.variance(mascara6))
            mascara7 = [img[x-1, y-1], img[x-1, y], img[x, y-1],
                        img[x, y], img[x, y+1], img[x+1, y], img[x+1, y+1]]
            media.append(statistics.mean(mascara7))
            variancia.append(statistics.variance(mascara7))
            mascara8 = [img[x-1, y+1], img[x-1, y], img[x, y-1],
                        img[x, y], img[x, y+1], img[x+1, y-1], img[x+1, y]]
            media.append(statistics.mean(mascara8))
            variancia.append(statistics.variance(mascara8))
            mascara9 = [img[x-1, y], img[x, y-1], img[x, y],
                        img[x, y+1], img[x+1, y-1], img[x+1, y], img[x+1, y+1]]
            media.append(statistics.mean(mascara9))
            variancia.append(statistics.variance(mascara9))
            mascara10 = [img[x-1, y-1], img[x-1, y], img[x, y-1],
                         img[x, y], img[x, y+1], img[x+1, y-1], img[x+1, y]]
            media.append(statistics.mean(mascara10))
            variancia.append(statistics.variance(mascara10))
            mascara11 = [img[x-1, y-1], img[x-1, y], img[x-1, y+1],
                         img[x, y-1], img[x, y], img[x, y+1], img[x+1, y]]
            media.append(statistics.mean(mascara11))
            variancia.append(statistics.variance(mascara11))
            mascara12 = [img[x-1, y], img[x-1, y+1], img[x, y-1],
                         img[x, y], img[x, y+1], img[x+1, y], img[x+1, y+1]]
            media.append(statistics.mean(mascara12))
            variancia.append(statistics.variance(mascara12))
            menor = min(variancia)
            for i in range(len(variancia)):
                if (variancia[i] == menor):
                    matriz_final[x, y] = media[i]
    cv.imshow("Somboonkaew", matriz_final)
    cv.waitKey()


def nagaoEMatsuyama(img):
    matriz_final = np.array(img)
    h, w = img.shape
    for x in range(1, h-2):
        for y in range(1, w - 2):
            media = []
            variancia = []
            # sao 9 mascaras
            mascara1 = [img[x-1, y-1], img[x-1, y], img[x-1, y+1], img[x, y-1],
                        img[x, y], img[x, y+1], img[x+1, y-1], img[x+1, y], img[x+1, y+1]]
            media.append(statistics.mean(mascara1))
            variancia.append(statistics.variance(mascara1))
            mascara2 = [img[x-2, y-1], img[x-2, y], img[x-2, y+1],
                        img[x-1, y-1], img[x-1, y], img[x-1, y + 1], img[x, y]]
            media.append(statistics.mean(mascara2))
            variancia.append(statistics.variance(mascara2))
            mascara3 = [img[x, y], img[x-1, y+1], img[x-1, y+2],
                        img[x, y+1], img[x, y+2], img[x+1, y+1], img[x+1, y+2]]
            media.append(statistics.mean(mascara3))
            variancia.append(statistics.variance(mascara3))
            mascara4 = [img[x, y], img[x + 1, y-1], img[x+1, y],
                        img[x+1, y+1], img[x+2, y-1], img[x+2, y], img[x+2, y+1]]
            media.append(statistics.mean(mascara4))
            variancia.append(statistics.variance(mascara4))
            mascara5 = [img[x-1, y-2], img[x-1, y-1], img[x, y-2],
                        img[x, y-1], img[x, y], img[x+1, y-2], img[x+1, y-1]]
            media.append(statistics.mean(mascara5))
            variancia.append(statistics.variance(mascara5))
            mascara6 = [img[x-2, y-2], img[x-2, y-1], img[x-1, y-2],
                        img[x-1, y-1], img[x-1, y], img[x, y-1], img[x, y]]
            media.append(statistics.mean(mascara6))
            variancia.append(statistics.variance(mascara6))
            mascara7 = [img[x-2, y+2], img[x-2, y+1], img[x-1, y+2],
                        img[x-1, y+1], img[x-1, y], img[x, y], img[x, y+1]]
            media.append(statistics.mean(mascara7))
            variancia.append(statistics.variance(mascara7))
            mascara8 = [img[x+2, y+2], img[x+2, y+1], img[x+1, y+2],
                        img[x+1, y+1], img[x+1, y], img[x, y+1], img[x, y]]
            media.append(statistics.mean(mascara8))
            variancia.append(statistics.variance(mascara8))
            mascara9 = [img[x, y], img[x, y-1], img[x+1, y-2],
                        img[x+1, y-1], img[x+1, y], img[x+2, y-2], img[x+2, y-1]]
            media.append(statistics.mean(mascara9))
            variancia.append(statistics.variance(mascara9))
            menor = min(variancia)
            for i in range(len(variancia)):
                if (variancia[i] == menor):
                    matriz_final[x, y] = media[i]
    cv.imshow("Nagao e Matsuyama", matriz_final)
    cv.imshow("Original", img)
    cv.waitKey()


def tomitaEtsuji(img):
    # são 5 máscaras
    matriz_final = np.array(img)
    h, w = img.shape
    for x in range(1, h - 2):
        for y in range(1, w - 2):
            media = []
            variancia = []
            # subregião 1
            mascara = [img[x-2, y-2], img[x-2, y-1], img[x-2, y], img[x-1, y-2],
                       img[x-1, y-1], img[x-1, y], img[x, y-2], img[x, y-1], img[x, y]]
            media.append(statistics.mean(mascara))
            variancia.append(statistics.variance(mascara))
            # mascara 2
            mascara2 = [img[x-2, y], img[x-2, y+1], img[x-2, y+2], img[x-1, y],
                        img[x-1, y+1], img[x-1, y+2], img[x, y], img[x, y+1], img[x, y+2]]
            media.append(statistics.mean(mascara2))
            variancia.append(statistics.variance(mascara2))
            # mascara 3
            mascara3 = [img[x, y-2], img[x, y-1], img[x, y], img[x + 1, y-2],
                        img[x+1, y-1], img[x+1, y], img[x+2, y-2], img[x+2, y-1], img[x+2, y]]
            media.append(statistics.mean(mascara3))
            variancia.append(statistics.variance(mascara3))
            # mascara 4
            mascara4 = [img[x, y], img[x, y + 1], img[x, y + 2], img[x+1, y], img[x + 1,
                                                                                  y + 1], img[x + 1, y + 2], img[x + 2, y], img[x + 2, y + 1], img[x + 2, y+2]]
            media.append(statistics.mean(mascara4))
            variancia.append(statistics.variance(mascara4))
            # mascara 5
            mascara5 = [img[x-1, y-1], img[x-1, y], img[x-1, y+1], img[x, y - 1],
                        img[x, y], img[x, y+1], img[x+1, y-1], img[x+1, y], img[x+1, y+1]]
            media.append(statistics.mean(mascara5))
            variancia.append(statistics.variance(mascara5))
            # pegando a mascara com menor variancia padrão
            menor = min(variancia)
            if (menor == variancia[0]):
                # mascara 1
                matriz_final[x, y] = media[0]
            elif (menor == variancia[1]):
                # mascara 2
                matriz_final[x, y] = media[1]
            elif (menor == variancia[2]):
                # mascara 3
                matriz_final[x, y] = media[2]
            elif (menor == variancia[3]):
                # mascara 4
                matriz_final[x, y] = media[3]
            elif (menor == variancia[4]):
                # mascara 5
                matriz_final[x, y] = media[4]
    cv.imshow("Tomita e Tsuji", matriz_final)
    cv.imshow("original", img)
    cv.waitKey()


def kuwahara(img):
    # 5x5
    matriz_final = np.array(img)
    h, w = img.shape
    for x in range(1, h - 2):
        for y in range(1, w - 2):
            # tem as subregiões
            media = []
            variancia = []
            # subregião 1
            subregiao = [img[x-2, y-2], img[x-2, y-1], img[x-2, y], img[x-1, y-2],
                         img[x-1, y-1], img[x-1, y], img[x, y-2], img[x, y-1], img[x, y]]
            media.append(statistics.mean(subregiao))
            variancia.append(statistics.variance(subregiao))
            # subregiao 2
            subregiao2 = [img[x-2, y], img[x-2, y+1], img[x-2, y+2], img[x-1, y],
                          img[x-1, y+1], img[x-1, y+2], img[x, y], img[x, y+1], img[x, y+2]]
            media.append(statistics.mean(subregiao2))
            variancia.append(statistics.variance(subregiao2))
            # subregiao 3
            subregiao3 = [img[x, y-2], img[x, y-1], img[x, y], img[x + 1, y-2],
                          img[x+1, y-1], img[x+1, y], img[x+2, y-2], img[x+2, y-1], img[x+2, y]]
            media.append(statistics.mean(subregiao3))
            variancia.append(statistics.variance(subregiao3))
            # subregiao 4
            subregiao4 = [img[x, y], img[x, y + 1], img[x, y + 2], img[x+1, y], img[x + 1,
                                                                                    y + 1], img[x + 1, y + 2], img[x + 2, y], img[x + 2, y + 1], img[x + 2, y+2]]
            media.append(statistics.mean(subregiao4))
            variancia.append(statistics.variance(subregiao4))
            # pegando a subregiao com menor variancia padrão
            menor = min(variancia)
            if (menor == variancia[0]):
                # subregiao 1
                matriz_final[x, y] = media[0]
            elif (menor == variancia[1]):
                # subregiao 2
                matriz_final[x, y] = media[1]
            elif (menor == variancia[2]):
                # subregiao 3
                matriz_final[x, y] = media[2]
            elif (menor == variancia[3]):
                # subregiao 4
                matriz_final[x, y] = media[3]
    cv.imshow("Kuwahara", matriz_final)
    cv.imshow("original", img)
    cv.waitKey()


def minimo(img):
    # 3x3
    matriz_final = np.zeros_like(img)
    h, w = img.shape
    for x in range(1, h-2):
        for y in range(1, w-2):
            elementos = [img[x - 1, y - 1], img[x - 1, y], img[x-1, y + 1], img[x, y-1],
                         img[x, y], img[x, y+1], img[x+1, y-1], img[x+1, y], img[x+1, y+1]]
            minimo = min(elementos)
            matriz_final[x, y] = minimo
    cv.imshow("Minimo 3x3", matriz_final)
    cv.imshow("Original", img)
    cv.waitKey()

    matriz_final = np.zeros_like(img)
    for x in range(1, h-2):
        for y in range(1, w-2):
            elementos = [img[x-2, y-2], img[x-2, y-1], img[x-2, y], img[x-2, y+1], img[x-2, y+2], img[x-1, y-2], img[x-1, y-1], img[x-1, y], img[x-1, y+1], img[x-1, y+2], img[x, y-2], img[x, y-1],
                         img[x, y], img[x, y+1], img[x, y+2], img[x+1, y-2], img[x+1, y-1], img[x+1, y], img[x+1, y+1], img[x+1, y+2], img[x+2, y-2], img[x+2, y-1], img[x+2, y], img[x+2, y+1], img[x+2, y+2]]
            minimo = min(elementos)
            matriz_final[x, y] = minimo
    cv.imshow("Minimo 5x5", matriz_final)
    cv.imshow("Original", img)
    cv.waitKey()


def maximo(img):
    # 3x3
    matriz_final = np.zeros_like(img)
    h, w = img.shape
    for x in range(1, h-2):
        for y in range(1, w-2):
            elementos = [img[x - 1, y - 1], img[x - 1, y], img[x-1, y + 1], img[x, y-1],
                         img[x, y], img[x, y+1], img[x+1, y-1], img[x+1, y], img[x+1, y+1]]
            maximo = max(elementos)
            matriz_final[x, y] = maximo
    cv.imshow("Maximo 3x3", matriz_final)
    cv.imshow("Original", img)
    cv.waitKey()

    matriz_final = np.zeros_like(img)
    for x in range(1, h-2):
        for y in range(1, w-2):
            elementos = [img[x-2, y-2], img[x-2, y-1], img[x-2, y], img[x-2, y+1], img[x-2, y+2], img[x-1, y-2], img[x-1, y-1], img[x-1, y], img[x-1, y+1], img[x-1, y+2], img[x, y-2], img[x, y-1],
                         img[x, y], img[x, y+1], img[x, y+2], img[x+1, y-2], img[x+1, y-1], img[x+1, y], img[x+1, y+1], img[x+1, y+2], img[x+2, y-2], img[x+2, y-1], img[x+2, y], img[x+2, y+1], img[x+2, y+2]]
            maximo = max(elementos)
            matriz_final[x, y] = maximo
    cv.imshow("Maximo 5x5", matriz_final)
    cv.imshow("Original", img)
    cv.waitKey()


def moda(img):
    # 3x3
    matriz_final = np.zeros_like(img)
    h, w = img.shape
    for x in range(1, h-2):
        for y in range(1, w-2):
            elementos = [img[x - 1, y - 1], img[x - 1, y], img[x-1, y + 1], img[x, y-1],
                         img[x, y], img[x, y+1], img[x+1, y-1], img[x+1, y], img[x+1, y+1]]
            moda = statistics.mode(elementos)
            matriz_final[x, y] = moda
    cv.imshow("Moda 3x3", matriz_final)
    cv.imshow("Original", img)
    cv.waitKey()

    matriz_final = np.zeros_like(img)
    for x in range(1, h-2):
        for y in range(1, w-2):
            elementos = [img[x-2, y-2], img[x-2, y-1], img[x-2, y], img[x-2, y+1], img[x-2, y+2], img[x-1, y-2], img[x-1, y-1], img[x-1, y], img[x-1, y+1], img[x-1, y+2], img[x, y-2], img[x, y-1],
                         img[x, y], img[x, y+1], img[x, y+2], img[x+1, y-2], img[x+1, y-1], img[x+1, y], img[x+1, y+1], img[x+1, y+2], img[x+2, y-2], img[x+2, y-1], img[x+2, y], img[x+2, y+1], img[x+2, y+2]]
            moda = statistics.mode(elementos)
            matriz_final[x, y] = moda
    cv.imshow("Moda 5x5", matriz_final)
    cv.imshow("Original", img)
    cv.waitKey()


def mediana(img):
    # tenho que pegar o elemento do "meio" após ordenar as coisas
    # 3x3
    matriz_final = np.zeros_like(img)
    h, w = img.shape
    for x in range(1, h-2):
        for y in range(1, w-2):
            lista = []
            elementos = [img[x - 1, y - 1], img[x - 1, y], img[x-1, y + 1], img[x, y-1],
                         img[x, y], img[x, y+1], img[x+1, y-1], img[x+1, y], img[x+1, y+1]]
            lista += elementos
            lista.sort()
            meio = math.ceil(len(lista)/2)
            matriz_final[x, y] = lista[meio]
    cv.imshow("Mediana 3x3", matriz_final)
    cv.imshow("Original", img)
    cv.waitKey()

    matriz_final = np.zeros_like(img)
    for x in range(1, h-2):
        for y in range(1, w-2):
            lista = []
            elementos = [img[x-2, y-2], img[x-2, y-1], img[x-2, y], img[x-2, y+1], img[x-2, y+2], img[x-1, y-2], img[x-1, y-1], img[x-1, y], img[x-1, y+1], img[x-1, y+2], img[x, y-2], img[x, y-1],
                         img[x, y], img[x, y+1], img[x, y+2], img[x+1, y-2], img[x+1, y-1], img[x+1, y], img[x+1, y+1], img[x+1, y+2], img[x+2, y-2], img[x+2, y-1], img[x+2, y], img[x+2, y+1], img[x+2, y+2]]
            lista += elementos
            lista.sort()
            meio = math.ceil(len(lista)/2)
            matriz_final[x, y] = lista[meio]
    cv.imshow("Mediana 5x5", matriz_final)
    cv.imshow("Original", img)
    cv.waitKey()


def media(img):
    mask3x3 = np.ones((3, 3), np.float64)/9
    mask5x5 = np.ones((5, 5), np.float64)/25
    h, w = img.shape
    matriz_final = np.zeros_like(img)  # é a matriz da convolução
    # 3x3 mediana
    for x in range(1, h - 2):
        for y in range(1, w - 2):
            matriz_final[x, y] = img[x - 1, y - 1] * mask3x3[0, 0] + img[x - 1, y] * mask3x3[0, 1] + img[x-1, y + 1] * mask3x3[0, 2] + img[x, y-1] * mask3x3[1, 0] + \
                img[x, y] * mask3x3[1, 1] + img[x, y+1] * mask3x3[1, 2] + img[x+1, y-1] * \
                mask3x3[2, 0] + img[x+1, y] * mask3x3[2, 1] + \
                img[x+1, y+1] * mask3x3[2, 2]
    cv.imshow("3x3", matriz_final.astype('uint8'))
    cv.imshow("original", img)
    cv.waitKey()
    # 5x5
    matriz_final = matriz_final.astype(np.int32)
    matriz_final = np.zeros_like(img)
    for x in range(1, h - 2):
        for y in range(1, w - 2):
            matriz_final[x, y] = (img[x-2, y-2] * mask5x5[0, 0]) * (img[x-2, y-1] * mask5x5[0, 1]) + (img[x-2, y] * mask5x5[0, 2]) + (img[x-2, y+1] * mask5x5[0, 3]) + (img[x-2, y+2] * mask5x5[0, 4]) + (img[x-1, y-2] * mask5x5[1, 0]) + (img[x-1, y-1] * mask5x5[1, 1]) + (img[x-1, y] * mask5x5[1, 2]) + (img[x-1, y+1] * mask5x5[1, 3]) + (img[x-1, y+2] * mask5x5[1, 4]) + (img[x, y-2] * mask5x5[2, 0]) + (img[x, y-1] * mask5x5[2, 1]) + \
                (img[x, y] * mask5x5[2, 2]) + (img[x, y+1] * mask5x5[2, 3]) + (img[x, y+2] * mask5x5[2, 4]) + (img[x+1, y-2] * mask5x5[3, 0]) + (img[x+1, y-1] * mask5x5[3, 1]) + (img[x+1, y] * mask5x5[3, 2]) + (img[x+1, y+1] *
                                                                                                                                                                                                                   mask5x5[3, 3]) + (img[x+1, y+2] * mask5x5[3, 4]) + (img[x+2, y-2] * mask5x5[4, 0]) + (img[x+2, y-1] *
                                                                                                                                                                                                                                                                                                         mask5x5[4, 1]) + (img[x+2, y] * mask5x5[4, 2]) + (img[x+2,
                                                                                                                                                                                                                                                                                                                                                               y+1] * mask5x5[4, 3]) + (img[x+2, y+2] * mask5x5[4, 4])
    cv.imshow("5x5", matriz_final.astype('uint8'))
    cv.imshow("original", img)
    cv.waitKey()


img = cv.imread(cv.samples.findFile(
    "/home/caiovinicius/repos/pdi/Processamento-Digital-de-Imagem/implementacoes/images/lena.pgm"), cv.IMREAD_UNCHANGED)

# media(img)
# cv.destroyAllWindows()
# mediana(img)
# cv.destroyAllWindows()
# moda(img)
# cv.destroyAllWindows()
# maximo(img)
# minimo(img)
# kuwahara(img)
# tomitaEtsuji(img)
# nagaoEMatsuyama(img)
# somboonkaew(img)
