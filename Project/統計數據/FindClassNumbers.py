#統計該資料夾裡的txt檔標籤的Numbers總數

import os
from re import X
import matplotlib.pyplot as plt

folder_path = 'C:\\Users\\alana\\Desktop\\實驗室\\資料擴增實驗\\原始數據集 + 1,3 新增雜訊\\要新增的\\labels(1跟3)' #存放Labels路径
classes_file = "F:\\魚類標記\\relabelclasses EN.txt" #存放类别文件路径
#E:\\魚類標記\\classes.txt
#E:\\魚類標記\\relabelclasses.txt
classes_data = []
file_list=os.listdir(folder_path)

#生成 [['0_Chromis_fumea', 0], ['1_Pomacentrus_coelestis', 0]......,['87_Mugil_cephalus', 0]]
for classes in open(classes_file,'r',encoding="utf-8").readlines():
    dr = [classes.replace("\n", ""), 0]        
    classes_data.append(dr)  #
    

for item in file_list:
    #print(item)                       #P4-2021-09-24-12-00.mp4_002910.400.txt
    #print(item.split('.')[3])         #txt
    if item.split('.')[1] == "txt" and item != "classes.txt":
        for line in open(folder_path+"/"+item,'r').readlines():  #讀取每一筆資料
            for i in range(len(classes_data)):  #len(classes_data) = 88 
                if line.split(' ')[0] == str(i):
                    classes_data[i][1] += 1
print(classes_data)



fig = plt.figure()
fig.canvas.set_window_title('data statistics')
plt.rcParams["font.sans-serif"]=['SimHei']
plt.title("data statistics")
plt.xlabel("class")
plt.ylabel("number")
for i in range(len(classes_data)):
    plt.bar(classes_data[i][0], classes_data[i][1])
plt.show()

#replace()方法语法：str.replace(old, new[, max])
# old -- 将被替换的子字符串。
# new -- 新字符串，用于替换old子字符串。
# max -- 可选字符串, 替换不超过 max 次

#append() 方法用于在列表末尾添加新的对象(dr)