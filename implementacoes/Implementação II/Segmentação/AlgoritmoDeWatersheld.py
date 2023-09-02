import cv2
import numpy as np

# Carregue a imagem
imagem = cv2.imread('implementacoes\images\Captura de tela 2023-09-02 135409.png')
imagem_original = imagem.copy()

# Converta a imagem para escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Aplique um limiar para segmentar a imagem
_, thresh = cv2.threshold(imagem_cinza, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Remova o ruído usando a abertura morfológica
kernel = np.ones((3, 3), np.uint8)
abertura = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# Encontre os marcadores para o algoritmo Watershed
dist_transform = cv2.distanceTransform(abertura, cv2.DIST_L2, 5)
_, markers = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
markers = cv2.connectedComponents(markers.astype(np.uint8))[1]

# Aplique o algoritmo Watershed
cv2.watershed(imagem, markers)

# Destaque as linhas de contenção em vermelho
imagem[markers == -1] = [0, 0, 255]

# Exibir a imagem resultante com as regiões segmentadas e as linhas de contenção
cv2.imshow('Imagem Segmentada', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
