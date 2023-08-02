import cv2 as cv
import sys
import numpy as np

path = cv.samples.findFile("/home/caiovinicius/repos/pdi/Processamento-Digital-de-Imagem/implementacoes/images/lena_cor.jpg")
img = cv.imread(path, 1) # IMREAD_UNCHANGED
if img is None:
    sys.exit("Could not read the image.")
img2 = cv.cvtColor(img, cv.COLOR_BGR2RGBA)
cv.imshow("img BGR",img)
cv.imshow("img RGB",img2)
b,g,r = cv.split(img)
cv.waitKey()
cv.destroyAllWindows()
# Primeiro eu tenho que mostrar a imagem colorida e em seguida, mostrar as componentes dela.
