import cv2
import numpy as np

# Carregar a imagem em tons de cinza
gray_image = cv2.imread('implementacoes\images\imageteste.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar um mapa de cores (colormap) para a pseudocolorização
colored_image = cv2.applyColorMap(gray_image, cv2.COLORMAP_JET)

# Mostrar a imagem pseudocolorizada
cv2.imshow('Pseudocolorizada', colored_image)
cv2.waitKey(0)

# Carregar a imagem colorida
color_image = cv2.imread('implementacoes\images\imageteste.jpg')

# Converter a imagem para escala de cinza
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

# Aplicar um mapa de cores (colormap) para a pseudocolorização
colored_image = cv2.applyColorMap(gray_image, cv2.COLORMAP_HOT)

# Mostrar a imagem colorida e pseudocolorizada lado a lado
stacked_image = np.hstack((color_image, colored_image))
cv2.imshow('Original vs Pseudocolorizada', stacked_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
