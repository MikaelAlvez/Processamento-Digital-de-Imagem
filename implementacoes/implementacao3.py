import cv2 as cv
import sys
import numpy as np

path = cv.samples.findFile(
    "/home/caiovinicius/repos/pdi/Processamento-Digital-de-Imagem/implementacoes/images/lena_cor.jpg")
img = cv.imread(path, 1)  # IMREAD_UNCHANGED
if img is None:
    sys.exit("Could not read the image.")
h, w, channels = img.shape
if (channels == 1):
    cv.imshow("Imagem com só um componente", img)
    cv.waitKey()
    cv.destroyAllWindows()
elif (channels == 2):
    cv.imshow("Imagem com dois componentes", img)
    first, second = decompor(img)
    cv.imshow("first", first)
    cv.imshow("second", second)
    cv.waitKey()
    cv.destroyAllWindows()
elif (channels == 3):
    cv.imshow("Imagem com três componentes", img)
    first, second, third = decompor(img)
    cv.imshow("first", first)
    cv.imshow("second", second)
    cv.imshow("third", third)
    cv.waitKey()
    cv.destroyAllWindows()
    # converter
    cv.imshow("RGB para HSB", cv.cvtColor(img, cv.COLOR_BGR2HSV))
    cv.imshow("RGB para YUV", cv.cvtColor(img, cv.COLOR_BGR2YUV))
    # cv.imshow("RGB para CMYK", cv.cvtColor(img, cv.COLOR_BGR2CMYK))
else:
    cv.imshow("Imagem com quatro componentes", img)
    first, second, third, fourth = decompor(img)
    cv.imshow("first", first)
    cv.imshow("second", second)
    cv.imshow("third", third)
    cv.imshow("fourth", fourth)
    cv.waitKey()
    cv.destroyAllWindows()
    # convertendo

cv.waitKey()
cv.destroyAllWindows()
# Primeiro eu tenho que mostrar a imagem colorida e em seguida, mostrar as componentes dela.
