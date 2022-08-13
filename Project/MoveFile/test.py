import os
dst_db='C:\\Users\\alana\\Desktop\\Aigo\\P4_1200_1'

for fname in os.listdir(dst_db):
    file=os.path.join(dst_db, fname)  #將所有txt檔路徑存至file變數

class_map={'78':1,
           '3':2
          }         #字典
txt=None
with open(file, 'r') as f:
    txt=f.read().split('\n')[:-1]  #txt = ['2 0.551595 0.461182 0.030273 0.042480']
    
for i in range(len(txt)): #len(txt)=1 
    cls_id, s=txt[i].split(' ', 1)  #cls_id = 切割出的第一個值(number)  s = 切割出的第二個值(coordinate)
    try:
        cls_id=class_map[cls_id]  
    except:
         cls_id=int(cls_id)
    txt[i]='{cls_id} {s}'   # txt[i] = 2 0.551595 0.461182 0.030273 0.042480

    with open(file, 'w') as f:  #存檔
        for s in txt:
            f.write(s+'\n')



