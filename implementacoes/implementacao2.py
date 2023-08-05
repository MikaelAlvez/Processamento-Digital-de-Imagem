import cv2
import numpy as np

# -----TRANSLAÇÃO-----
def perform_translation(image):
    dragging = False
    deslocamento = np.float32([[1, 0, 0], [0, 1, 0]])
    start_x, start_y = 0, 0

    def onMouse(event, x, y, flags, param):
        nonlocal dragging, start_x, start_y, deslocamento
        if event == cv2.EVENT_LBUTTONDOWN:
            dragging = True
            start_x, start_y = x, y
        elif event == cv2.EVENT_MOUSEMOVE and dragging:
            dx = x - start_x
            dy = y - start_y
            deslocamento = np.float32([[1, 0, dx], [0, 1, dy]])
            deslocado = cv2.warpAffine(image, deslocamento, (largura, altura))
            cv2.imshow("Operacao", deslocado)
        elif event == cv2.EVENT_LBUTTONUP:
            dragging = False

    altura, largura = image.shape[:2]
    cv2.imshow("Operacao", image)
    cv2.setMouseCallback("Operacao", onMouse)

    while True:
        key = cv2.waitKey(1)

        if key == 27:  # Tecla ESC para sair
            break
        elif key == 13:  # Tecla Enter para prosseguir
            break

    cv2.destroyAllWindows()
    return cv2.warpAffine(image, deslocamento, (largura, altura))

# -----ROTAÇÃO-----
def perform_rotation(image):
    dragging = False
    start_x, start_y = 0, 0
    angle = 0

    def onMouse(event, x, y, flags, param):
        nonlocal dragging, start_x, start_y, angle
        if event == cv2.EVENT_LBUTTONDOWN:
            dragging = True
            start_x, start_y = x, y
        elif event == cv2.EVENT_MOUSEMOVE and dragging:
            dx = x - start_x
            dy = y - start_y
            angle = np.arctan2(dy, dx) * 180 / np.pi
            rotated = rotate_image(image, angle)
            cv2.imshow("Operacao", rotated)
        elif event == cv2.EVENT_LBUTTONUP:
            dragging = False

    def rotate_image(image, angle):
        centro = (0, 0)
        rotacao = cv2.getRotationMatrix2D(centro, angle, 1.0)
        rotacionado = cv2.warpAffine(image, rotacao, (image.shape[1], image.shape[0]), flags=cv2.INTER_LINEAR)
        return rotacionado

    cv2.imshow("Operacao", image)
    cv2.setMouseCallback("Operacao", onMouse)

    while True:
        key = cv2.waitKey(1)

        if key == 27:
            break
        elif key == 13:
            break

    cv2.destroyAllWindows()
    return rotate_image(image, angle)

# -----ESCALA-----
def perform_scaling(image):
    scale_factor = 1.0

    def onMouse(event, x, y, flags, param):
        nonlocal scale_factor
        if event == cv2.EVENT_MOUSEWHEEL:
            if flags > 0:
                scale_factor *= 1.1
            else:
                scale_factor /= 1.1
            scaled = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)
            cv2.imshow("Operacao", scaled)

    cv2.imshow("Operacao", image)
    cv2.setMouseCallback("Operacao", onMouse)

    while True:
        key = cv2.waitKey(1)

        if key == 27:
            break
        elif key == 13:
            break

    cv2.destroyAllWindows()
    return cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)


# -----REFLEXÃO-----
def perform_reflection(image):
    reflection_type = input("Escolha o tipo de reflexão (horizontal/vertical): ").lower()

    def perform_reflection_type(reflection_type):
        if reflection_type == 'horizontal':
            reflected = cv2.flip(image, 1)
        elif reflection_type == 'vertical':
            reflected = cv2.flip(image, 0)
        else:
            return None
        return reflected

    reflected = perform_reflection_type(reflection_type)

    if reflected is not None:
        cv2.imshow(f"Reflexao {reflection_type.capitalize()}", reflected)
        cv2.waitKey(0)
    else:
        print("Tipo de reflexão inválido.")

    cv2.destroyAllWindows()
    return reflected

# -----CISALHAMENTO-----
def perform_shear(image):
    dragging = False
    start_x, start_y = 0, 0
    dx, dy = 0, 0

    def onMouse(event, x, y, flags, param):
        nonlocal dragging, start_x, start_y, dx, dy
        if event == cv2.EVENT_LBUTTONDOWN:
            dragging = True
            start_x, start_y = x, y
        elif event == cv2.EVENT_MOUSEMOVE and dragging:
            dx = x - start_x
            dy = y - start_y
            cisalhamento = np.float32([[1, dx / image.shape[0], 0], [dy / image.shape[1], 1, 0]])
            cisalhado = cv2.warpAffine(image, cisalhamento, (image.shape[1], image.shape[0]))
            cv2.imshow("Operacao", cisalhado)
        elif event == cv2.EVENT_LBUTTONUP:
            dragging = False

    cv2.imshow("Operacao", image)
    cv2.setMouseCallback("Operacao", onMouse)

    while True:
        key = cv2.waitKey(1)

        if key == 27:
            break
        elif key == 13:
            break

    cv2.destroyAllWindows()
    return cv2.warpAffine(image, np.float32([[1, dx / image.shape[0], 0], [dy / image.shape[1], 1, 0]]), (image.shape[1], image.shape[0]))

# Carregar a imagem
imagem = cv2.imread("implementacoes/images/lena.pgm")

while True:
    print("Escolha uma operação:")
    print("1. Translação")
    print("2. Rotação")
    print("3. Escala")
    print("4. Reflexão")
    print("5. Cisalhamento")
    print("0. Sair")

    choice = input("Opção: ")

    if choice == '1':
        imagem = perform_translation(imagem.copy())
    elif choice == '2':
        imagem = perform_rotation(imagem.copy())
    elif choice == '3':
        imagem = perform_scaling(imagem.copy())
    elif choice == '4':
        imagem = perform_reflection(imagem.copy())
    elif choice == '5':
        imagem = perform_shear(imagem.copy())
    elif choice == '0':
        break
    else:
        print("Opção inválida!")

cv2.destroyAllWindows()
