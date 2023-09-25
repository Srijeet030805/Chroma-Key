import cv2 as cv
import Chroma
import sys

data = cv.imread("maxresdefault3.jpg",1)
bg = cv.imread("bg2.jpg",1)

if data is None:
 sys.exit("Could not read the image.")

img= Chroma.Image(data)
processed= img.chromaKey(bg)

cv.imshow("Chroma Key", buffer)
k = cv.waitKey(0)
cv.destroyAllWindows()
