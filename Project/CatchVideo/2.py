import os
import cv2


video_dir='D:\\2022_NMMST_2TB\\20220508\\Chang_Tang_Li'
video_file='2022-05-08-0600-0800_chang.mp4'
cap = cv2.VideoCapture(os.path.join(video_dir, video_file)) # 讀取電腦中的影片
if not cap.isOpened():
    print("Cannot open camera")
    exit()
    
#2048, 3072