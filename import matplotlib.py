from msvcrt import getch
from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np

def bgr2rgb(img):
    return img[:,:,::-1]

img=cv.imread("img1.jpg",-1)
newImage=np.concatenate((img,bgr2rgb(img)),2)
plt.imshow(newImage)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()