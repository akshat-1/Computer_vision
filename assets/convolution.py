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
        self.pad_height = 0
        self.pad_width = 0
        
        self.__channels()
       
        if self.is_padding:
            self.pad_height = self.kernel.shape[0] // 2
            self.pad_width = self.kernel.shape[1] // 2
        
        

        
        if self.is_padding:
            self.blue = np.pad(self.blue, ((self.pad_height, self.pad_height), (self.pad_width, self.pad_width)), mode='constant', constant_values=0)
            self.green = np.pad(self.green, ((self.pad_height, self.pad_height), (self.pad_width, self.pad_width)), mode='constant', constant_values=0)
            self.red = np.pad(self.red, ((self.pad_height, self.pad_height), (self.pad_width, self.pad_width)), mode='constant', constant_values=0)


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
                pixel = [np.uint8(np.clip(np.real(blue[i][j]), 0, 255)), np.uint8(np.clip(np.real(green[i][j]), 0, 255)), np.uint8(np.clip(np.real(red[i][j]), 0, 255))]
                row.append(pixel)
            imgr.append(row)
        return np.array(imgr)

    def convolve(self):
        
       
        result_b = np.copy(self.blue)
        result_g = np.copy(self.green)
        result_r = np.copy(self.red)

        
        for i in range(self.pad_height, self.blue.shape[0] - self.pad_height):
            for j in range(self.pad_width, self.blue.shape[1] - self.pad_width):
                ans_b = 0
                ans_g = 0
                ans_r = 0
                for k in range(self.kernel.shape[0]):
                    for l in range(self.kernel.shape[1]):
                        ans_b += self.kernel[k][l] * self.blue[i - self.pad_height + k][j - self.pad_width + l]
                        ans_g += self.kernel[k][l] * self.green[i - self.pad_height + k][j - self.pad_width + l]
                        ans_r += self.kernel[k][l] * self.red[i - self.pad_height + k][j - self.pad_width + l]

                result_b[i][j] = ans_b
                result_g[i][j] = ans_g
                result_r[i][j] = ans_r
        
        return self.__combine(result_b[self.pad_height:-self.pad_height, self.pad_width:-self.pad_width], 
                              result_g[self.pad_height:-self.pad_height, self.pad_width:-self.pad_width], 
                              result_r[self.pad_height:-self.pad_height, self.pad_width:-self.pad_width])
    
    # def fast_convolve(self):
    #     f_blue = np.fft.fftshift(np.fft.fft2(self.blue))
    #     f_red = np.fft.fftshift(np.fft.fft2(self.red))
    #     f_green = np.fft.fftshift(np.fft.fft2(self.green))
    #     f_kernel = np.fft.fftshift(np.fft.fft2(self.kernel))

    #     kernel_padded = np.zeros_like(f_blue)  
    #     kh, kw = f_kernel.shape
    #     center_h, center_w = f_blue.shape[0] // 2, f_blue.shape[1] // 2  

    #     kernel_padded[center_h - kh // 2:center_h + kh // 2 + kh % 2,
    #                 center_w - kw // 2:center_w + kw // 2 + kw % 2] = f_kernel


    #     b_c_k = np.fft.ifft2(np.fft.ifftshift(f_blue * kernel_padded))
    #     g_c_k = np.fft.ifft2(np.fft.ifftshift(f_green * kernel_padded))
    #     r_c_k = np.fft.ifft2(np.fft.ifftshift(f_red * kernel_padded))

    #     return self.__combine(b_c_k[self.pad_height:-self.pad_height, self.pad_width:-self.pad_width], 
    #                           g_c_k[self.pad_height:-self.pad_height, self.pad_width:-self.pad_width], 
    #                           r_c_k[self.pad_height:-self.pad_height, self.pad_width:-self.pad_width])
        




        









        


        