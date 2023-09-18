import cv2 as cv
import numpy as np


def high_boost(src):  # a - 1 * original + passa alta
    A = 2
    if (A >= 1):
        W = (9 * A) - 1
        kernel = np.array([[-1, -1, -1], [-1, W, -1], [-1, -1, -1]])
        ddepth = -1
        dst = cv.filter2D(src, ddepth, kernel)
    cv.imshow("Filtro HighBoost", dst)
    cv.waitKey()



def m3(src):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    ddepth = -1
    dst = cv.filter2D(src, ddepth, kernel)
    cv.imshow("Filtro M3", dst)
    cv.waitKey()



def m2(src):
    kernel = np.array([[1, -2, 1], [-2, 5, -2], [1, -2, 1]])
    ddepth = -1
    dst = cv.filter2D(src, ddepth, kernel)
    cv.imshow("Filtro M2", dst)
    cv.waitKey()


def m1(src):
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    ddepth = -1
    dst = cv.filter2D(src, ddepth, kernel)
    cv.imshow("Filtro M1", dst)
    cv.waitKey()


def h2(src):
    kernel = (np.array([[-1, -1, -1], [-1, 8, -1],
               [-1, -1, -1]]))
    ddepth = -1
    dst = cv.filter2D(src, ddepth, kernel)
    cv.imshow("Filtro H2", dst)
    cv.waitKey()

def h1(src):
    kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    ddepth = -1
    dst = cv.filter2D(src, ddepth, kernel)
    cv.imshow("Filtro H1", dst)
    cv.waitKey()
img = cv.imread(cv.samples.findFile(
    "implementacoes\images\lena.pgm"), cv.IMREAD_UNCHANGED)
h1(img)
h2(img)
m1(img)
m2(img)
m3(img)
high_boost(img)
