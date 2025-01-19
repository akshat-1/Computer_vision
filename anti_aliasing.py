import numpy as np
from convolution import convolution
from kernels import gaussian

class anti_aliasing:
    def __init__(self, image, iters=3):
        self.img = image
        self.iters = iters
        
    def anti_alias(self):
        image = self.img

        while(self.iters):
            convolve = convolution(image, gaussian)
            image = convolve.convolve()

            self.iters -=1
        image = image[::2, ::2]
        
        return image



