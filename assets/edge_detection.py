import numpy as np
from assets.convolution import convolution
from assets.kernels import *

class edge_detection:
    def __init__(self, image):
        self.img = image
    
    def __gradients(self):
        self.img = convolution(self.img, gaussian, cvt_gray=True).convolve()
        y_grad = convolution(self.img,v_edges, cvt_gray=True).convolve()
        x_grad = convolution(self.img,h_edges, cvt_gray=True).convolve()

        norm_grad = np.copy(x_grad)
        for i in range(x_grad.shape[0]):
            for j in range(x_grad.shape[1]):
                norm_grad[i][j] = np.uint8(np.sqrt(int(x_grad[i][j])**2 + int(y_grad[i][j])**2))
        
        return norm_grad
    
    # def __non_max_suppression(self):
    #     k

    def get_grads(self):
        return self.__gradients()
    

