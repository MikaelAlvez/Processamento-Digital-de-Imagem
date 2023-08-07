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
        cv.waitKey(10000)
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
        fourth[:, :, 2] = img[:, :, 2]
        cv.imshow("first", first)
        cv.imshow("second", second)
        cv.imshow("fourth", fourth)
        cv.imshow("third", third)
        cv.waitKey(10000)
        cv.destroyAllWindows()


def cvtBGR2CMYK(img):
    bgrdash = img.astype(np.float64)/255

    # Calculate K as (1 - whatever is biggest out of Rdash, Gdash, Bdash)
    K = 1 - np.max(bgrdash, axis=2)

    # Calculate C
    C = (1-bgrdash[..., 2] - K)/(1-K)

    # Calculate M
    M = (1-bgrdash[..., 1] - K)/(1-K)

    # Calculate Y
    Y = (1-bgrdash[..., 0] - K)/(1-K)

    # Combine 4 channels into single image and re-scale back up to uint8
    CMYK = (np.dstack((C, M, Y, K)) * 255).astype(np.uint8)
    return CMYK


path = cv.samples.findFile(
    "/home/caiovinicius/repos/pdi/Processamento-Digital-de-Imagem/implementacoes/images/lena_cor.jpg")
img = cv.imread(path)  # IMREAD_UNCHANGED
if img is None:
    sys.exit("Could not read the image.")
h, w, channels = img.shape
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
    cmyk = cvtBGR2CMYK(img)
    print(cmyk[0][0], img[0][0])
    # print(hsb[0, 0], yuv[0, 0], cmyk[0, 0])
    # cv.imshow("BGR para HSB", hsb)
    # decompor(hsb)
    # cv.waitKey(10000)
    # cv.destroyAllWindows()
    # cv.imshow("BGR para YUV", yuv)
    # decompor(yuv)
    cv.imshow("BGR para CMYK", cmyk)
    decompor(cmyk)
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
