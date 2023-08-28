import cv2
import numpy as np

def apply_log_transform(image):
    # Cálculo do valor máximo de intensidade presente na imagem
    fmax = np.max(image)

    # Cálculo do parâmetro 'a' para a transformação logarítmica
    a = 255 / np.log(1 + fmax)

    # Aplicando a transformação logarítmica
    transformed_image = a * np.log1p(image)

    # Garantindo que os valores da imagem transformada estejam dentro do intervalo [0, 255]
    transformed_image = np.clip(transformed_image, 0, 255).astype(np.uint8)

    return transformed_image

def apply_square_root_transform(image):
    # Cálculo do valor máximo de intensidade presente na imagem
    fmax = np.max(image)

    # Cálculo do parâmetro 'a' para a transformação de raiz quadrada
    a = 255 / np.sqrt(fmax)

    # Aplicando a transformação de raiz quadrada
    transformed_image = a * np.sqrt(image)

    # Garantindo que os valores da imagem transformada estejam dentro do intervalo [0, 255]
    transformed_image = np.clip(transformed_image, 0, 255).astype(np.uint8)

    return transformed_image

def apply_exponential_transform(image):
    # Cálculo do parâmetro 'a' para a transformação exponencial
    a = 255 / (np.exp(np.max(image) / 255.0) - 1)

    # Aplicando a transformação exponencial
    transformed_image = a * (np.exp(image / 255.0) - 1)

    # Garantindo que os valores da imagem transformada estejam dentro do intervalo [0, 255]
    transformed_image = np.clip(transformed_image, 0, 255).astype(np.uint8)

    return transformed_image

def apply_square_transform(image):
    # Cálculo do valor máximo de intensidade presente na imagem
    fmax = np.max(image)

    # Cálculo do parâmetro 'a' para a transformação de quadrado
    a = 1

    # Aplicando a transformação de quadrado
    transformed_image = a * (image ** 2)

    # Garantindo que os valores da imagem transformada estejam dentro do intervalo [0, 255]
    transformed_image = np.clip(transformed_image, 0, 255).astype(np.uint8)

    return transformed_image

image = cv2.imread('implementacoes\images\imageteste.jpg', cv2.IMREAD_GRAYSCALE)

while True:
    # Exibindo um menu de opções
    print("Escolha uma operação:")
    print("A) Transformação Logarítmica")
    print("B) Transformação de Raiz Quadrada")
    print("C) Transformação Exponencial")
    print("D) Transformação de Quadrado")
    print("S) Sair")

    choice = input("Opção: ")

    if choice == 'A' or choice == 'a':
        transformed_image = apply_log_transform(image)
        cv2.imshow('Transformed Image', transformed_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif choice == 'B' or choice == 'b':
        transformed_image = apply_square_root_transform(image)
        cv2.imshow('Transformed Image', transformed_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif choice == 'C' or choice == 'c':
        transformed_image = apply_exponential_transform(image)
        cv2.imshow('Transformed Image', transformed_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif choice == 'D' or choice == 'd':
        transformed_image = apply_square_transform(image)
        cv2.imshow('Transformed Image', transformed_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif choice == 'S' or choice == 's':
        break
    else:
        print("Opção inválida. Escolha novamente.")
