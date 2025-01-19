import cv2
import numpy as np
from convolution import convolution 
from anti_aliasing import anti_aliasing
from kernels import gaussian, v_edges, h_edges

img = cv2.imread(r"D:\github\Computer_vision\4.jpg")

width = 626  # Desired width
height = int(img.shape[0] * (width / img.shape[1]))  # Maintain aspect ratio

resized_img = cv2.resize(img, (width, height))


anti_al = anti_aliasing(img, iters=5)
imgg = anti_al.anti_alias()

cv2.imshow("me", imgg)
cv2.waitKey(0)
cv2.destroyAllWindows()