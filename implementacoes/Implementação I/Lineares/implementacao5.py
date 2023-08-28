import cv2
import numpy as np

def linear_transformation(image_path):
    # Carregar a imagem em escala de cinza
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Erro ao carregar a imagem.")
    else:
        # Definir o intervalo desejado para a nova imagem (Gmin, Gmax)
        Gmin = 0
        Gmax = 50
        

        # Obter os valores mínimos e máximos da imagem original
        Fmin = np.min(image)
        Fmax = np.max(image)

        # Calcular o fator de escala (a) e o valor de ajuste de brilho (b)
        a = (Gmax - Gmin) / (Fmax - Fmin)
        b = Gmin - a * Fmin

        # Aplicar a transformação linear
        transformed_image = cv2.convertScaleAbs(image, alpha=a, beta=b)

        # Exibir a imagem original e a transformada
        cv2.imshow('Imagem Original', image)
        cv2.imshow('Imagem Transformada por Partes', transformed_image)

        # Aguardar até que uma tecla seja pressionada e depois fechar as janelas
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def piecewise_transformation(image_path):
    # Carregar a imagem em escala de cinza
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Erro ao carregar a imagem.")
    else:
        # Definir a quantidade de partes (subintervalos)
        num_parts = 4
        
        # Definir os intervalos de intensidade desejados
        interval_ranges = [(0, 50), (51, 100), (101, 150), (151, 255)]

        # Lista para armazenar as transformações para cada intervalo
        def transformations(x):
            return [2 * x, x, 0.5 * x, x]  # Exemplo de transformação

        # Criar uma imagem vazia para a saída
        output_image = np.zeros_like(image, dtype=np.uint8)

        # Aplicar a transformação por partes
        for i, (start, end) in enumerate(interval_ranges):
            mask = cv2.inRange(image, start, end)
            transformed_values = transformations(image)
            transformed_values[i] = transformed_values[i].astype(np.uint8)
            output_image = cv2.add(output_image, transformed_values[i] * mask)

        # Exibir a imagem original e a transformada por partes
        cv2.imshow('Imagem Original', image)
        cv2.imshow('Imagem Transformada por Partes', output_image)

        # Aguardar até que uma tecla seja pressionada e depois fechar as janelas
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def inverse_transformation(image_path):
    # Carregar a imagem em escala de cinza
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Erro ao carregar a imagem.")
    else:
        # Aplicar a transformação inversa (negativo)
        inverted_image = 255 - image

        # Exibir a imagem original e a transformação inversa
        cv2.imshow('Imagem Original', image)
        cv2.imshow('Imagem Transformação Inversa', inverted_image)

        # Aguardar até que uma tecla seja pressionada e depois fechar as janelas
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def binary_transformation(image_path):
    # Carregar a imagem em escala de cinza
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Erro ao carregar a imagem.")
    else:
        # Definir um valor limite para a transformação binária
        threshold = 45

        # Aplicar a transformação binária
        _, binary_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)

        # Exibir a imagem original e a transformação binária
        cv2.imshow('Imagem Original', image)
        cv2.imshow('Imagem Transformação Binária', binary_image)

        # Aguardar até que uma tecla seja pressionada e depois fechar as janelas
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def main():
    image_path = 'implementacoes\images\imageteste.jpg'  # Substitua pelo caminho correto

    while True:
        print("Escolha uma opção:")
        print("A) Transformação Linear")
        print("B) Transformação por Partes")
        print("C) Transformação Inversa")
        print("D) Transformação Binária")
        print("S) Sair")
        choice = input("Opção: ").upper()

        if choice == 'A':
            linear_transformation(image_path)
        elif choice == 'B':
            piecewise_transformation(image_path)
        elif choice == 'C':
            inverse_transformation(image_path)
        elif choice == 'D':
            binary_transformation(image_path)
        elif choice == 'S':
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()