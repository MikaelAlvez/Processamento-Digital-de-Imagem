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
    c = np.zeros_like(cmyk)
    c[:,:,0] = cmyk[:,:,0]
    cv.imshow("c",converterCMYK2BGR(c))




def converterBGR2CMYK(bgr):
    # primeiramente, converter para cmy
    bgrdash = bgr.astype(float)/255.

    # Calculate K as (1 - whatever is biggest out of Rdash, Gdash, Bdash)
    K  = 1 - np.max(bgrdash, axis=2)

    # Calculate C
    C = (1-bgrdash[...,2] - K)/(1-K)

    # Calculate M
    M = (1-bgrdash[...,1] - K)/(1-K)

    # Calculate Y
    Y = (1-bgrdash[...,0] - K)/(1-K)

    # Combine 4 channels into single image and re-scale back up to uint8
    CMYK = (np.dstack((C,M,Y,K)) * 255).astype(np.uint8)
    return CMYK

def converterCMYK2BGR(cmyk):
    h,w,channels = cmyk.shape
    bgr = np.zeros((h,w,3))
    print(1 - cmyk[0,0,0])
    bgr[:,:,2] = 255 * (1 - cmyk[:,:,0]/255) * (1 - cmyk[:,:,3]/255)
    bgr[:,:,1] = 255 * (1 - cmyk[:,:,1]/255) * (1 - cmyk[:,:,3]/255)
    bgr[:,:,0] = 255 * (1 - cmyk[:,:,2]/255) * (1 - cmyk[:,:,3]/255)
    cv.imshow("bgr", bgr.astype('uint8'))
    #print(bgr[0])
    return bgr
    cv.waitKey()

def converterBGR2GRAY(img, tipo=""):
    h,w,channels = img.shape
    gray  = np.zeros((255,255))
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



img = cv.imread(cv.samples.findFile(
    "/home/caio/repos/pdi/Processamento-Digital-de-Imagem/implementacoes/images/lena_cor.jpg"), cv.IMREAD_UNCHANGED)
# decompor rgb
cv.imshow("bgr", img)
decomporBGR(img)
#Converter BGR to CMYK
cmyk = converterBGR2CMYK(img)
converterBGR2GRAY(img,"simples")
converterBGR2GRAY(img,"NTSC")
decomporCMYK(cmyk)