import cv2
import numpy as np

def detect_points(image_path, threshold):
    # Carregar a imagem em escala de cinza
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Aplicar uma operação de limiarização para binarizar a imagem
    _, binary_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    
    # Encontrar os contornos dos pontos na imagem binarizada
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Desenhar círculos nos pontos detectados
    result_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    for contour in contours:
        if cv2.contourArea(contour) > 0:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.circle(result_image, (x + w//2, y + h//2), 5, (0, 0, 255), -1)
    
    return result_image

# Caminho para a imagem de entrada
image_path = 'implementacoes\images\lena.pgm'

# Valor do limiar definido pelo usuário
threshold = int(input("Informe o valor do limiar (T): "))

# Realizar a detecção de pontos
result = detect_points(image_path, threshold)

# Exibir a imagem resultante
cv2.imshow('Detecção de Pontos', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
