import numpy as np
import cv2

def region_growth(image, seed):
    height, width, channels = image.shape
    visited = np.zeros((height, width), dtype=np.uint8)
    segmented = np.copy(image)

    # Defina um limite de intensidade para crescer a região
    region_threshold = 70

    # Defina uma pilha para armazenar as coordenadas dos pixels a serem verificados
    stack = []
    stack.append(seed)

    # Obtém a intensidade do pixel de semente
    seed_intensity = image[seed[0], seed[1]]

    while len(stack) > 0:
        current_pixel = stack.pop()
        y, x = current_pixel

        # Verifique se o pixel já foi visitado
        if visited[y, x] == 1:
            continue

        # Verifique se a intensidade do pixel atual é semelhante à intensidade da semente
        if np.abs(np.linalg.norm(image[y, x] - seed_intensity)) <= 60:
        # if np.linalg.norm(image[y, x] - seed_intensity) < region_threshold:
            segmented[y, x] = [255, 170, 0]  # Pseudocolorir o pixel em azul na imagem segmentada
            visited[y, x] = 1  # Marcar o pixel como visitado

            # Adicione pixels vizinhos à pilha para verificação
            if x > 0:
                stack.append((y, x - 1))
            if x < width - 1:
                stack.append((y, x + 1))
            if y > 0:
                stack.append((y - 1, x))
            if y < height - 1:
                stack.append((y + 1, x))

    return segmented

# image = cv2.imread('implementacoes\images\exemplo.jpg')
image = cv2.imread('implementacoes\images\Captura de tela 2023-09-04 123953.png')
# Crie uma janela de visualização da imagem
cv2.namedWindow('Imagem Original')
cv2.imshow('Imagem Original', image)

# Aguarde o usuário escolher o valor da semente com um clique do mouse
print("Clique na imagem para escolher a semente...")
seed_point = (-1, -1)

def on_mouse_click(event, x, y, flags, param):
    global seed_point

    if event == cv2.EVENT_LBUTTONDOWN:
        seed_point = (y, x)

cv2.setMouseCallback('Imagem Original', on_mouse_click)

while seed_point == (-1, -1):
    cv2.waitKey(1)

# Aplique o algoritmo de crescimento de região
segmented_image = region_growth(image, seed_point)

# Exibir a imagem segmentada com a região em azul
cv2.imshow('Imagem Segmentada', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
