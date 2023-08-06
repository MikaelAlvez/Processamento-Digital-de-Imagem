import cv2
import numpy as np

# ----- ZOOM IN COM INTERPOLAÇÃO -----
def perform_zoom_in_interpolation(image, x, y, scale_factor):
    altura, largura = image.shape[:2]

    nova_altura = int(altura * scale_factor)
    nova_largura = int(largura * scale_factor)

    deslocamento_x = max(0, x - nova_largura // 2)
    deslocamento_y = max(0, y - nova_altura // 2)

    zoomed_in = cv2.resize(image, (nova_largura, nova_altura), interpolation=cv2.INTER_LINEAR)
    zoomed_in = zoomed_in[deslocamento_y:deslocamento_y+altura, deslocamento_x:deslocamento_x+largura]
    return zoomed_in

# Carregar a imagem
imagem = cv2.imread("implementacoes/images/lena.pgm")

# Exibir a imagem original
cv2.imshow("Zoom In - Interpolacao", imagem)

scale_factor = 1.0
x = 0
y = 0

def onMouse(event, _x, _y, flags, param):
    global scale_factor, x, y
    if event == cv2.EVENT_MOUSEWHEEL:
        if flags > 0:
            scale_factor *= 1.1
        else:
            scale_factor /= 1.1
        x, y = _x, _y
        zoomed_image = perform_zoom_in_interpolation(imagem, x, y, scale_factor)
        cv2.imshow("Zoom In - Interpolacao", zoomed_image)

cv2.setMouseCallback("Zoom In - Interpolacao", onMouse)

while True:
    key = cv2.waitKey(1)

    if key == 27:  # Tecla ESC para sair
        break

cv2.destroyAllWindows()

# ----- ZOOM IN COM REPLICAÇÃO -----

# Exibir a imagem original
cv2.imshow("Zoom In - Replicacao", imagem)

scale_factor = 1.0

def onMouse(event, x, y, flags, param):
    global scale_factor
    if event == cv2.EVENT_MOUSEWHEEL:
        if flags > 0:
            scale_factor *= 1.1
        else:
            scale_factor /= 1.1
        scaled = cv2.resize(imagem, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)
        cv2.imshow("Zoom In - Replicacao", scaled)

cv2.setMouseCallback("Zoom In - Replicacao", onMouse)

while True:
    key = cv2.waitKey(1)

    if key == 27:  # Tecla ESC para sair
        break

    # ----- ZOOM OUT COM EXCLUSÃO -----
def perform_zoom_out_exclusion(image, x, y):
    altura, largura = image.shape[:2]

    scale_factor = 0.5
    nova_altura = int(altura * scale_factor)
    nova_largura = int(largura * scale_factor)

    deslocamento_x = max(0, x - nova_largura // 2)
    deslocamento_y = max(0, y - nova_altura // 2)

    zoomed_out = cv2.resize(image, (nova_largura, nova_altura), interpolation=cv2.INTER_LINEAR)
    result = np.zeros_like(image)
    result[deslocamento_y:deslocamento_y+nova_altura, deslocamento_x:deslocamento_x+nova_largura] = zoomed_out
    return result

# Carregar a imagem
imagem = cv2.imread("implementacoes/images/lena.pgm")

# Exibir a imagem original
cv2.imshow("Zoom Out - Exclusao", imagem)

clicks = 0
last_x = 0
last_y = 0

def onMouse(event, x, y, flags, param):
    global clicks, last_x, last_y
    if event == cv2.EVENT_MOUSEWHEEL:
        if flags < 0:
            clicks += 1
            if clicks == 1:
                last_x = x
                last_y = y
            elif clicks == 2:
                clicks = 0
                zoomed_image = perform_zoom_out_exclusion(imagem, last_x, last_y)
                cv2.imshow("Zoom Out - Exclusao", zoomed_image)

cv2.setMouseCallback("Zoom Out - Exclusao", onMouse)

while True:
    key = cv2.waitKey(1)

    if key == 27:  # Tecla ESC para sair
        break

    # ----- ZOOM OUT COM VALOR-MÉDIO -----
def perform_zoom_out_mean(image, x, y):
    altura, largura = image.shape[:2]

    scale_factor = 0.8
    nova_altura = int(altura * scale_factor)
    nova_largura = int(largura * scale_factor)

    deslocamento_x = max(0, x - nova_largura // 2)
    deslocamento_y = max(0, y - nova_altura // 2)

    zoomed_out = cv2.resize(image, (nova_largura, nova_altura), interpolation=cv2.INTER_LINEAR)
    result = image.copy()
    result[deslocamento_y:deslocamento_y+nova_altura, deslocamento_x:deslocamento_x+nova_largura] = zoomed_out

    # Calcular a média dos pixels na área de zoom out
    for i in range(deslocamento_y, deslocamento_y+nova_altura):
        for j in range(deslocamento_x, deslocamento_x+nova_largura):
            result[i, j] = np.mean(result[i, j])

    return result

# Carregar a imagem
imagem = cv2.imread("implementacoes/images/lena.pgm")

# Exibir a imagem original
cv2.imshow("Zoom Out (Valor-Médio)", imagem)

clicks = 0
last_x = 0
last_y = 0

def onMouse(event, x, y, flags, param):
    global clicks, last_x, last_y
    if event == cv2.EVENT_MOUSEWHEEL:
        if flags < 0:
            clicks += 1
            if clicks == 1:
                last_x = x
                last_y = y
            elif clicks == 2:
                clicks = 0
                zoomed_image = perform_zoom_out_mean(imagem, last_x, last_y)
                cv2.imshow("Zoom Out (Valor-Médio)", zoomed_image)

cv2.setMouseCallback("Zoom Out (Valor-Médio)", onMouse)

while True:
    key = cv2.waitKey(1)

    if key == 27:  # Tecla ESC para sair
        break

cv2.destroyAllWindows()
