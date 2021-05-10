#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import os
import sys
import time
import matplotlib.pyplot as plt
from threading import Thread

import Tkinter as tk
from tkinter import ttk
from tkFileDialog import askopenfilename

import serial
import easygui

if not os.path.exists("../FaceData"):
	os.makedirs("../FaceData")


window = tk.Tk()
window.title('Cameras Console')
window.geometry('230x500+50+30')
window.resizable(0, 0)      
var = tk.StringVar()  

# buttons
focusParamButton = tk.Button(window, text='Geometry参数(1/100, 8, 200, RAW)', width=25, height=2)
focusParamButton.grid(row = 0, column = 0) 
captureParamButton = tk.Button(window,text='Material参数 (1/100, 16, 100, RAW)', width=25, height=2)
captureParamButton.grid(row = 1, column = 0)
previewButton = tk.Button(window, text='预览', width=25, height=2)
previewButton.grid(row = 2, column = 0) 
endPreviewButton = tk.Button(window,text='关闭预览', width=25, height=2)
endPreviewButton.grid(row = 3, column = 0)
captureButton = tk.Button(window,text='拍摄Material', width=25, height=2)
captureButton.grid(row = 4, column = 0)  
captureButton_burst = tk.Button(window,text='拍摄Geometry', width=25, height=2)
captureButton_burst.grid(row = 5, column = 0)
captureButton_uniform = tk.Button(window,text='拍摄Uniform', width=25, height=2)
captureButton_uniform.grid(row = 6, column = 0)
captureButton_video = tk.Button(window,text='拍摄Video', width=25, height=2)
captureButton_video.grid(row = 7, column = 0)
clearButton = tk.Button(window,text='清空相机', width=25, height=2)
clearButton.grid(row = 8, column = 0)
downloadButton = tk.Button(window,text='下载图片', width=25, height=2)
downloadButton.grid(row = 9, column = 0) 
exitButton = tk.Button(window,text='退出', width=25, height=2)
exitButton.grid(row = 10, column = 0) 

#comboxlist=ttk.Combobox(window)  
#comboxlist["values"]=("1","2","3","4")  
#comboxlist.current(0)    
#comboxlist.bind("<<ComboboxSelected>>",go)  
#comboxlist.grid(row = 9, column = 0)  

#previewButton.configure(state='disabled')
#endPreviewButton.configure(state='disabled')
#captureButton.configure(state='disabled')

def clearCamera():
	a=os.system('gphoto-bash-script/ClearCanon.sh')
	var.set("Clear Done.")

def DownloadCamera():
	a=os.system('gphoto-bash-script/DownloadCanon_24.sh')
	var.set("Download Done.")

def FocusCamera():
	a=os.system('gphoto-bash-script/FocusCanon.sh')
	var.set("Params:(1/10, 16, 100, RAW)")
	focusParamButton.configure(fg='red')
	captureParamButton.configure(fg='black')
	#previewButton.configure(state='active')

def SetCanon():
	a=os.system('gphoto-bash-script/SetCanon_basic.sh')
	var.set("Params:(1/100, 16, 100, RAW)")
	captureParamButton.configure(fg='red')
	focusParamButton.configure(fg='black')
	#previewButton.configure(state='disabled')
	#endPreviewButton.configure(state='disabled')
	

def PreviewThread():
	t1 = Thread(target=Preview)
	t1.start()

def Preview():
	a=os.system('gphoto-bash-script/preview.sh')
	var.set("preview")
	
	#previewButton.configure(state='disabled')
	#endPreviewButton.configure(state='active')

def EndPreview():
	a=os.system('gphoto-bash-script/preview_quit.sh')
	var.set("end preview")

	#previewButton.configure(state='active')
	#endPreviewButton.configure(state='disabled')

def capture_uniform():
	ser = serial.Serial('/dev/ttyACM0', 115200)
	if ser.isOpen() == False:
	    ser.open()
	#print "port: ",ser.name, " isOpen:", ser.isOpen()
	ser.write("0") #.decode('hex')

	#captureButton.configure(state='active')
	#time.sleep(5)

def capture_video():
	ser = serial.Serial('/dev/ttyACM0',115200)
	if ser.isOpen() == False:
		ser.open()
	ser.write("104") #video()

def capture_burst():
	ser = serial.Serial('/dev/ttyACM0',115200)
	if ser.isOpen() == False:
		ser.open()
	ser.write("3") #video()

def capture():
	ser = serial.Serial('/dev/ttyACM0', 115200)
	if ser.isOpen() == False:
	    ser.open()
	print "serial port: ",ser.name, " isOpen:", ser.isOpen()
	ser.write("2")   #01 - 6lights sequence    

def exit():
	EndPreview()
	sys.exit(0)
    

focusParamButton.configure(command=FocusCamera)
previewButton.configure(command=PreviewThread)
endPreviewButton.configure(command=EndPreview)
captureParamButton.configure(command=SetCanon)
clearButton.configure(command=clearCamera)
captureButton_uniform.configure(command=capture_uniform)
captureButton.configure(command=capture)
captureButton_burst.configure(command=capture_burst)
captureButton_video.configure(command=capture_video)
downloadButton.configure(command=DownloadCamera)
exitButton.configure(command=exit)    


displayLabel = tk.Label(window, textvariable=var, fg='blue', width=25, height=2)
displayLabel.grid(row = 11, column = 0)

window.mainloop()
