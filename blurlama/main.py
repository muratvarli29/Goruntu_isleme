import cv2
import numpy
image=cv2.imread("gunbatimi.jpg")

kernel1=numpy.ones((5,5),numpy.float32)/25
img=cv2.filter2D(src=image,ddepth=-1,kernel=kernel1)
cv2.imshow("orijinal image",image)
cv2.imshow("Kernel blur",img )
cv2.waitKey()
cv2.destroyAllWindows()