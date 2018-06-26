import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import data, io, filters, morphology, img_as_ubyte

img = cv2.imread(r'Elevation_export.tif' ,0)

# Apply the binary threshold. 
ret,thresh1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)

titles = ['Original Image','Binary']
images = [img, thresh1]

for i in xrange(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

##img = morphology.binary_erosion(thresh1,morphology.diamond(1))
##img = img_as_ubyte(img)
##cv2.imshow('Eroded Image', img)
##cv2.waitKey(0)
