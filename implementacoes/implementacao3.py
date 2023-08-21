import cv2 as cv
import sys
import numpy as np
from PIL import Image


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
        fourth[:, :, 3] = img[:, :, 3]
        cv.imshow("first", first)
        cv.imshow("second", second)
        cv.imshow("third", third)
        cv.imshow("fourth", fourth)
        cv.waitKey(10000)
        cv.destroyAllWindows()


def hsv2rgb(hsv):
    h, w, channels = hsv.shape
    bgr = np.zeros_like(hsv)
    for x in range(h):
        for y in range(w):
            hi = np.floor(hsv[y, x, 0] / 60.0) % 6
            hi = hi.astype('uint8')
            v = hsv[y, x, 2].astype('float')
            f = (hsv[y, x, 0] / 60.0) - hi
            p = v * (1.0 - hsv[y, x, 1])
            q = v * (1.0 - (f * hsv[y, x, 1]))
            t = v * (1.0 - ((1.0 - f) * hsv[y, x, 1]))
            if (hi == 0):
                bgr[y, x] = [p, t, v]
            if (hi == 1):
                bgr[y, x] = [p, v, q]
            if (hi == 2):
                bgr[y, x] = [t, v, p]
            if (hi == 3):
                bgr[y, x] = [v, q, p]
            if (hi == 4):
                bgr[y, x] = [v, p, t]
            if (hi == 5):
                bgr[y, x] = [q, p, v]
    cv.imshow("bgr", bgr)
    cv.imshow("hsv", hsv)
    return bgr


def decomporYUV(image):
    R = np.zeros_like(image)
    R[:, :, 2] = image[:, :, 0] + (1.140*image[:, :, 2])
    G = np.zeros_like(image)
    G[:, :, 1] = image[:, :, 0] - 0.395*image[:, :, 1] - 0.581*image[:, :, 2]
    B = np.zeros_like(image)
    B[:, :, 0] = image[:, :, 0] + 2.032*image[:, :, 1]
    cv.imshow("Y", R)
    cv.imshow("G", G)
    cv.imshow("B", B)


def decomporHsv(image):
    H = np.zeros_like(image).astype('uint8')
    H[:, :, 0] = image[:, :, 0]
    S = np.zeros_like(image).astype('uint8')
    S[:, :, 1] = image[:, :, 1]
    V = np.zeros_like(image).astype('uint8')
    V[:, :, 2] = image[:, :, 2]
    cv.imshow("h", cv.cvtColor(H, cv.COLOR_HSV2BGR))
    cv.imshow("s", cv.cvtColor(S, cv.COLOR_HSV2BGR))
    cv.imshow("v", cv.cvtColor(V, cv.COLOR_HSV2BGR))
    cv.imshow("HSV", image)


def CMYK2BGR(image):
    rgb_scale = 255
    h, w, channels = image.shape
    image_array = np.zeros((h, w, 3), dtype=np.uint8)
    for x in range(h):
        for y in range(w):
            r = rgb_scale * \
                ((1 - (image[y, x, 0] / 100)) * (1 - image[y, x, 3] / 100))
            g = rgb_scale * \
                ((1 - (image[y, x, 1] / 100)) * (1 - image[y, x, 3] / 100))
            b = rgb_scale * \
                ((1 - (image[y, x, 2] / 100)) * (1 - image[y, x, 3] / 100))
            image_array[y, x] = [b, g, r]
    return image_array.astype('uint8')


def cvtBGR2CMYK(path):
    image = Image.open(
        path)
    cmyk_image = image.convert('CMYK')
    bands = Image.Image.split(cmyk_image)
    arr = np.array(cmyk_image).astype('uint8')
    C = np.zeros_like(arr)
    C[:, :, 0] = np.array(bands[0]).astype('uint8')
    cv.imshow('C', CMYK2BGR(C))
    M[:, :, 1] = np.array(bands[1]).astype('uint8')
    M = np.zeros_like(arr)
    cv.imshow('M', CMYK2BGR(M))
    Y = np.zeros_like(arr)
    Y[:, :, 2] = np.array(bands[2]).astype('uint8')
    cv.imshow('Y', CMYK2BGR(Y))
    K = np.zeros_like(arr)
    K[:, :, 3] = np.array(bands[3]).astype('uint8')
    cv.imshow('K', CMYK2BGR(K))
    cv.imshow("CMYK", arr)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return arr


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
    # cv.imshow("Imagem com três componentes", img)
    # decompor(img)
    # converter
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # arrumar os componentes desse
    yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)  # arrumar os componentes desse
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # cmyk = cvtBGR2CMYK(path)
    decomporYUV(yuv)
    # cv.imshow("BGR para Gray", gray)
    # decomporHsv(hsv)
    # hsv2rgb(hsv)
    # cv.waitKey(10000)
    # cv.destroyAllWindows()
    # cv.imshow("BGR para YUV", yuv)
    # decompor(yuv)
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
