import cv2
import os
from fileinput import filename
import numpy as np
import matplotlib.pyplot as plt
import glob
from IPython.display import clear_output

def gaussian_noise(img, mean=0, sigma=0.15):
    
    # int -> float (標準化)
    img = img / 255.0
    # 隨機生成高斯 noise (float + float)
    noise = np.random.normal(mean, sigma, img.shape)
    # noise + 原圖
    gaussian_out = img + noise
    # 所有值必須介於 0~1 之間，超過1 = 1，小於0 = 0
    gaussian_out = np.clip(gaussian_out, 0, 1)
    
    # 原圖: float -> int (0~1 -> 0~255)
    gaussian_out = np.uint8(gaussian_out*255)
    # noise: float -> int (0~1 -> 0~255)
    noise = np.uint8(noise*255)

    return gaussian_out


def img_processing(img):
    # do something here
    result_img = gaussian_noise(img)

    return result_img
    
#     return img

def read_path(file_pathname):
    #遍历该目录下的所有图片文件
    for filename in os.listdir(file_pathname):
        print(filename)
        origin_img = cv2.imread(file_pathname+'/'+filename)
        result_img = img_processing(origin_img)
        
        cv2.imwrite('C:\\Users\\alana\\Aigo\\FIsh\\images\\test'+"/"+filename,result_img)


read_path("C:\\Users\\alana\\Aigo\\FIsh\\images\\test")

