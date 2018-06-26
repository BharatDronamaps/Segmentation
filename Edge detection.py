import cv2
from matplotlib import pyplot as plt

frame = cv2.imread("Elevation_export.tif")
edges = cv2.Canny(frame,200,255)
plt.imshow(edges)
plt.title('Edge detected image')
plt.show()
cv2.waitKey(0)
cv2.imwrite('Python_Edges.tif',edges)
