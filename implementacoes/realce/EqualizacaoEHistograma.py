import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np


image = cv.imread('implementacoes/images/lena.pgm', cv.IMREAD_GRAYSCALE)

histogram = cv.calcHist([image], [0], None, [256], [0, 256])
histogram = np.squeeze(histogram)
equalized = cv.equalizeHist(image)
plt.figure(figsize=(8, 6))
plt.title('Histograma dos Níveis de Cinza')
plt.xlabel('Nível de Cinza')
plt.ylabel('Frequência')
plt.plot(histogram, color='black')
plt.xlim([0, 255])
plt.show()
histogram = cv.calcHist([equalized], [0], None, [256], [0, 256])
histogram = np.squeeze(histogram)
plt.figure(figsize=(8, 6))
plt.title('Histograma equalizado dos Níveis de Cinza')
plt.xlabel('Nível de Cinza')
plt.ylabel('Frequência')
plt.plot(histogram, color='black')
plt.xlim([0, 255])
plt.show()
cv.imshow("Original", image)
cv.imshow("Equalizada", equalized)
cv.waitKey()
