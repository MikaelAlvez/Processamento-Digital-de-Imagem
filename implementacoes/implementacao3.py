import cv2 as cv
import sys
import numpy as np


def decomporBGR(img):
    b = np.zeros_like(img)
    b[:, :, 0] = img[:, :, 0]
    g = np.zeros_like(img)
    g[:, :, 1] = img[:, :, 1]
    r = np.zeros_like(img)
    r[:, :, 2] = img[:, :, 2]
    cv.imshow("B", b)
    cv.imshow("g", g)
    cv.imshow("r", r)
    cv.waitKey()
    cv.destroyAllWindows()


def decomporCMYK(cmyk):
    h, w, channels = cmyk.shape
    c = np.zeros_like(cmyk)
    c[:, :, 0] = cmyk[:, :, 0]
    m = np.zeros_like(cmyk)
    m[:, :, 1] = cmyk[:, :, 1]
    y = np.zeros_like(cmyk)
    y[:, :, 2] = cmyk[:, :, 2]
    k = np.zeros((h, w))  # criei um single channel
    k = cmyk[:, :, 3]
    cv.imshow("c", converterCMYK2BGR(c))
    cv.imshow('m', converterCMYK2BGR(m))
    cv.imshow('y', converterCMYK2BGR(y))
    cv.imshow('k', k)
    cv.waitKey()


def decomporHSV(img):
    h, w, channels = img.shape
    cv.destroyAllWindows()
    H = np.zeros((h, w))
    H = img[:, :, 0]
    S = np.zeros((h, w))
    S = img[:, :, 1]
    V = np.zeros((h, w))
    V = img[:, :, 2]
    cv.imshow("HSV", img)
    cv.imshow("H", H)
    cv.imshow("S", S)
    cv.imshow("V", V)
    cv.waitKey()
    cv.destroyAllWindows()


def converterBGR2CMYK(bgr):
    bgrdash = bgr.astype(np.float64)/255.

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


def converterCMYK2BGR(cmyk):
    cmyk = cmyk / 255
    R = 255 * (1 - cmyk[:, :, 0]) * (1 - cmyk[:, :, 3])
    G = 255 * (1 - cmyk[:, :, 1]) * (1 - cmyk[:, :, 3])
    B = 255 * (1 - cmyk[:, :, 2]) * (1 - cmyk[:, :, 3])
    bgr = np.dstack((B, G, R)).astype('uint8')
    return bgr


def converterBGR2GRAY(img, tipo=""):
    h, w, channels = img.shape
    gray = np.zeros((h, w))
    if (tipo == "simples"):
        gray = (img[:, :, 0] * 0.333) + \
            (img[:, :, 1] * 0.333) + (0.333 * img[:, :, 2])
        gray = gray.astype("uint8")
        cv.imshow("gray - solução simples", gray)
        cv.waitKey()
        cv.destroyAllWindows()
    elif (tipo == "NTSC"):
        gray = (img[:, :, 0] * 0.114) + \
            (img[:, :, 1] * 0.587) + (0.299 * img[:, :, 2])
        gray = gray.astype("uint8")
        cv.imshow("gray - NTSC", gray)
        cv.waitKey()
        cv.destroyAllWindows()


def decomporYUV(yuv):
    h, w, channels = yuv.shape
    Y = np.zeros((h, w))
    Y = yuv[:, :, 0]
    U = np.zeros_like(yuv)
    U[:, :, 0] = yuv[:, :, 1]
    U[:, :, 1] = yuv[:, :, 0]
    V = np.zeros_like(yuv)
    V[:, :, 2] = yuv[:, :, 2]
    V[:, :, 1] = yuv[:, :, 0]
    cv.imshow("YUV", yuv)
    cv.imshow("Y", Y)
    cv.imshow("U", U)
    cv.imshow("V", V)
    cv.waitKey()
    cv.destroyAllWindows()


img = cv.imread(cv.samples.findFile(
    "/home/caiovinicius/repos/pdi/Processamento-Digital-de-Imagem/implementacoes/images/lena_cor.jpg"), cv.IMREAD_UNCHANGED)
# decompor rgb
cv.imshow("bgr", img)
decomporBGR(img)
# Converter BGR to CMYK
cmyk = converterBGR2CMYK(img)
# cv.imshow("CMYK retornando para BGR", converterCMYK2BGR(cmyk))
decomporCMYK(cmyk)
# Converter BGR to gray
converterBGR2GRAY(img, "simples")
converterBGR2GRAY(img, "NTSC")
# Converter BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
decomporHSV(hsv)
# Converter BGR to yuv
yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)
decomporYUV(yuv)
