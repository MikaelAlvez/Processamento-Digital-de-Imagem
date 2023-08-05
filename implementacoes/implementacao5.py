import cv2

class ImageLinearTransformation:
    def __init__(self, img):
        self.img = img

    def transform(self, Fmin, Fmax, Gmin, Gmax):
        transformed_img = cv2.convertScaleAbs(self.img, alpha=(Gmax - Gmin) / (Fmax - Fmin), beta=Gmin - Fmin)
        return transformed_img

    def inverse_transform(self, Fmin, Fmax, Gmin, Gmax):
        inv_transformed_img = cv2.convertScaleAbs(self.img, alpha=(Fmax - Fmin) / (Gmax - Gmin), beta=Fmin - Gmin)
        return inv_transformed_img

    def binary_operation(self, other_img, operation):
        if operation == '1':
            result_img = cv2.add(self.img, other_img)
        elif operation == '2':
            result_img = cv2.subtract(self.img, other_img)
        elif operation == '3':
            result_img = cv2.multiply(self.img, other_img)
        elif operation == '4':
            result_img = cv2.divide(self.img, other_img)
        else:
            raise ValueError("Operação binária não suportada")
        
        return result_img

def main():
    while True:
        print("Escolha uma operação:")
        print("1. Transformação linear para novo intervalo")
        print("2. Escolhe-se da quantidade de partes e depois define o intervalo")
        print("3. Inversa")
        print("4. Binária")
        print("0. Sair")
        
        choice = input("Opção: ")
        
        if choice == '0':
            break
        
        img_path = input("Informe o caminho da imagem: ")
        original_img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
        
        if original_img is None:
            print("Não foi possível carregar a imagem.")
            continue
        
        image_transformation = ImageLinearTransformation(original_img)
        
        if choice == '1':
            Fmin = float(input("Informe o valor mínimo do intervalo inicial: "))
            Fmax = float(input("Informe o valor máximo do intervalo inicial: "))
            Gmin = float(input("Informe o valor mínimo do novo intervalo: "))
            Gmax = float(input("Informe o valor máximo do novo intervalo: "))
            transformed_img = image_transformation.transform(Fmin, Fmax, Gmin, Gmax)
            cv2.imshow("Transformed Image", transformed_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
        elif choice == '2':
            parts = int(input("Informe a quantidade de partes: "))
            Gmin = float(input("Informe o valor mínimo do novo intervalo: "))
            Gmax = float(input("Informe o valor máximo do novo intervalo: "))
            
            Fmin = min(image_transformation.img.flatten())
            Fmax = max(image_transformation.img.flatten())
            
            transformed_img = image_transformation.transform(Fmin, Fmax, Gmin, Gmax)
            cv2.imshow("Transformed Image", transformed_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif choice == '3':
            Fmin = float(input("Informe o valor mínimo do intervalo original: "))
            Fmax = float(input("Informe o valor máximo do intervalo original: "))
            Gmin = float(input("Informe o valor mínimo do intervalo da imagem inversa: "))
            Gmax = float(input("Informe o valor máximo do intervalo da imagem inversa: "))
            inv_transformed_img = image_transformation.inverse_transform(Fmin, Fmax, Gmin, Gmax)
            cv2.imshow("Inverse Transformed Image", inv_transformed_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
        elif choice == '4':
            other_img_path = input("Informe o caminho da outra imagem para a operação binária: ")
            other_img = cv2.imread(other_img_path, cv2.IMREAD_UNCHANGED)
            
            if other_img is None:
                print("Não foi possível carregar a outra imagem.")
                continue
            
            operation = input("Informe a operação:\n 1. Adição\n 2. Subtração\n 3. Multiplicação\n 4. Divisão\n Opção: ").strip().lower()
            result_img = image_transformation.binary_operation(other_img, operation)
            cv2.imshow("Binary Operation Result", result_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
        else:
            print("Escolha inválida")

if __name__ == "__main__":
    main()