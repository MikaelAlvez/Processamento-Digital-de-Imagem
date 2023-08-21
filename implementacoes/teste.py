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


def cvtBGR2CMYK(path):
    image = Image.open(
        path)
    cmyk_image = image.convert('CMYK')
    bands = Image.Image.split(cmyk_image)
    arr = np.array(cmyk_image).astype('uint8')
    C = np.zeros_like(arr)
    C[:, :, 0] = np.array(bands[0]).astype('uint8')
    C[:,:,3] = np.array(bands[3]).astype(np.float64)
    M = np.zeros_like(arr)
    M[:, :, 1] = np.array(bands[1]).astype('uint8')
    Y = np.zeros_like(arr)
    Y[:, :, 2] = np.array(bands[2]).astype('uint8')
    K = np.zeros_like(arr)
    K[:, :, 3] = np.array(bands[3]).astype('uint8')
    print(arr[0][0])
    cv.imshow('cmyk', arr)
    cv.imshow('C', C)
    # cv.imshow('M', M)
    # cv.imshow('Y', Y)
    # cv.imshow('K', K)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return arr


path = cv.samples.findFile(
    "/home/caio/repos/pdi/Processamento-Digital-de-Imagem/implementacoes/images/lena_cor.jpg")
img = cv.imread(path)  # IMREAD_UNCHANGED
if img is None:
    sys.exit("Could not read the image.")
cmyk_1 = bgr_to_cmyk(img)
cv.imshow('aaaa', cmyk_1)
cmyk = cvtBGR2CMYK(path)
cv.imshow('bbbb', cmyk)
cv.waitKey(10000)
cv.destroyAllWindows()
# Primeiro eu tenho que mostrar a imagem colorida e em seguida, mostrar as componentes dela.
def converterHSV2BGR(hsv):
    h,w,channels = hsv.shape
    bgr = np.zeros((h,w,3))
    rgbdash = np.zeros((h,w,3)).astype('float')
    for x in range(h):
        for y in range(w):
            H = hsv[y,x,0]
            S = hsv[y,x,1]
            V = hsv[y,x,2]
            C = V * S
            X = C * (1 - abs(((H/60) % 2) - 1))
            M = V - C
            if(H >= 0 and H < 60):
                rgbdash[y,x] = (C,X,0)
            elif(H >= 60 and H < 120):
                rgbdash[y,x] = (X,C,0)
            elif(H >= 120 and H < 180):
                rgbdash[y,x] = (0,C,X)
            elif(H >= 180 and H < 240):
                rgbdash[y,x] = (0,X,C)
            elif(H >= 240 and H < 300):
                rgbdash[y,x] = (X,0,C)
            elif(H >= 300 and H < 360):
                rgbdash[y,x] = (C,0,X)
            bgr[y,x] = (rgbdash[y,x,2]+M * 255, rgbdash[y,x,1] + M * 255, rgbdash[y,x,0] + M * 255)
    print(bgr[0,0])
    bgr = bgr.astype('uint8')
    cv.imshow('bgr',bgr)
    cv.waitKey()
    return bgr
def converterBGR2HSV(img):
    h,w,channels = img.shape
    rDash = (img[:,:,2]/255).astype('float')
    gDash = (img[:,:,1]/255).astype('float')
    bDash = (img[:,:,0]/255).astype('float')
    HSV = np.zeros((h,w,3))
    for x in range(h):
        for y in range(w):
            cMax = max(rDash[y,x], gDash[y,x], bDash[y,x]) 
            cMin = min(rDash[y,x], gDash[y,x], bDash[y,x]) 
            delta = cMax - cMin
            if(delta == 0):
                H = 0
            elif(cMax == rDash[y,x]):
                H = 60 * (((gDash[y,x] - bDash[y,x])/delta) %6)
            elif(cMax == gDash[y,x]):
                H = 60 * (((bDash[y,x] - rDash[y,x])/delta) + 2)
            elif(cMax == bDash[y,x]):
                H = 60 * (((rDash[y,x] - gDash[y,x])/delta) + 4)
            if(cMax == 0):
                S = 0
            else:
                S = (delta/cMax)
            V = cMax
            HSV[y,x] = (H,S,V)
    return HSV
def decomporHSV(img):
    cv.destroyAllWindows()
    H = np.zeros_like(img)
    H[:,:,0] = img[:,:,0]
    H[:,:,2] = img[:,:,2]
    S = np.zeros_like(img)
    S[:,:,1] = img[:,:,1]
    S[:,:,2] = img[:,:,2]
    V = np.zeros_like(img)
    V[:,:,2] = img[:,:,2]
    cv.imshow("HSV", img)
    cv.imshow("H", cv.cvtColor(H,cv.COLOR_HSV2BGR))
    cv.imshow("S", cv.cvtColor(S,cv.COLOR_HSV2BGR))
    cv.imshow("V", cv.cvtColor(V,cv.COLOR_HSV2BGR))
    cv.waitKey()
    cv.destroyAllWindows()
