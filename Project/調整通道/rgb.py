#去除紅色通道

import cv2
import numpy
import matplotlib.pyplot as plt
import os



def RGBtransform(img):
    img = img.copy()
    img[:, :, 2] = 0  # G=0
    return img

def img_processing(img):
    result_img = RGBtransform(img)
    return result_img

def read_path(file_pathname):
    #讀取資料夾下所有圖片
    for filename in os.listdir(file_pathname):
        print(file_pathname+'\\'+filename)
        origin_img = cv2.imread(file_pathname+'\\'+filename)
        result_img = img_processing(origin_img)
        
        cv2.imwrite('C:\\Users\\alana\\Desktop\\RGB\\result'+"/"+filename,result_img)

read_path("C:\\Users\\alana\\Desktop\\RGB") #路徑不能有中文!

# #示範代碼
# # 1.20 图像拆分通道 (Numpy切片)
# img1 = cv2.imread("C:\\Users\\alana\\Desktop\\RGB\\05010401.jpg", flags=1)
# # [:, :, 0] 藍
# # [:, :, 1] 綠
# # [:, :, 2] 紅

# #去除 R 通道
# bImg = img1.copy()  # 获取 BGR
# bImg[:, :, 2] = 0  # G=0
  
# # 获取 G 通道
# gImg = img1.copy()  # 获取 BGR

    
# plt.subplot(211), plt.title("1. ORG channel"), plt.axis('off')
# gImg = cv2.cvtColor(gImg, cv2.COLOR_BGR2RGB)
# plt.imshow(gImg)  # matplotlib 顯示原始圖像

# plt.subplot(212), plt.title("2. Without R channel"), plt.axis('off')
# bImg = cv2.cvtColor(bImg, cv2.COLOR_BGR2RGB)  # 图片格式转换：BGR(OpenCV) -> RGB(PyQt5)
# plt.imshow(bImg)  # matplotlib 顯示去除紅色圖像


# plt.show()
