# import os
# imgfolder_path = 'C:\\Users\\alana\\Project\\IMG (原始)\\0605視2_0600-0630' #存放IMG資料夾路径
# txtfolder_path = "C:\\Users\\alana\\Project\\LABEL (原始 不准動)\\0605視2_0600-0630_標註" #存放TXT資料夾路徑

# classes_data = []
# imgfile_list=os.listdir(imgfolder_path)

# for file in file_list:
#     #print(item)                       #P4-2021-09-24-12-00.mp4_002910.400.txt
#     #print(item.split('.')[3])         #txt
#     if file.split('.')[1] != "classes.txt":
#         for line in open(folder_path+"/"+item,'r').readlines():  #讀取每一筆資料
#             for i in range(len(classes_data)):  #len(classes_data) = 88 
#                 if line.split(' ')[0] == str(i):
#                     classes_data[i][1] += 1
# print(classes_data)