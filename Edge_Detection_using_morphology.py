from skimage import data, io, filters, morphology, img_as_ubyte

import cv2
import numpy as np
from matplotlib import pyplot as plt

#Read and display Image (Change path as per your computer)

##imag = cv2.imread('neighborhood.tiff')
##imag = cv2.imread('Elevation_export.tif')
imag = cv2.imread('Elevation_export.tif')
##plt.imshow(imag)
##plt.title('Original Image')
##plt.show()
##cv2.waitKey(0)

#COnvert to Grey, Binary

img = cv2.cvtColor(imag, cv2.COLOR_RGB2GRAY);


 
_ , img = cv2.threshold(img,100,200,cv2.THRESH_BINARY)
##plt.imshow(img)
##plt.title('Binary Image')
##plt.show()
##cv2.waitKey(0)



# Expel objects with small sizes



img = morphology.binary_erosion(img,morphology.diamond(1))
img = img_as_ubyte(img)
##plt.imshow(img)
##plt.title('Eroded Image')
##plt.show()
##cv2.waitKey(0)

img = morphology.binary_opening(img)
img = img_as_ubyte(img)
##plt.imshow(img)
##plt.title('Opened Image')
##plt.show()
##cv2.waitKey(0)

element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
img = cv2.erode(img, element, iterations =10)
img = cv2.dilate(img, element, iterations =10)


ing = morphology.remove_small_objects(img,min_size=200,connectivity=2, in_place=True)
##plt.imshow(ing)
##plt.title('Remove object')
##plt.show()
##cv2.waitKey(0)


# Canny Detection

edges = cv2.Canny(ing,10,20)

##plt.imshow(edges)
##plt.title('Edge detected image')
##plt.show()
##cv2.waitKey(0)
cv2.imwrite('Python_Edges_elevation.tif',edges)

# COntour Detection

image,contours,hierarchy = cv2.findContours(edges, 1, 2)

#cnt = contours[0]
cv2.drawContours(image, contours, -1, (0,255,0), 3)
plt.imshow(image)
plt.show()
cv2.waitKey(0)

NumeroContornos = str(len(contours))
print NumeroContornos
'''
hull = cv2.convexHull(cnt,returnPoints = False)
cv2.imshow('COntour ', hull)
cv2.waitKey(0)
''
#Line Detection using Hough Trnasform

lines = cv2.HoughLines(ing,1,np.pi/180,200)

for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

cv2.line(edges,(x1,y1),(x2,y2),(255),2)
plt.imshow(edges)
plt.title('Hough Line Detection')
plt.show()
cv2.waitKey(0)

# Finding contours and CUrves

ret,thresh = cv2.threshold(edges,127,255,100)
print thresh.dtype
image,contours,hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]
epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
plt.imshow(approx)
plt.title('Contour')
plt.show()
cv2.waitKey(0)
'''

