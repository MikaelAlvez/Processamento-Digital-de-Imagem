import cv2
import numpy as np

class NonLinearTransformation:
    def log_transform(self, img, c):
        log_transformed_img = c * np.log1p(img)
        return log_transformed_img

    def sqrt_transform(self, img):
        sqrt_transformed_img = np.sqrt(img)
        return sqrt_transformed_img

    def exponential_transform(self, img, c):
        exp_transformed_img = np.exp(c * img)
        return exp_transformed_img

    def square_transform(self, img):
        square_transformed_img = np.square(img)
        return square_transformed_img

def main():
    while True:
        print("Escolha uma operação:")
        print("1. Log")
        print("2. Raíz")
        print("3. Exponencial")
        print("4. Quadrado")
        print("0. Sair")
        
        choice = input("Opção: ")
        
        if choice == '0':
            break
        
        img_path = input("Informe o caminho da imagem: ")
        original_img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
        
        if original_img is None:
            print("Não foi possível carregar a imagem.")
            continue
        
        non_linear_transformation = NonLinearTransformation()
        
        if choice == '1':
            c = float(input("Informe o valor de c para a transformação logarítmica: "))
            log_transformed_img = non_linear_transformation.log_transform(original_img, c)
            cv2.imshow("Log Transformed Image", log_transformed_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
        elif choice == '2':
            sqrt_transformed_img = non_linear_transformation.sqrt_transform(original_img)
            cv2.imshow("Square Root Transformed Image", sqrt_transformed_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
        elif choice == '3':
            c = float(input("Informe o valor de c para a transformação exponencial: "))
            exp_transformed_img = non_linear_transformation.exponential_transform(original_img, c)
            cv2.imshow("Exponential Transformed Image", exp_transformed_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
        elif choice == '4':
            square_transformed_img = non_linear_transformation.square_transform(original_img)
            cv2.imshow("Square Transformed Image", square_transformed_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
        else:
            print("Escolha inválida")

if __name__ == "__main__":
    main()
