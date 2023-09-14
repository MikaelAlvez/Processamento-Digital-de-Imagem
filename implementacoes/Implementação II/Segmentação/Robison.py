import cv2
import numpy as np

def robison_operator(image):
    # Definir as oito máscaras de convolução
    kernels = [
        np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]]),
        np.array([[0, -1, -2], [1, 0, -1], [2, 1, 0]]),
        np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]),
        np.array([[-2, -1, 0], [-1, 0, 1], [0, 1, 2]]),
        np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]),
        np.array([[0, 1, 2], [-1, 0, 1], [-2, -1, 0]]),
        np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]]),
        np.array([[2, 1, 0], [1, 0, -1], [0, -1, -2]])
    ]

    # Inicializar a matriz de magnitude do gradiente
    gradient_magnitude = np.zeros_like(image, dtype=np.float32)

    # Aplicar cada máscara e manter o valor máximo
    for kernel in kernels:
        gradient = cv2.filter2D(image, -1, kernel)
        gradient_magnitude = np.maximum(gradient_magnitude, np.abs(gradient))

    return gradient_magnitude

# Carregar a imagem em escala de cinza
imagem = cv2.imread('implementacoes\images\lena.pgm', cv2.IMREAD_GRAYSCALE)

# Aplicar o operador de Robison para calcular a magnitude do gradiente
resultado = robison_operator(imagem)

# Normalizar a imagem resultante para exibição
resultado = cv2.normalize(resultado, None, 0, 255, cv2.NORM_MINMAX)

# Converter para o tipo de dados uint8
resultado = resultado.astype(np.uint8)

# Exibir a imagem resultante
cv2.imshow('Robison', resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()
