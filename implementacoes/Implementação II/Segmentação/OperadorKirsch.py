import cv2
import numpy as np

def kirsch_operator(image):
    # Definir as oito máscaras de convolução
    kernels = [
        np.array([[5, -3, -3], [5, 0, -3], [5, -3, -3]]),
        np.array([[-3, -3, -3], [5, 0, -3], [5, 5, -3]]),
        np.array([[-3, -3, -3], [-3, 0, -3], [5, 5, 5]]),
        np.array([[-3, -3, -3], [-3, 0, 5], [-3, 5, 5]]),
        np.array([[-3, -3, 5], [-3, 0, 5], [-3, -3, 5]]),
        np.array([[-3, 5, 5], [-3, 0, 5], [-3, -3, -3]]),
        np.array([[5, 5, 5], [-3, 0, -3], [-3, -3, -3]]),
        np.array([[5, 5, -3], [5, 0, -3], [-3, -3, -3]])
    ]

    # Inicializa a matriz de magnitude do gradiente
    gradient_magnitude = np.zeros_like(image, dtype=np.float32)

    # Aplica cada máscara e manter o valor máximo
    for kernel in kernels:
        gradient = cv2.filter2D(image, -1, kernel)
        gradient_magnitude = np.maximum(gradient_magnitude, gradient)

    max_value = np.max(gradient_magnitude)
    print("Maior valor encontrado:", max_value)
    return gradient_magnitude


imagem = cv2.imread('implementacoes\images\lena.pgm', cv2.IMREAD_GRAYSCALE)

# Aplica o operador de Kirsh para calcular a magnitude do gradiente
resultado = kirsch_operator(imagem)

# Normaliza a imagem resultante para exibição
resultado = cv2.normalize(resultado, None, 0, 255, cv2.NORM_MINMAX)

# Converter para o tipo de dados uint8
resultado = resultado.astype(np.uint8)

cv2.imshow('Operador de Kirsh', resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()
