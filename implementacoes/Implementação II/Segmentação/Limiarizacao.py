import cv2
import numpy as np

def threshold_global(image):
    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    return binary_image

def threshold_local(image, option):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    if option == 'I':
        binary_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    elif option == 'II':
        binary_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    elif option == 'III':
        _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    elif option == 'IV':
        n = int(input("Informe o valor de n: "))
        k = float(input("Informe o valor de k: "))
        binary_image = niblack_threshold(gray_image, n, k)
    else:
        return None
    return binary_image

def niblack_threshold(image, n, k):
    binary_image = np.zeros_like(image)
    
    for y in range(n // 2, image.shape[0] - n // 2):
        for x in range(n // 2, image.shape[1] - n // 2):
            window = image[y - n // 2:y + n // 2 + 1, x - n // 2:x + n // 2 + 1]
            mean = np.mean(window)
            std = np.std(window)
            threshold = mean + k * std
            if image[y, x] > threshold:
                binary_image[y, x] = 255
    
    return binary_image

def main():
    image_path = 'implementacoes\images\exemplo.jpg'
    image = cv2.imread(image_path)
    
    while True:
        print("\nA. Limiarização Global")
        print("B. Limiarização Local:")
        print("S. Sair")
        
        option = input("Selecione uma opção: ").lower()  # Converter entrada para minúsculas
        
        if option == 's':
            break
        elif option == 'a':
            binary_image = threshold_global(image)
        elif option == 'b':
            print("\nI. Média")
            print("II. Máximo")
            print("III. Mínimo")
            print("IV. Niblack")

            local_option = input("Selecione uma opção: ")  # Converter entrada para minúsculas

            if local_option in ['I', 'II', 'III', 'IV']:
                binary_image = threshold_local(image, local_option)
            else:
                print("Opção inválida.")
                continue
        else:
            print("Opção inválida.")
            continue
        
        # Mostrar a imagem resultante
        cv2.imshow('Limiarizacao', binary_image)
        key = cv2.waitKey(0)
        
        # Verificar se a tecla pressionada foi "Esc" (27)
        if key == 27:
            continue
        
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
