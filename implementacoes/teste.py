import cv2 as cv
import numpy as np
from PIL import Image

bgr = cv.imread('implementacoes/images/lena_cor.jpg')
# Make float and divide by 255 to give BGRdash
bgrdash = bgr.astype(np.float64)/255

# Calculate K as (1 - whatever is biggest out of Rdash, Gdash, Bdash)
K = 1 - np.max(bgrdash, axis=2)

# Calculate C
C = (1-bgrdash[..., 2] - K)/(1-K)

# Calculate M
M = (1-bgrdash[..., 1] - K)/(1-K)

# Calculate Y
Y = (1-bgrdash[..., 0] - K)/(1-K)

# Combine 4 channels into single image and re-scale back up to uint8
CMYK = (np.dstack((C, M, Y, K)) * 255).astype(np.uint8)
cv.imshow("aa", bgr)
cv.imshow('bb', CMYK)
cv.imwrite('cmyk.jpg', CMYK)
cv.waitKey(0)
