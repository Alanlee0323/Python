import os

db='C:\\Users\\alana\\Desktop\\Aigo\\P4_1200_1'

def isBlocked(f, black_list):
    txt=f.read().split('\n')[:-1]   #切出檔案f內的
    # split()通過指定分隔符對字符串進行切片，如果參數num 有指定值，則僅分隔num 個子字符串
    # list[:-1]：返回从0到-1的数据，故返回第一个到倒数第二个的数据（不包含结束索引位置-1）
    
    for line in txt:
        if int(line.split(' ')[0]) in black_list:  #split(' ')[0] 以空格為切割基準 返還第0個切出來的字串 若標記的數字在黑名單內
            return True
    return False


def isExsisted(f, white_list):
    txt=f.read().split('\n')[:-1]
    
    for line in txt:
        if int(line.split(' ')[0]) in white_list:
            return True
    return False
