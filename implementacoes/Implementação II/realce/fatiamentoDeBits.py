import cv2 as cv
import numpy as np
img = cv.imread(cv.samples.findFile(
    "implementacoes\images\lena.pgm"), cv.IMREAD_UNCHANGED)
print(bin(img[0, 0]))
binary_representation = bin(img[0, 0])[2:]
print(binary_representation)

# vou pegar o valor binario e em seguida vou pegar o comprimento da string e comparar, quando for 1 então eu vou multiplicar o número pela  2n – 1 no qual n é igual a qual o bit significativo, ex : 0 0 0 0 1 1 1 1, o primeiro bit da direita tem n = 0

# pegando 8 planos de bit distintos
h, w = img.shape
for z in range(7):
    plano = np.zeros_like(img)
    for x in range(h):
        for y in range(w):
            binary_representation = bin(img[x, y])[2:]
            while(len(binary_representation) != 8):
                binary_representation = "0" + binary_representation;
            indiceFinal = len(binary_representation) - 1
            binary_representation = binary_representation[indiceFinal-z:indiceFinal+1]
            plano[x,y] = int(binary_representation,2)
    nome = "Plano " + str(z)
    cv.imshow(nome, plano)
cv.waitKey()
cv.destroyAllWindows()


for z in range(7):
    plano = np.zeros_like(img)
    for x in range(h):
        for y in range(w):
            binary_representation = bin(img[x, y])[2:]
            while(len(binary_representation) != 8):
                binary_representation = "0" + binary_representation;
            tam = len(binary_representation) - 1
            if(binary_representation[tam-z] == "1"):
                plano[x,y] = 255
            else:
                plano[x,y] = 0
    nome = "Plano " + str(z)
    cv.imshow(nome, plano)
cv.waitKey()