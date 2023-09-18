import cv2
import numpy as np

imagem = cv2.imread('implementacoes\images\lena.pgm', cv2.IMREAD_GRAYSCALE)

# Passo 1: Estimar um valor inicial para o limiar
limiar_inicial = np.mean(imagem)

# Defina um critério de parada para a convergência do limiar
limiar_atual = limiar_inicial
limiar_anterior = 0
tolerancia = 1  # Valor de tolerância para a convergência

while abs(limiar_atual - limiar_anterior) > tolerancia:
    # Passo 2: Particionar a imagem em duas regiões
    regiao1 = imagem <= limiar_atual
    regiao2 = imagem > limiar_atual

    # Passo 3: Calcular os valores médios das intensidades em cada região
    u1 = np.mean(imagem[regiao1])
    u2 = np.mean(imagem[regiao2])

    # Passo 4: Calcular o novo limiar
    limiar_anterior = limiar_atual
    limiar_atual = (u1 + u2) / 2

# Passo 5: Limiar final
limiar_final = limiar_atual

# Aplicar a limiarização final
imagem_binarizada = (imagem > limiar_final).astype(np.uint8) * 255

cv2.imshow('Limiarizacao global', imagem_binarizada)
cv2.waitKey(0)
cv2.destroyAllWindows()
