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
            binario = bin(img[x, y])
            binary_representation = bin(img[x, y])[2:]
            if (z >= len(binary_representation)):
                plano[x, y] = 0
            else:
                plano[x, y] = int(binary_representation[z]) * (2**z - 1)
    nome = "Plano " + str(z)
    cv.imshow(nome, plano)
cv.waitKey()
