import os

def isExsisted(txt, white_list):
    
    
    for line in txt:
        if int(line.split(' ')[0]) in white_list:
            return True
    return False
    
