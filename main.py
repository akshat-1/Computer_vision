import cv2
import numpy as np
from convolution import convolution 
from kernels import gaussian, bilateral, v_edges, h_edges

img = cv2.imread(r"D:\github\Computer_vision\2.png")

width = 626  # Desired width
height = int(img.shape[0] * (width / img.shape[1]))  # Maintain aspect ratio

resized_img = cv2.resize(img, (width, height))


convolve = convolution(resized_img, h_edges)
imgg = convolve.convolve()

cv2.imshow("me", imgg)
cv2.waitKey(0)
cv2.destroyAllWindows()