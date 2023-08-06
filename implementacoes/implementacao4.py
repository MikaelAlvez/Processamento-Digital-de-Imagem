import cv2 as cv
import numpy as np


def fatiamento(img):
    img_rgb = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
    img_rgb = np.zeros_like(img_rgb)
    altura, largura = img.shape
    for x in range(altura):
        for y in range(largura):
            if (img[y][x] >= 0 and img[y][x] < 80):
                img_rgb[y][x] = [255, 0, 0]
            elif (img[y][x] >= 80 and img[y][x] < 160):
                img_rgb[y][x] = [0, 255, 0]
            else:
                img_rgb[y][x] = [0, 0, 255]
    return img_rgb


def redistribuicao(img):
    altura, largura, channels = img.shape
    img_redistribuida = np.copy(img)
    for x in range(altura):
        for y in range(largura):
            if (img[y, x, 2] >= 150 and img[y, x, 1] < 60):
                img_redistribuida[y, x, 2] = 255
    return img_redistribuida


path = cv.samples.findFile(
    "/home/caiovinicius/repos/pdi/Processamento-Digital-de-Imagem/implementacoes/images/lena.pgm")
path_colorido = cv.samples.findFile(
    "/home/caiovinicius/repos/pdi/Processamento-Digital-de-Imagem/implementacoes/images/lena_cor.jpg")
img = cv.imread(path, cv.IMREAD_UNCHANGED)  # IMREAD_UNCHANGED
img_colorida = cv.imread(
    path_colorido, cv.IMREAD_UNCHANGED)  # IMREAD_UNCHANGED
# cv.imshow("fatiamento", fatiamento(img))
# cv.imshow("original", img)
cv.imshow('original colorida', img_colorida)
cv.imshow("redistribuida", redistribuicao(img_colorida))
cv.waitKey(100000)
cv.destroyAllWindows()
