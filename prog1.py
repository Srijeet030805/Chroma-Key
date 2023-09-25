import cv2 as cv
import statistics
import sys
#import matplotlib.pyplot as plt


img = cv.imread("maxresdefault3.jpg",1)
bg = cv.imread("bg2.jpg",1)
buffer=img.copy()

if img is None:
 sys.exit("Could not read the image.")


x=len(img)
y=len(img[0])

b= [img[i][j][0] for i in range(x) for j in range(y)]
g= [img[i][j][1] for i in range(x) for j in range(y)]
r= [img[i][j][2] for i in range(x) for j in range(y)]

#plt.hist(b,20,color="blue")
#plt.hist(g,20,color="green")
#plt.hist(r,20,color="red")
#plt.show()

mr=statistics.mode(r)
mg=statistics.mode(g)
mb=statistics.mode(b)

def inNbd(c,r,p):
    return abs(p-c)<r

for i in range(x):
    for j in range(y):
        if inNbd(mb,50,img[i][j][0]) and inNbd(mg,50,img[i][j][1]) and inNbd(mr,50,img[i][j][2]) :
            buffer[i][j]=bg[i][j]

cv.imshow("Original", img)
#cv.imshow("Background", bg)
cv.imshow("Chroma Key", buffer)
k = cv.waitKey(0)

#if k == ord("s"):
#cv.imwrite("starry_night.png", img)
cv.destroyAllWindows()
