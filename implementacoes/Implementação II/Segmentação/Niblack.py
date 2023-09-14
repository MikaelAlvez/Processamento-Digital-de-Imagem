import cv2
import numpy as np

# Carregue a imagem em tons de cinza
imagem = cv2.imread('implementacoes\images\exemplo.jpg', cv2.IMREAD_GRAYSCALE)

# Solicitar ao usuário os valores de n e k
n = int(input("Digite o valor de n (tamanho da vizinhança): "))
k = float(input("Digite o valor de k (fator de ajuste): "))

# Defina o tamanho da imagem
altura, largura = imagem.shape

# Inicialize a imagem binarizada com zeros
imagem_binarizada = np.zeros((altura, largura), dtype=np.uint8)

# Calcule o desvio padrão local usando a função de filtro de caixa
std_dev = np.zeros_like(imagem, dtype=np.float32)

for i in range(altura):
    for j in range(largura):
        x1 = max(0, i - n // 2)
        x2 = min(altura, i + n // 2 + 1)
        y1 = max(0, j - n // 2)
        y2 = min(largura, j + n // 2 + 1)

        local_area = imagem[x1:x2, y1:y2]
        local_mean = np.mean(local_area)
        local_std_dev = np.std(local_area)

        limiar = local_mean + k * local_std_dev
        if imagem[i, j] > limiar:
            imagem_binarizada[i, j] = 255

# Exiba a imagem binarizada
cv2.imshow('Niblack', imagem_binarizada)
cv2.waitKey(0)
cv2.destroyAllWindows()
