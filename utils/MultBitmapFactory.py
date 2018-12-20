#coding:utf-8
import PIL.Image as Image  
import os
import sys

def compressMutiImage(dirPath):  
	rename(dirPath)
	fileList = os.listdir(dirPath)
	for f in fileList:
		if(".png" in f):
		    if os.path.isfile(f):     
		        sImg=Image.open(f)  
		        w,h=sImg.size  
		        dImg=sImg.resize((w/2,h/2),Image.ANTIALIAS)
		        dImg.save(f)
		        print("succeed"+f)
		    else:
		    	print(f+" is not file")
	    
def rename(dirPath):
	fileList = os.listdir(dirPath)
	for i, f in enumerate(fileList):
		print(f)
		if(".png" in f):
			os.rename(f, str(i)+".png")

if __name__=='__main__':  
    compressMutiImage(sys.argv[1])
