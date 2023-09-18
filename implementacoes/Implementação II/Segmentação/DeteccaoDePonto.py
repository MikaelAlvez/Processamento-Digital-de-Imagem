import cv2
import numpy as np

def detect_isolated_points(image_path, T):
    gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # máscara h
    mask = np.array([[-1, -1, -1],
                     [-1,  8, -1],
                     [-1, -1, -1]])
    
    # Convolução usando a máscara
    convolved_image = cv2.filter2D(gray_image, -1, mask)
    
    # Calcular as diferenças ponderadas
    weighted_diff = np.abs(convolved_image - gray_image)
    
    # Encontrar os pontos isolados acima do limiar
    # isolated_points = (weighted_diff > T).astype(np.uint8) * 255
    isolated_points = (convolved_image > T).astype(np.uint8) * 255

    stacked_images = np.hstack((gray_image, isolated_points))
    cv2.imshow("Original vs Modified", stacked_images)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = "implementacoes\images\lena.pgm"

T = int(input("Informe o valor de T: "))

detect_isolated_points(image_path, T)
