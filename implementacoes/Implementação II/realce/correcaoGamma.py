import cv2 as cv
import numpy as np
img = cv.imread(cv.samples.findFile(
    "/home/caiovinicius/repos/pdi/Processamento-Digital-de-Imagem/implementacoes/images/lena.pgm"), cv.IMREAD_UNCHANGED)
cv.imshow("img", img)
cv.waitKey()
h, w = img.shape

imgAjustada = np.zeros_like(img).astype(np.float64)
gamma = 3
c = 1.0
for x in range(h):
    for y in range(w):
        imgAjustada[x, y] = (c * ((img[x, y]/255) ** gamma)) * 255
cv.imshow("imgAjustada", imgAjustada.astype("uint8"))
cv.imshow("img", img)
cv.waitKey()
