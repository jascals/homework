#coding:utf-8
import PIL.Image as Image  
import os
import sys

def compressMultImage(dirPath):  
	fileList = os.listdir(dirPath)
	for f in fileList:
	    if os.path.isfile(f):     
	        sImg=Image.open(f)  
	        w,h=sImg.size  
	        dImg=sImg.resize((w/2,h/2),Image.ANTIALIAS)
	        dImg.save(f)
	        print("succeed"+f)
if __name__=='__main__':  
    compressMultImage(sys.argv[1])
