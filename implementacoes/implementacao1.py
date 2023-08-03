# abrindo a imagem - a função cv.imread consegue abrir vários formatos diferentes de imagem
import cv2 as cv
import sys
import numpy as np


def soma(img1, img2):
    altura, largura = img1.shape
    imgSoma = np.add(img1, img2, dtype='int32')
    maior_valor = max(max(linha) for linha in imgSoma)
    menor_valor = min(min(linha) for linha in imgSoma)
    resultado = np.copy(imgSoma)
    if (maior_valor > 255):
        for x in range(altura):
            for y in range(largura):
                a = 255 / (maior_valor - menor_valor)
                b = -a * menor_valor
    return resultado
def sub(img1,img2):
    altura, largura = img1.shape
    imgSub = np.subtract(img1, img2, dtype='int32')
    maior_valor = max(max(linha) for linha in imgSub)
    menor_valor = min(min(linha) for linha in imgSub)
    resultado = np.copy(imgSub)
    if (menor_valor < 0):
        for x in range(altura):
            for y in range(largura):
                a = 255 / (maior_valor - menor_valor)
                b = -a * menor_valor
                resultado[y, x] = round(a * imgSub[y,x] + b)
    return resultado
def div(img1,img2):
    altura, largura = img1.shape
    imgDiv = np.divide(img1, img2, dtype='float')
    maior_valor = max(max(linha) for linha in imgDiv)
    menor_valor = min(min(linha) for linha in imgDiv)
    resultado = np.copy(imgDiv).astype('uint8')
    for x in range(altura):
        for y in range(largura):
            resultado[y, x] = round(imgDiv[y,x])
    return resultado
def mul(img1,img2):
    altura, largura = img1.shape
    imgMul = np.multiply(img1, img2, dtype='int32')
    maior_valor = max(max(linha) for linha in imgMul)
    menor_valor = min(min(linha) for linha in imgMul)
    resultado = np.copy(imgMul)
    if (maior_valor > 255):
        for x in range(altura):
            for y in range(largura):
                a = 255 / (maior_valor - menor_valor)
                b = -a * menor_valor
                resultado[y, x] = round(a * imgMul[y,x] + b)
    return resultado

def logical_and(img1,img2):
    return cv.bitwise_and(img1,img2)
def logical_or(img1, img2):
    return cv.bitwise_or(img1,img2)
def logical_xor(img1,img2):
    return cv.bitwise_xor(img1,img2)

img = cv.imread(cv.samples.findFile("implementacoes\images\lena.pgm"))
if img is None:
    sys.exit("Could not read the image.")
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

img1 = np.array([[132,120,138],[84,110,200],[255,92,177]])
img2 = np.array([[152,92,107],[80,124,210],[230,100,164]])
img4 = np.array([[100,220,230],[45,95,120],[205,100,0]])
img3 = np.array([[200,100,100],[0,10,50],[50,250,120]])
imgSub = sub(img1, img2)
imgSoma = soma(img3, img4)
imgMul = mul(img1,2)
imgDiv = div(img1,2)
#cv.imshow("Img1", img1)
#cv.imshow("Img2", img2)
cv.imshow("ImgSoma", imgSoma)
#cv.imshow("ImgSub", imgSub)
cv.waitKey()
cv.destroyAllWindows()