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
    B = img[:, :, 0].astype(float)
    G = img[:, :, 1].astype(float)
    R = img[:, :, 2].astype(float)

    B_ = np.copy(B)
    G_ = np.copy(G)
    R_ = np.copy(R)

    K = np.zeros_like(B)
    C = np.zeros_like(B)
    M = np.zeros_like(B)
    Y = np.zeros_like(B)

    for i in range(B.shape[0]):
        for j in range(B.shape[1]):
            B_[i, j] = B[i, j]/255
            G_[i, j] = G[i, j]/255
            R_[i, j] = R[i, j]/255
            K[i, j] = 1 - max(B_[i, j], G_[i, j], R_[i, j])
            if (B_[i, j] == 0) and (G_[i, j] == 0) and (R_[i, j] == 0):
                # black
                C[i, j] = 0
                M[i, j] = 0
                Y[i, j] = 0
            else:
                C[i, j] = (1 - R_[i, j] - K[i, j])/float((1 - K[i, j]))
                M[i, j] = (1 - G_[i, j] - K[i, j])/float((1 - K[i, j]))
                Y[i, j] = (1 - B_[i, j] - K[i, j])/float((1 - K[i, j]))

    CMYK = (np.dstack((C, M, Y, K)) * 255).astype(np.uint8)
    return CMYK


path = cv.samples.findFile(
    "/home/caiovinicius/repos/pdi/Processamento-Digital-de-Imagem/implementacoes/images/lena_cor.jpg")
img = cv.imread(path, cv.IMREAD_UNCHANGED)  # IMREAD_UNCHANGED
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
