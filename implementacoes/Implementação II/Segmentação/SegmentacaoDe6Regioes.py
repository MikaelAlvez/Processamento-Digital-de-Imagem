import numpy as np
import cv2

def region_growing(image, seed, region_id):
    height, width, channels = image.shape
    visited = np.zeros((height, width), dtype=np.uint8)
    segmented = np.copy(image)

    # Defina um limite de intensidade para crescer a região
    region_threshold = 200

    # Defina uma pilha para armazenar as coordenadas dos pixels a serem verificados
    stack = []
    stack.append(seed)

    # Defina cores diferentes para cada região
    colors = [
        [255, 0, 0],   # Red
        [0, 255, 0],   # Green
        [0, 0, 255],   # Blue
        [255, 255, 0], # Yellow
        [255, 0, 255], # Magenta
        [0, 255, 255]  # Cyan
    ]

    # Obtém a intensidade do pixel de semente
    seed_intensity = image[seed[0], seed[1]]

    while len(stack) > 0:
        current_pixel = stack.pop()
        y, x = current_pixel

        # Verifique se o pixel já foi visitado
        if visited[y, x] == 1:
            continue

        # Verifique se a intensidade do pixel atual é semelhante à intensidade da semente
        if np.linalg.norm(image[y, x] - seed_intensity) < region_threshold:
            segmented[y, x] = colors[region_id % len(colors)]  # Atribuir uma cor à região
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

# Carregue uma imagem colorida
image = cv2.imread('implementacoes\images\lena.pgm')

# Crie uma janela de visualização da imagem original
cv2.namedWindow('Imagem Original')
cv2.imshow('Imagem Original', image)

# Aguarde o usuário escolher as sementes com cliques do mouse
print("Clique em 6 pontos diferentes na imagem para escolher as sementes...")

# Armazene as coordenadas das sementes em uma lista
seeds = []

def on_mouse_click(event, x, y, flags, param):
    global seeds

    if event == cv2.EVENT_LBUTTONDOWN:
        seeds.append((y, x))

cv2.setMouseCallback('Imagem Original', on_mouse_click)

while len(seeds) < 6:
    cv2.waitKey(1)

# Aplique o algoritmo de crescimento de região para cada semente e atribua uma cor diferente
segmented_image = image.copy()
for i, seed in enumerate(seeds):
    segmented_image = region_growing(segmented_image, seed, i)

# Exibir a imagem segmentada com as regiões em cores diferentes
cv2.imshow('Imagem Segmentada', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
