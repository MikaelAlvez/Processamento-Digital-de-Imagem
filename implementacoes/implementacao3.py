import cv2 as cv
import sys
import numpy as np


def decompor(img):
    h, w, channels = img.shape
    if channels == 2:
        first = np.zeros_like(img)
        second = np.zeros_like(img)
        first[:, :, 0] = img[:, :, 0]
        second[:, :, 1] = img[:, :, 1]
        cv.imshow("first", first)
        cv.imshow("second", second)
    if channels == 3:
        first = np.zeros_like(img)
        second = np.zeros_like(img)
        third = np.zeros_like(img)
        first[:, :, 0] = img[:, :, 0]
        second[:, :, 1] = img[:, :, 1]
        third[:, :, 2] = img[:, :, 2]
        cv.imshow("first", first)
        cv.imshow("second", second)
        cv.imshow("third", third)
        cv.waitKey(0)
        cv.destroyAllWindows()
    if channels == 4:
        # print(img[:, :, 0])
        first = np.zeros_like(img)
        second = np.zeros_like(img)
        third = np.zeros_like(img)
        fourth = np.zeros_like(img)
        first[:, :, 0] = img[:, :, 0]
        second[:, :, 1] = img[:, :, 1]
        third[:, :, 2] = img[:, :, 2]
        fourth[:, :, 3] = img[:, :, 3]
        cv.imshow("first", first)
        cv.imshow("second", second)
        cv.imshow("third", third)
        cv.imshow("fourth", fourth)
        cv.waitKey(0)
        cv.destroyAllWindows()


def bgr_to_cmyk(img):
    RGB_SCALE = 255
    CMYK_SCALE = 100
    altura, largura, bands = img.shape
    resultado = np.zeros((altura, largura, 4), dtype=np.uint8)
    for x in range(altura):
        for y in range(largura):
            r = img[y, x, 2]
            g = img[y, x, 1]
            b = img[y, x, 0]
            if (r, g, b) == (0, 0, 0):
                # black
                resultado[y, x] = [0, 0, 0, CMYK_SCALE]
            # rgb [0,255] -> cmy [0,1]
            C = 1 - r / RGB_SCALE
            M = 1 - g / RGB_SCALE
            Y = 1 - b / RGB_SCALE
            # extract out k [0, 1]
            min_cmy = min(C, M, Y)
            C = (C - min_cmy) / (1 - min_cmy)
            M = (M - min_cmy) / (1 - min_cmy)
            Y = (Y - min_cmy) / (1 - min_cmy)
            K = min_cmy
            resultado[y, x] = [round(
                C * CMYK_SCALE), round(M * CMYK_SCALE), round(Y * CMYK_SCALE), round(K * CMYK_SCALE)]
            # rescale to the range [0,CMYK_SCALE]
    return resultado



path = cv.samples.findFile(
    "implementacoes\images\lena_cor.jpg")
img = cv.imread(path)  # IMREAD_UNCHANGED
if img is None:
    sys.exit("Could not read the image.")
h, w, channels = img.shape
# cmyk_1 = bgr_to_cmyk(img)
# cv.imshow('aaaa', cmyk_1)
# cv.waitKey(0)
if (channels == 1):
    cv.imshow("Imagem com só um componente", img)
    cv.waitKey()
    cv.destroyAllWindows()
elif (channels == 2):
    cv.imshow("Imagem com dois componentes", img)
    decompor(img)
    cv.waitKey()
    cv.destroyAllWindows()
elif (channels == 3):
    cv.imshow("Imagem com três componentes", img)
    decompor(img)
    # converter
    hsb = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #cmyk = cvtBGR2CMYK(path)
    cmyk = bgr_to_cmyk(img)
    cv.imshow("BGR para Gray", gray)
    cv.imshow("BGR para HSB", hsb)
    decompor(hsb)
    cv.imshow("BGR para CMYK", cmyk)
    decompor(cmyk)
    # cv.waitKey(10000)
    # cv.destroyAllWindows()
    cv.imshow("BGR para YUV", yuv)
    decompor(yuv)
    # cv.waitKey()
    # cv.destroyAllWindows()
else:
    cv.imshow("Imagem com quatro componentes", img)
    decompor(img)
    cv.waitKey(10000)
    cv.destroyAllWindows()

cv.waitKey(10000)
cv.destroyAllWindows()
# Primeiro eu tenho que mostrar a imagem colorida e em seguida, mostrar as componentes dela.
