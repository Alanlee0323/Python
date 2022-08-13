import time



counter=0
start=time.time()
while True:
    ret, frame = cap.read()             # 讀取影片的每一幀
    if frame is None: break
#    if counter>=1000: break
    
    counter+=1
    if counter%30==0:
        code='20220508_0600-0800_chang'
        fname=f"{code}_{counter}.jpg"
        cv2.imwrite(os.path.join('E:\\Chang_Tang_Li', fname), frame)