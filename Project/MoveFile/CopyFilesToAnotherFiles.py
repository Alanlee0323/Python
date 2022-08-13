#若舊資料夾裡文件內容的標籤編號在白名單內 則複製該文件到新資料夾

import shutil
import os
import numpy as np
import CopyFilesToAnotherFiles_def as df

db='C:\\Users\\alana\\Desktop\\Aigo\\P4_1200_labelled' #舊資料夾
dst_db='C:\\Users\\alana\\Desktop\\Aigo\\P4_1200_1_copy' #新資料夾
white_list=[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,54,55,77,65,70,73,78]
classes = np.zeros(88)
for fname in os.listdir(db):
    with open(os.path.join(db, fname), 'r') as f:
        
        if fname=='classes.txt': continue
        txt=f.read().split('\n')[:-1]
        
        if df.isExsisted(txt, white_list): #若編號在白名單內
            arr = [int(s.split(' ')[0]) for s in txt]
            classes[arr]+=1
            src=os.path.join(db, fname)
            dst=os.path.join(dst_db, fname)
            shutil.copyfile(src, dst) #複製檔案到指定資料夾

print(np.argwhere(classes>0))