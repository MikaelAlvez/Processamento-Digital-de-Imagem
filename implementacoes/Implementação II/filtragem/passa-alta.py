import cv2 as cv
import numpy as np


def high_boost(img):  # a - 1 * original + passa alta
    h, w = img.shape
    A = 2
    if (A >= 0):
        W = (9 * A) - 1
        mascara = np.array([[-1, -1, -1], [-1, W, -1], [-1, -1, -1]])
        print(mascara)
        passa_alta = np.zeros_like(img)
        orig = img * (A - 1)
        for x in range(1, h - 2):
            for y in range(1, w-2):
                passa_alta[x, y] = img[x-1, y-1] * mascara[0, 0] + img[x-1, y] * mascara[0, 1] + img[x-1, y+1] * mascara[0, 2] + img[x, y-1] * mascara[1, 0] + \
                    img[x, y] * mascara[1, 1] + img[x, y+1] * mascara[1, 2] + img[x+1, y-1] * \
                    mascara[2, 0] + img[x+1, y] * mascara[2, 1] + \
                    img[x+1, y+1] * mascara[2, 2]
        hb = orig + passa_alta
        cv.imshow("Original", img)
        cv.imshow("High Boost", hb)
        cv.waitKey()


def m3(img):
    h, w = img.shape
    mascara = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    matriz_final = np.zeros_like(img)
    for x in range(1, h-2):
        for y in range(1, w-2):
            matriz_final[x, y] = img[x-1, y-1] * mascara[0, 0] + img[x-1, y] * mascara[0, 1] + img[x-1, y+1] * mascara[0, 2] + img[x, y-1] * mascara[1, 0] + \
                img[x, y] * mascara[1, 1] + img[x, y+1] * mascara[1, 2] + img[x+1, y-1] * \
                mascara[2, 0] + img[x+1, y] * mascara[2, 1] + \
                img[x+1, y+1] * mascara[2, 2]
    cv.imshow("Filtro M3 ", matriz_final)
    cv.imshow("Original", img)
    cv.waitKey()


def m2(img):
    h, w = img.shape
    mascara = np.array([[1, -2, 1], [-2, 5, -2], [1, -2, 1]])
    matriz_final = np.zeros_like(img)
    for x in range(1, h-2):
        for y in range(1, w-2):
            matriz_final[x, y] = img[x-1, y-1] * mascara[0, 0] + img[x-1, y] * mascara[0, 1] + img[x-1, y+1] * mascara[0, 2] + img[x, y-1] * mascara[1, 0] + \
                img[x, y] * mascara[1, 1] + img[x, y+1] * mascara[1, 2] + img[x+1, y-1] * \
                mascara[2, 0] + img[x+1, y] * mascara[2, 1] + \
                img[x+1, y+1] * mascara[2, 2]
    cv.imshow("Filtro M2 ", matriz_final)
    cv.imshow("Original", img)
    cv.waitKey()


def m1(img):
    h, w = img.shape
    mascara = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    matriz_final = np.zeros_like(img)
    for x in range(1, h-2):
        for y in range(1, w-2):
            matriz_final[x, y] = img[x-1, y-1] * mascara[0, 0] + img[x-1, y] * mascara[0, 1] + img[x-1, y+1] * mascara[0, 2] + img[x, y-1] * mascara[1, 0] + \
                img[x, y] * mascara[1, 1] + img[x, y+1] * mascara[1, 2] + img[x+1, y-1] * \
                mascara[2, 0] + img[x+1, y] * mascara[2, 1] + \
                img[x+1, y+1] * mascara[2, 2]
    cv.imshow("Filtro M1 ", matriz_final)
    cv.imshow("Original", img)
    cv.waitKey()


def h2(img):  # perguntar se tem que dividir a mascara por 9.
    h, w = img.shape
    mascara = (np.array([[-1, -1, -1], [-1, 8, -1],
               [-1, -1, -1]]))
    matriz_final = np.zeros_like(img)
    for x in range(1, h-2):
        for y in range(1, w-2):
            matriz_final[x, y] = img[x-1, y-1] * mascara[0, 0] + img[x-1, y] * mascara[0, 1] + img[x-1, y+1] * mascara[0, 2] + img[x, y-1] * mascara[1, 0] + \
                img[x, y] * mascara[1, 1] + img[x, y+1] * mascara[1, 2] + img[x+1, y-1] * \
                mascara[2, 0] + img[x+1, y] * mascara[2, 1] + \
                img[x+1, y+1] * mascara[2, 2]
    cv.imshow("Filtro H2 ", matriz_final)
    cv.imshow("Original", img)
    cv.waitKey()


def h1(img):
    h, w = img.shape
    mascara = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    matriz_final = np.zeros_like(img)
    for y in range(1, h-2):
        for x in range(1, w-2):
            matriz_final[x, y] = img[x-1, y-1] * mascara[0, 0] + img[x-1, y] * mascara[0, 1] + img[x-1, y+1] * mascara[0, 2] + img[x, y-1] * mascara[1, 0] + \
                img[x, y] * mascara[1, 1] + img[x, y+1] * mascara[1, 2] + img[x+1, y-1] * \
                mascara[2, 0] + img[x+1, y] * mascara[2, 1] + \
                img[x+1, y+1] * mascara[2, 2]
    cv.imshow("Filtro H1 ", matriz_final)
    cv.imshow("Original", img)
    cv.waitKey()


img = cv.imread(cv.samples.findFile(
    "implementacoes\images\lena.pgm"), cv.IMREAD_UNCHANGED)
# h1(img)
# h2(img)
# m1(img)
# m2(img)
# m3(img)
# high_boost(img)
