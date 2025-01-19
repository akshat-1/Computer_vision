import numpy as np
import cv2

class convolution:
    def __init__(self, img, kernel, is_padding=True):
        self.img = img
        self.kernel = kernel
        self.is_padding = is_padding
        self.blue = None
        self.green = None
        self.red = None

    def __channels(self):
        # BGR 
        blue_channel = []
        red_channel = []
        green_channel = []

        for i in self.img:
            bl = []
            rd = []
            gn = []
            for j in i:
                bl.append(int(j[0]))
                rd.append(int(j[2]))
                gn.append(int(j[1]))

            blue_channel.append(bl)
            red_channel.append(rd)
            green_channel.append(gn)

        self.blue = np.array(blue_channel)
        self.green = np.array(green_channel)
        self.red = np.array(red_channel)

    def __combine(self, blue, green, red):
        imgr = []
        for i in range(len(blue)):
            row = []
            for j in range(len(blue[i])):
                pixel = [np.uint8(blue[i][j]), np.uint8(green[i][j]), np.uint8(red[i][j])]
                row.append(pixel)
            imgr.append(row)
        return np.array(imgr)

    def convolve(self):
        pad_height = 0
        pad_width = 0
        
       
        if self.is_padding:
            pad_height = self.kernel.shape[0] // 2
            pad_width = self.kernel.shape[1] // 2
        
        self.__channels()

        
        if self.is_padding:
            self.blue = np.pad(self.blue, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant', constant_values=0)
            self.green = np.pad(self.green, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant', constant_values=0)
            self.red = np.pad(self.red, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant', constant_values=0)

       
        result_b = np.copy(self.blue)
        result_g = np.copy(self.green)
        result_r = np.copy(self.red)

        
        for i in range(pad_height, self.blue.shape[0] - pad_height):
            for j in range(pad_width, self.blue.shape[1] - pad_width):
                ans_b = 0
                ans_g = 0
                ans_r = 0
                for k in range(self.kernel.shape[0]):
                    for l in range(self.kernel.shape[1]):
                        ans_b += self.kernel[k][l] * self.blue[i - pad_height + k][j - pad_width + l]
                        ans_g += self.kernel[k][l] * self.green[i - pad_height + k][j - pad_width + l]
                        ans_r += self.kernel[k][l] * self.red[i - pad_height + k][j - pad_width + l]

                result_b[i][j] = ans_b
                result_g[i][j] = ans_g
                result_r[i][j] = ans_r
        
        return self.__combine(result_b[pad_height:-pad_height, pad_width:-pad_width], 
                              result_g[pad_height:-pad_height, pad_width:-pad_width], 
                              result_r[pad_height:-pad_height, pad_width:-pad_width])




        









        


        