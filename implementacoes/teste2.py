from PIL import Image
img = Image.open('/home/caio/repos/pdi/Processamento-Digital-de-Imagem/implementacoes/images/lena_cor.jpg').convert('CMYK')
img.show()