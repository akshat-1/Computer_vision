import cv2
import numpy as np
from assets.convolution import convolution 
from assets.anti_aliasing import anti_aliasing
from assets.kernels import gaussian, v_edges, h_edges, grad_gaussian
from assets.edge_detection import edge_detection

img = cv2.imread(r"D:\github\Computer_vision\assets\4.jpg")

width = 626  # Desired width
height = int(img.shape[0] * (width / img.shape[1]))  # Maintain aspect ratio

resized_img = cv2.resize(img, (width, height))


imgg = edge_detection(resized_img).get_grads()


cv2.imshow("me", imgg)
cv2.waitKey(0)
cv2.destroyAllWindows()