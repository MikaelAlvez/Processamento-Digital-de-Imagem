import cv2
import numpy as np

def apply_freichen_operators(image):
    # Definir as nove máscaras de convolução
    masks = [
        np.array([[1, np.sqrt(2), 1], [0, 0, 0], [-1, -np.sqrt(2), -1]]),
        np.array([[1, 0, -1], [np.sqrt(2), 0, -np.sqrt(2)], [1, 0, -1]]),
        np.array([[0, -1, np.sqrt(2)], [1, 0, -1], [-np.sqrt(2), 1, 0]]),
        np.array([[np.sqrt(2), -1, 0], [-1, 0, 1], [0, 1, -np.sqrt(2)]]),
        np.array([[0, 1, 0], [-1, 0, -1], [0, 1, 0]]),
        np.array([[-1, 0, 1], [0, 0, 0], [1, 0, -1]]),
        np.array([[1, -2, 1], [-2, 4, -2], [1, -2, 1]]),
        np.array([[-2, 1, -2], [1, 4, 1], [-2, 1, -2]]),
        np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    ]

    # Inicializar uma lista para armazenar os resultados de cada máscara
    results = []

    # Aplicar cada máscara à imagem
    for mask in masks:
        filtered_image = cv2.filter2D(image, -1, mask)
        results.append(filtered_image)

    return results

imagem = cv2.imread('implementacoes\images\lena.pgm', cv2.IMREAD_GRAYSCALE)

# Aplicar o operador de Frei-Chen
resultado = apply_freichen_operators(imagem)

# Exibir as imagens resultantes
for i, image in enumerate(resultado):
    cv2.imshow(f'Resultado {i+1}', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
