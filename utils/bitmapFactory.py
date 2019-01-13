#coding:utf-8
import PIL.Image as Image  
import os
import sys

def compressImage(fromPath,toPath):  
    if os.path.isfile(fromPath):     
        sImg=Image.open(fromPath)  
        w,h=sImg.size  
        print(w)
        print(h)
        dImg=sImg.resize((int(w/2),int(h/2)),Image.ANTIALIAS)
        dImg.save(toPath)
        print("succeed")
if __name__=='__main__':  
    compressImage(sys.argv[1], sys.argv[2])
