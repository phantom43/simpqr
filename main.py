import qrcode
import numpy as np
import cv2
import os
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
class credit: 
	author = '''
	author : Muh Rezky Ananda
	version: 1.0.0
	relase : 10/10/2021
	git    : https://github.com/phantom43


	'''
print(bcolors.UNDERLINE + credit.author 
	+ bcolors.ENDC)
QR = input("input teks/link> ")
img = qrcode.make(QR)
type(img)  
img.save("result.png")
print(bcolors.WARNING + "QR telah tersimpan...!!!" 
      + bcolors.ENDC)
print(bcolors.HEADER + "ingin scan sekarang...?" 
      + bcolors.ENDC)
p = input('y/n? ')
if p == "ya":
 os.system("sleep 5")
 print("silahkan ctrl+ z untuk exit program")
 img = cv2.imread("result.png")
 cv2.imshow('image',img)
 cv2.waitKey(0)
 exit()
if p == "n":
	os.system("clear")
	os.system('python3 main.py')
	
