import os
import Catchnumber_def as hiden

black_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
              23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42,
              43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62,
              63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 79, 80, 81, 82,
              83]
white_list = [6, 7, 8, 9, 10, 11, 12, 13, 73]

for fname in os.listdir(hiden.db):  # os.listdir() 用於返回指定文件夾的文件或文件夾的名字的方法列表。
    with open(os.path.join(hiden.db, fname), 'r') as f:  # os.path.join() 連接兩個或更多的路徑名組件
        if fname == 'classes.txt':
            continue
        if hiden.isBlocked(f, black_list):
            continue
        print(os.path.join(hiden.db, fname))
