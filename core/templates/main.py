import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile("implementacoes\images\Lenasalp.pgm"))
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("implementacoes\images\Lenasalp.pgm", img)
