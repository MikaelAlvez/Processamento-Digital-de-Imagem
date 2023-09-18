import cv2 as cv
import numpy as np
import statistics

def pontilhado_ordenado2x2(img):
    h,w = img.shape
    resultado = np.zeros_like(img)
    for y in range(0,h-1,2):
        for x in range(0,w-1,2):
            matriz = np.array([0,0,0,0])
            matriz[0] = img[x,y]
            matriz[1] = img[x,y]
            matriz[2] = img[x,y]
            matriz[3] = img[x,y]
            media = statistics.mean(matriz)
            if(media <= 51):
                matriz[0] = 0;
                matriz[1] = 0;
                matriz[2] = 0;
                matriz[3] = 0;
            elif(media <= 102):
                matriz[0] = 0;
                matriz[1] = 0;
                matriz[2] = 255;
                matriz[3] = 0;
            elif(media <= 153):
                matriz[0] = 0;
                matriz[1] = 255;
                matriz[2] = 255;
                matriz[3] = 0;
            elif(media <= 204):
                matriz[0] = 0;
                matriz[1] = 255;
                matriz[2] = 255;
                matriz[3] = 255;
            elif(media<= 255):
                matriz[0] = 255;
                matriz[1] = 255;
                matriz[2] = 255;
                matriz[3] = 255;
            resultado[x,y] = matriz[0];
            resultado[x + 1,y] = matriz[1];
            resultado[x,y+1] = matriz[2];
            resultado[x + 1,y + 1] = matriz[3];
    cv.imshow("2x2", resultado)
    cv.waitKey()


def pontilhadoOrdenado3x2(img):
    h,w = img.shape
    resultado = np.zeros_like(img)
    for y in range(0,h-1,2):
        for x in range(0,w-2,3):
            matriz = np.array([0,0,0,0,0,0])
            matriz[0] = img[x,y]
            matriz[1] = img[x,y]
            matriz[2] = img[x,y]
            matriz[3] = img[x,y]
            matriz[4] = img[x,y]
            matriz[5] = img[x,y]
            media = statistics.mean(matriz)
            if(media <= 36.43):
                matriz[0] = 0
                matriz[1] = 0
                matriz[2] = 0
                matriz[3] = 0
                matriz[4] = 0
                matriz[5] = 0
            elif(media <= 72.86):
                matriz[0] = 0
                matriz[1] = 0
                matriz[2] = 0
                matriz[3] = 255
                matriz[4] = 0
                matriz[5] = 0
            elif(media <= 109.29):
                matriz[0] = 0
                matriz[1] = 0
                matriz[2] = 255
                matriz[3] = 255
                matriz[4] = 0
                matriz[5] = 0
            elif(media <= 145.72):
                matriz[0] = 255
                matriz[1] = 0
                matriz[2] = 255
                matriz[3] = 255
                matriz[4] = 0
                matriz[5] = 0
            elif(media <= 182.15):
                matriz[0] = 255
                matriz[1] = 0
                matriz[2] = 255
                matriz[3] = 255
                matriz[4] = 255
                matriz[5] = 0
            elif(media <= 218.58):
                matriz[0] = 255
                matriz[1] = 0
                matriz[2] = 255
                matriz[3] = 255
                matriz[4] = 255
                matriz[5] = 255
            elif(media <= 255):
                matriz[0] = 255
                matriz[1] = 255
                matriz[2] = 255
                matriz[3] = 255
                matriz[4] = 255
                matriz[5] = 255
            resultado[x,y] = matriz[0];
            resultado[x + 1,y] = matriz[1];
            resultado[x + 2,y] = matriz[2];
            resultado[x,y+1] = matriz[3];
            resultado[x + 1,y + 1] = matriz[4];
            resultado[x + 2,y + 1] = matriz[5];
    cv.imshow("3x2", resultado)
    cv.waitKey()
def pontilhadoOrdenado3x3(img):
    h,w = img.shape
    resultado = np.zeros_like(img)
    for y in range(0,h-2,3):
        for x in range(0,w-2,3):
            matriz = np.array([0,0,0,0,0,0,0,0,0])
            matriz[0] = img[x,y]
            matriz[1] = img[x,y]
            matriz[2] = img[x,y]
            matriz[3] = img[x,y]
            matriz[4] = img[x,y]
            matriz[5] = img[x,y]
            matriz[6] = img[x,y]
            matriz[7] = img[x,y]
            matriz[8] = img[x,y]
            media = statistics.mean(matriz)
            if(media <= 25.5):
                    matriz[0] = 0
                    matriz[1] = 0
                    matriz[2] = 0
                    matriz[3] = 0
                    matriz[4] = 0
                    matriz[5] = 0
                    matriz[6] = 0
                    matriz[7] = 0
                    matriz[8] = 0
            elif(media <= 51):
                    matriz[0] = 0
                    matriz[1] = 0
                    matriz[2] = 0
                    matriz[3] = 0
                    matriz[4] = 255
                    matriz[5] = 0
                    matriz[6] = 0
                    matriz[7] = 0
                    matriz[8] = 0
            elif(media <= 76.5):
                    matriz[0] = 0
                    matriz[1] = 0
                    matriz[2] = 0
                    matriz[3] = 255
                    matriz[4] = 255
                    matriz[5] = 0
                    matriz[6] = 0
                    matriz[7] = 0
                    matriz[8] = 0
            elif(media <= 102):
                    matriz[0] = 0
                    matriz[1] = 0
                    matriz[2] = 0
                    matriz[3] = 255
                    matriz[4] = 255
                    matriz[5] = 0
                    matriz[6] = 0
                    matriz[7] = 255
                    matriz[8] = 0
            elif(media <= 127.5):
                    matriz[0] = 0
                    matriz[1] = 0
                    matriz[2] = 0
                    matriz[3] = 255
                    matriz[4] = 255
                    matriz[5] = 255
                    matriz[6] = 0
                    matriz[7] = 255
                    matriz[8] = 0
            elif(media <= 153):
                    matriz[0] = 0
                    matriz[1] = 0
                    matriz[2] = 255
                    matriz[3] = 255
                    matriz[4] = 255
                    matriz[5] = 255
                    matriz[6] = 0
                    matriz[7] = 255
                    matriz[8] = 0
            elif(media <= 178.5):
                    matriz[0] = 0
                    matriz[1] = 0
                    matriz[2] = 255
                    matriz[3] = 255
                    matriz[4] = 255
                    matriz[5] = 255
                    matriz[6] = 255
                    matriz[7] = 255
                    matriz[8] = 0
            elif(media <= 204):
                    matriz[0] = 255
                    matriz[1] = 0
                    matriz[2] = 255
                    matriz[3] = 255
                    matriz[4] = 255
                    matriz[5] = 255
                    matriz[6] = 255
                    matriz[7] = 255
                    matriz[8] = 0
            elif(media <= 229.5):
                    matriz[0] = 255
                    matriz[1] = 255
                    matriz[2] = 255
                    matriz[3] = 255
                    matriz[4] = 255
                    matriz[5] = 255
                    matriz[6] = 255
                    matriz[7] = 255
                    matriz[8] = 255
            elif(media <= 255):
                    matriz[0] = 255;
                    matriz[1] = 255;
                    matriz[2] = 255
                    matriz[3] = 255
                    matriz[4] = 255
                    matriz[5] = 255
                    matriz[6] = 255
                    matriz[7] = 255
                    matriz[8] = 255
            resultado[x,y] = matriz[0]
            resultado[x + 1,y] = matriz[1]
            resultado[x + 2,y] = matriz[2]
            resultado[x,y + 1] = matriz[3]
            resultado[x + 1,y + 1] = matriz[4]
            resultado[x + 2,y + 1] = matriz[5]
            resultado[x,y + 2] = matriz[6]
            resultado[x + 1,y + 2] = matriz[7]
            resultado[x + 2,y + 2] = matriz[8]
    cv.imshow("3x3", resultado)
    cv.waitKey()
def floydAndSteinberg(img):
     h,w = img.shape
     arr = np.array(img,dtype="float")
     for y in range(h-1):
        for x in range(w - 1):
            valorAproximado = 0 if arr[y,x] < 128 else 255
            erro = arr[y,x] - valorAproximado
            arr[y,x] = valorAproximado
            arr[y,x+1] += ((7.0*erro)/16)
            arr[y+1,x-1] += ((3.0*erro)/16)
            arr[y+1,x] += ((5.0*erro)/16)
            arr[y+1,x+1] += ((1.0*erro)/16) 
     for y in range(h):
        for x in range(w):
             if(arr[y,x] < 128):
                  arr[y,x] = 0
             else: arr[y,x] = 255   
     cv.imshow("Floyd and Steinberg", arr.astype('uint8'))
     cv.waitKey()
def rogers(img):
     h,w = img.shape
     arr = np.array(img,dtype='float')
     for y in range(h-1):
        for x in range(w - 1):
            valorAproximado = 0 if arr[y,x] < 128 else 255
            erro = arr[y,x] - valorAproximado
            arr[y,x] = valorAproximado
            arr[y,x+1] += ((erro * 3.0)/8)
            arr[y+1,x] += ((erro * 3.0)/8)
            arr[y+1,x+1] += ((erro * 2.0)/8)      
     for y in range(h):
        for x in range(w):
             if(arr[y,x] < 128):
                  arr[y,x] = 0
             else: arr[y,x] = 255 
     cv.imshow("Rogers", arr.astype('uint8'))
     cv.waitKey()
def jarvisJudiceNinke(img):
     h,w = img.shape
     arr = np.array(img,dtype='float')
     for y in range(h-2):
        for x in range(2,w - 2):
            valorAproximado = 0 if arr[y,x] < 128 else 255
            erro = arr[y,x] - valorAproximado
            arr[y,x] = valorAproximado
            arr[y,x+1] += ((erro * 7.0)/48)
            arr[y,x+2] += ((erro * 5.0)/48)
            arr[y+1,x-2] += ((erro * 3.0)/48)
            arr[y+1,x-1] += ((erro * 5.0)/48)
            arr[y+1,x] += ((erro * 7.0)/48)
            arr[y+1,x+1] += ((erro * 5.0)/48)
            arr[y+1,x+2] += ((erro * 3.0)/48)
            arr[y+2,x-2] += ((erro * 1.0)/48)
            arr[y+2,x-1] += ((erro * 3.0)/48)
            arr[y+2,x] += ((erro * 5.0)/48)
            arr[y+2,x+1] += ((erro * 3.0)/48)
            arr[y+2,x+2] += ((erro * 1.0)/48)
     for y in range(h):
        for x in range(w):
             if(arr[y,x] < 128):
                  arr[y,x] = 0
             else: arr[y,x] = 255 
     cv.imshow("Jarvis,Judice & Ninke", arr.astype('uint8'))
     cv.waitKey()
def stucki(img):
     h,w = img.shape
     arr = np.array(img,dtype='float')
     for y in range(h-2):
        for x in range(2,w - 2):
            valorAproximado = 0 if arr[y,x] < 128 else 255
            erro = arr[y,x] - valorAproximado
            arr[y,x] = valorAproximado
            arr[y,x+1] += ((erro * 8.0)/42)
            arr[y,x+2] += ((erro * 4.0)/42)
            arr[y+1,x-2] += ((erro * 2.0)/42)
            arr[y+1,x-1] += ((erro * 4.0)/42)
            arr[y+1,x] += ((erro * 8.0)/42)
            arr[y+1,x+1] += ((erro * 4.0)/42)
            arr[y+1,x+2] += ((erro * 2.0)/42)
            arr[y+2,x-2] += ((erro * 1.0)/42)
            arr[y+2,x-1] += ((erro * 2.0)/42)
            arr[y+2,x] += ((erro * 4.0)/42)
            arr[y+2,x+1] += ((erro * 2.0)/42)
            arr[y+2,x+2] += ((erro * 1.0)/42)
     for y in range(h):
        for x in range(w):
             if(arr[y,x] < 128):
                  arr[y,x] = 0
             else: arr[y,x] = 255 
     cv.imshow("Stucki", arr.astype('uint8'))
     cv.waitKey()
def stevensonAndArce(img):
     h,w = img.shape
     arr = np.array(img,dtype='float')
     for y in range(h-3):
        for x in range(3,w - 3):
            valorAproximado = 0 if arr[y,x] < 128 else 255
            erro = arr[y,x] - valorAproximado
            arr[y,x] = valorAproximado
            arr[y,x+2] += ((erro * 32.0)/200)
            arr[y+1,x-3] += ((erro * 12.0)/200)
            arr[y+1,x-1] += ((erro * 26.0)/200)
            arr[y+1,x+1] += ((erro * 30.0)/200)
            arr[y+1,x+3] += ((erro * 16.0)/200)
            arr[y+2,x-2] += ((erro * 12.0)/200)
            arr[y+2,x] += ((erro * 26.0)/200)
            arr[y+2,x+2] += ((erro * 12.0)/200)
            arr[y+3,x-3] += ((erro * 5.0)/200)
            arr[y+3,x-1] += ((erro * 12.0)/200)
            arr[y+3,x+1] += ((erro * 12.0)/200)
            arr[y+3,x+3] += ((erro * 5.0)/200)
     for y in range(h):
        for x in range(w):
             if(arr[y,x] < 128):
                  arr[y,x] = 0
             else: arr[y,x] = 255 
     cv.imshow("Stevenson and Arce", arr.astype('uint8'))
     cv.waitKey()
img = cv.imread(cv.samples.findFile(
    "/home/caiovinicius/repos/pdi/Processamento-Digital-de-Imagem/implementacoes/images/lena.pgm"), cv.IMREAD_UNCHANGED)
pontilhado_ordenado2x2(img)
pontilhadoOrdenado3x2(img)
pontilhadoOrdenado3x3(img)
floydAndSteinberg(img)
rogers(img)
jarvisJudiceNinke(img)
stucki(img)
stevensonAndArce(img)