#抓取資料夾裡面的所有檔案路徑

import os

path = "C:\\Users\\alana\\Desktop\\Aigo\\P4_1200_1"

dirs = os.listdir(path)
print(dirs)
# for file in dirs:
#     file_path = os.path.join(path, file)
#     print(file_path)
