import cv2 as cv
import sys
import numpy as np

def decomporBGR(img):
    b = np.zeros_like(img)
    b[:,:,0] = img[:,:,0]
    g = np.zeros_like(img)
    g[:,:,1] = img[:,:,1]
    r = np.zeros_like(img)
    r[:,:,2] = img[:,:,2]
    cv.imshow("B", b)
    cv.imshow("g", g)
    cv.imshow("r", r)
    cv.waitKey()
    cv.destroyAllWindows()

def decomporCMYK(cmyk):
    h,w,channels = cmyk.shape
    c = np.zeros_like(cmyk)
    c[:,:,0] = cmyk[:,:,0]
    c[:,:,3] = cmyk[:,:,3]
    m = np.zeros_like(cmyk)
    m[:,:,1] = cmyk[:,:,1]
    m[:,:,3] = cmyk[:,:,3]
    y = np.zeros_like(cmyk)
    y[:,:,2] = cmyk[:,:,2]
    y[:,:,3] = cmyk[:,:,3]
    k = np.zeros((h,w,4)) # criei um single channel
    k[:,:,3] = cmyk[:,:,3] 
    k = converterCMYK2BGR(k)
    cv.imshow("c",converterCMYK2BGR(c))
    cv.imshow('m', converterCMYK2BGR(m))
    cv.imshow('y', converterCMYK2BGR(y))
    #converterBGR2GRAY(k,"simples")

def decomporHSV(img):
    cv.destroyAllWindows()
    H = np.zeros_like(img)
    H[:,:,0] = img[:,:,0]
    S = np.zeros_like(img)
    S[:,:,1] = img[:,:,1]
    V = np.zeros_like(img)
    V[:,:,2] = img[:,:,2]
    #H = cv.cvtColor(H,cv.COLOR_HSV2BGR)
    #S = cv.cvtColor(S,cv.COLOR_HSV2BGR)
    #V = cv.cvtColor(V,cv.COLOR_HSV2BGR)
    cv.imshow("HSV", img)
    cv.imshow("H", H)
    cv.imshow("S", S)
    cv.imshow("V", V)
    cv.waitKey()
    cv.destroyAllWindows()

def converterBGR2CMYK(bgr):
    altura,largura,channels = bgr.shape
    bgrdash = bgr.astype(np.float64)/255.
    C = 1 - bgrdash[:,:,2]
    M = 1 - bgrdash[:,:,1]
    Y = 1 - bgrdash[:,:,0]
    CMY = np.dstack((C,M,Y))
    minValor = np.min(CMY,2)
    print(minValor[124,0])
    CMYK = np.zeros((altura,largura,4))
    for x in range(altura):
        for y in range(largura):
            if(minValor[y,x] == 1):
                CMYK[y,x] = (0,0,0,1)
            else:
                K = minValor[y,x]
                CMYK[y,x,0] = (C[y,x] - K) / (1 - K)
                CMYK[y,x,1] = (M[y,x] - K) / (1 - K) 
                CMYK[y,x,2] = (Y[y,x] - K) / (1 - K) 
                CMYK[y,x,3] = K 
    return (CMYK*255).astype('uint8')


def converterCMYK2BGR(cmyk):
    cmyk = cmyk / 255
    R = 255 * (1 - cmyk[:,:,0]) * (1 - cmyk[:,:,3])
    G = 255 * (1 - cmyk[:,:,1]) * (1 - cmyk[:,:,3])
    B = 255 * (1 - cmyk[:,:,2]) * (1 - cmyk[:,:,3])
    bgr = np.dstack((B,G,R)).astype('uint8')
    return bgr


def converterBGR2GRAY(img, tipo=""):
    h,w,channels = img.shape
    gray  = np.zeros((h,w))
    if(tipo == "simples"):
        gray = (img[:,:,0] * 0.333) + (img[:,:,1] * 0.333) + ( 0.333 * img[:,:,2])
        gray = gray.astype("uint8")
        cv.imshow("gray - solução simples", gray)
        cv.waitKey()
        cv.destroyAllWindows()
    elif(tipo == "NTSC"):
        gray = (img[:,:,0] * 0.114) + (img[:,:,1] * 0.587) + ( 0.299 * img[:,:,2])
        gray = gray.astype("uint8")
        cv.imshow("gray - NTSC", gray)
        cv.waitKey()
        cv.destroyAllWindows()

def decomporYUV(yuv):
    U = np.zeros_like(yuv)
    U[:,:,0] = yuv[:,:,1]
    U[:,:,1] = yuv[:,:,0]
    U = cv.cvtColor(U, cv.COLOR_YUV2BGR)
    V = np.zeros_like(yuv)
    V[:,:,2] = yuv[:,:,2]
    V[:,:,1] = yuv[:,:,0]
    V = cv.cvtColor(V, cv.COLOR_YUV2BGR)
    cv.imshow("YUV", yuv)
    cv.imshow("U", U)
    cv.imshow("V", V)
    cv.waitKey()
    cv.destroyAllWindows()


img = cv.imread(cv.samples.findFile(
    "/home/caio/repos/pdi/Processamento-Digital-de-Imagem/implementacoes/images/lena_cor.jpg"), cv.IMREAD_UNCHANGED)
# decompor rgb
cv.imshow("bgr", img)
decomporBGR(img)
#Converter BGR to CMYK
cmyk = converterBGR2CMYK(img)
cv.imshow("CMYK retornando para BGR",converterCMYK2BGR(cmyk))
decomporCMYK(cmyk)
# Converter BGR to gray
converterBGR2GRAY(img,"simples")
converterBGR2GRAY(img,"NTSC")
# Converter BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
decomporHSV(hsv)
# Converter BGR to yuv
yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)
decomporYUV(yuv)