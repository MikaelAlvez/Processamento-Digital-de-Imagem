import cv2
import numpy as np

def detect_isolated_points(image_path, T):
    # Carregar a imagem em escala de cinza
    gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Definir a máscara h
    mask = np.array([[-1, -1, -1],
                     [-1,  8, -1],
                     [-1, -1, -1]])
    
    # Aplicar a convolução usando a máscara
    convolved_image = cv2.filter2D(gray_image, -1, mask)
    
    # Calcular as diferenças ponderadas
    weighted_diff = np.abs(convolved_image - gray_image)
    
    # Encontrar os pontos isolados acima do limiar
    isolated_points = (weighted_diff > T).astype(np.uint8) * 255
    
    # Exibir as imagens original e modificada lado a lado
    stacked_images = np.hstack((gray_image, isolated_points))
    cv2.imshow("Original vs Modified", stacked_images)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Caminho da imagem
image_path = "implementacoes\images\exemplo.jpg"

# Solicitar ao usuário que informe o valor de T
T = int(input("Informe o valor de T: "))

# Chamar a função de detecção de pontos isolados
detect_isolated_points(image_path, T)
