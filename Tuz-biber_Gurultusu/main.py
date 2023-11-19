import numpy
import cv2

def saltPepperNoise(image):
    row,col,ch = image.shape
    s_vs_p = 0.5
    amount = 0.04
    noisy = numpy.copy(image)
    num_salt = int(numpy.ceil(amount*image.size*s_vs_p))
    corrds = [numpy.random.randint(0,i-1,num_salt) for i in image.shape]
    noisy[corrds] = 1
    num_pep = int(numpy.ceil(amount*image.size*s_vs_p))
    corrds = [numpy.random.randint(0,i-1,num_pep) for i in image.shape]
    noisy[corrds] = 0
    return noisy
img = cv2.imread("manzara.jpg");
cv2.imshow("Original",img)

J = saltPepperNoise(img)
cv2.imshow("SaltPepper Noise",J)


cv2.waitKey(0)