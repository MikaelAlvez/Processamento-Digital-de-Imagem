import numpy as np
import cv2 as cv
import math
import statistics

def minimo(img):
    # 3x3
    matriz_final = np.zeros_like(img)
    h,w = img.shape
    for x in range(1,h-2):
        for y in range(1,w-2):
            elementos = [img[x - 1, y - 1], img[x - 1, y], img[x-1, y + 1], img[x, y-1],img[x, y],img[x, y+1],img[x+1, y-1],img[x+1, y],img[x+1, y+1]]
            minimo = min(elementos)
            matriz_final[x,y] = minimo
    cv.imshow("Minimo 3x3", matriz_final)
    cv.imshow("Original", img)
    cv.waitKey()

    matriz_final = np.zeros_like(img)
    for x in range(1,h-2):
        for y in range(1,w-2):
            elementos = [img[x-2, y-2],img[x-2, y-1],img[x-2, y],img[x-2, y+1],img[x-2, y+2],img[x-1, y-2],img[x-1, y-1],img[x-1, y],img[x-1, y+1],img[x-1, y+2],img[x, y-2],img[x, y-1],img[x, y],img[x, y+1],img[x, y+2],img[x+1, y-2],img[x+1, y-1],img[x+1, y],img[x+1, y+1],img[x+1, y+2],img[x+2, y-2],img[x+2, y-1],img[x+2,y],img[x+2,y+1],img[x+2, y+2]]
            minimo = min(elementos)
            matriz_final[x,y] = minimo
    cv.imshow("Minimo 5x5", matriz_final)
    cv.imshow("Original", img)
    cv.waitKey()

def maximo(img):
    # 3x3
    matriz_final = np.zeros_like(img)
    h,w = img.shape
    for x in range(1,h-2):
        for y in range(1,w-2):
            elementos = [img[x - 1, y - 1], img[x - 1, y], img[x-1, y + 1], img[x, y-1],img[x, y],img[x, y+1],img[x+1, y-1],img[x+1, y],img[x+1, y+1]]
            maximo = max(elementos)
            matriz_final[x,y] = maximo
    cv.imshow("Maximo 3x3", matriz_final)
    cv.imshow("Original", img)
    cv.waitKey()

    matriz_final = np.zeros_like(img)
    for x in range(1,h-2):
        for y in range(1,w-2):
            elementos = [img[x-2, y-2],img[x-2, y-1],img[x-2, y],img[x-2, y+1],img[x-2, y+2],img[x-1, y-2],img[x-1, y-1],img[x-1, y],img[x-1, y+1],img[x-1, y+2],img[x, y-2],img[x, y-1],img[x, y],img[x, y+1],img[x, y+2],img[x+1, y-2],img[x+1, y-1],img[x+1, y],img[x+1, y+1],img[x+1, y+2],img[x+2, y-2],img[x+2, y-1],img[x+2,y],img[x+2,y+1],img[x+2, y+2]]
            maximo = max(elementos)
            matriz_final[x,y] = maximo
    cv.imshow("Maximo 5x5", matriz_final)
    cv.imshow("Original", img)
    cv.waitKey()


def moda(img):
    # 3x3
    matriz_final = np.zeros_like(img)
    h,w = img.shape
    for x in range(1,h-2):
        for y in range(1,w-2):
            elementos = [img[x - 1, y - 1], img[x - 1, y], img[x-1, y + 1], img[x, y-1],img[x, y],img[x, y+1],img[x+1, y-1],img[x+1, y],img[x+1, y+1]]
            moda = statistics.mode(elementos)
            matriz_final[x,y] = moda
    cv.imshow("Moda 3x3", matriz_final)
    cv.imshow("Original", img)
    cv.waitKey()

    matriz_final = np.zeros_like(img)
    for x in range(1,h-2):
        for y in range(1,w-2):
            elementos = [img[x-2, y-2],img[x-2, y-1],img[x-2, y],img[x-2, y+1],img[x-2, y+2],img[x-1, y-2],img[x-1, y-1],img[x-1, y],img[x-1, y+1],img[x-1, y+2],img[x, y-2],img[x, y-1],img[x, y],img[x, y+1],img[x, y+2],img[x+1, y-2],img[x+1, y-1],img[x+1, y],img[x+1, y+1],img[x+1, y+2],img[x+2, y-2],img[x+2, y-1],img[x+2,y],img[x+2,y+1],img[x+2, y+2]]
            moda = statistics.mode(elementos)
            matriz_final[x,y] = moda
    cv.imshow("Moda 5x5", matriz_final)
    cv.imshow("Original", img)
    cv.waitKey()

def mediana(img):
    # tenho que pegar o elemento do "meio" após ordenar as coisas
    # 3x3
    matriz_final = np.zeros_like(img)
    h,w = img.shape
    for x in range(1,h-2):
        for y in range(1,w-2):
            lista = []
            elementos = [img[x - 1, y - 1], img[x - 1, y], img[x-1, y + 1], img[x, y-1],img[x, y],img[x, y+1],img[x+1, y-1],img[x+1, y],img[x+1, y+1]]
            lista += elementos
            lista.sort()
            meio = math.ceil(len(lista)/2)
            matriz_final[x,y] = lista[meio]
    cv.imshow("Mediana 3x3", matriz_final)
    cv.imshow("Original", img)
    cv.waitKey()

    matriz_final = np.zeros_like(img)
    for x in range(1,h-2):
        for y in range(1,w-2):
            lista = []
            elementos = [img[x-2, y-2],img[x-2, y-1],img[x-2, y],img[x-2, y+1],img[x-2, y+2],img[x-1, y-2],img[x-1, y-1],img[x-1, y],img[x-1, y+1],img[x-1, y+2],img[x, y-2],img[x, y-1],img[x, y],img[x, y+1],img[x, y+2],img[x+1, y-2],img[x+1, y-1],img[x+1, y],img[x+1, y+1],img[x+1, y+2],img[x+2, y-2],img[x+2, y-1],img[x+2,y],img[x+2,y+1],img[x+2, y+2]]
            lista += elementos
            lista.sort()
            meio = math.ceil(len(lista)/2)
            matriz_final[x,y] = lista[meio]
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
                (img[x, y] * mask5x5[2, 2]) + (img[x, y+1] * mask5x5[2, 3]) + (img[x, y+2] * mask5x5[2, 4]) + (img[x+1, y-2] * mask5x5[3, 0]) + (img[x+1, y-1] * mask5x5[3, 1]) + (img[x+1, y] * mask5x5[3, 2]) + (img[x+1, y+1] * \
                mask5x5[3, 3]) + (img[x+1, y+2] * mask5x5[3, 4]) + (img[x+2, y-2] * mask5x5[4, 0]) + (img[x+2, y-1] * \
                mask5x5[4, 1]) + (img[x+2, y] * mask5x5[4, 2]) + (img[x+2,
                                                                  y+1] * mask5x5[4, 3]) + (img[x+2, y+2] * mask5x5[4, 4])
    cv.imshow("5x5", matriz_final.astype('uint8'))
    cv.imshow("original", img)
    cv.waitKey()


img = cv.imread(cv.samples.findFile(
    "/home/caio/repos/pdi/Processamento-Digital-de-Imagem/implementacoes/images/Lenasalp.pgm"), cv.IMREAD_UNCHANGED)

#media(img)
#cv.destroyAllWindows()
#mediana(img)
#cv.destroyAllWindows()
#moda(img)
#cv.destroyAllWindows()
#maximo(img)
minimo(img)