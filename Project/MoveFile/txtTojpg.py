from importlib.resources import path
import os
pt = "C:\\Users\\alana\\Desktop\\AIGO\\aigo_choose\\save.txt"


def txtTojpg(file , label_map):
    txt = None
    with open(file, 'r') as f:
        txt = f.read().split('.')[-1:]    #['txt\n']
        print(txt)

    for i in range(len(txt)):
        try:
            txt=label_map[txt]
        except:
            cls_id=int(cls_id)
        txt[i]=f'{cls_id} {s}'
    
    with open(file, 'w') as f:
        for s in txt:
            f.write(s+'\n')

class_map={'txt','jpg'}

txtTojpg(pt ,class_map)          #讓每個file檔都依照class_map 設定的變數改變