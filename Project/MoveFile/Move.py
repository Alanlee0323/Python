import os
import shutil
db='E:\\魚類標記\\AllLabelled' #預複製檔的位置
dst_db = 'E:\\魚類標記\\AllLabelledCopy'   #要放複製檔的位置
files = os.listdir(db)

arr = None  #目錄，類似之前yolo v4的train.txt那樣，裡面寫上檔案位置
with open("C:\\Users\\alana\\Desktop\\AIGO\\aigo_choose\\save.txt", 'r') as f:
    arr = f.read().split('\n')

for data in files:     #跟db資料夾的檔案做比對，有符合的就會複製一份到dst_db那裏
    if data in arr:
        src = os.path.join(db, data)
        dst=os.path.join(dst_db, data)
        shutil.copyfile(src, dst)