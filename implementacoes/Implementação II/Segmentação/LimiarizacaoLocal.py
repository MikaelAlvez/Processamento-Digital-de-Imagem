import cv2

# Carregue a imagem em tons de cinza
imagem = cv2.imread('implementacoes\images\lena.pgm', cv2.IMREAD_GRAYSCALE)

# Especificação do tamanho da janela de vizinhança e constante de subtração
tamanho_janela = 51  # Tamanho da janela de vizinhança
constante_subtracao = 10  # Valor a ser subtraído da média/máximo/mínimo

# Aplique a limiarização local baseada na média
imagem_binarizada_media = cv2.adaptiveThreshold(imagem, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, tamanho_janela, constante_subtracao)

# Aplique a limiarização local baseada no máximo
imagem_binarizada_maximo = cv2.adaptiveThreshold(imagem, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, tamanho_janela, constante_subtracao)

# Aplique a limiarização local baseada no mínimo
imagem_binarizada_minimo = cv2.adaptiveThreshold(imagem, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, tamanho_janela, constante_subtracao)

# Exiba as imagens binarizadas
cv2.imshow('Media', imagem_binarizada_media)
cv2.imshow('Maximo', imagem_binarizada_maximo)
cv2.imshow('Minimo', imagem_binarizada_minimo)

cv2.waitKey(0)
cv2.destroyAllWindows()
