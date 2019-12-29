#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import os
import sys
import time
import matplotlib.pyplot as plt
from threading import Thread

import Tkinter as tk
from tkFileDialog import askopenfilename

import serial
import easygui


window = tk.Tk()
window.title('Cameras Console')
window.geometry('230x450+50+30')
window.resizable(0, 0)      
var = tk.StringVar()  

# buttons
focusParamButton = tk.Button(window, text='对焦参数(1/60, 5.6, 6400, IMG)', width=25, height=2)
focusParamButton.grid(row = 0, column = 0) 
previewButton = tk.Button(window, text='预览', width=25, height=2)
previewButton.grid(row = 1, column = 0) 
endPreviewButton = tk.Button(window,text='关闭预览', width=25, height=2)
endPreviewButton.grid(row = 2, column = 0)
captureParamButton = tk.Button(window,text='拍摄参数 (1/100, 16, 100, RAW)', width=25, height=2)
captureParamButton.grid(row = 3, column = 0) 
clearButton = tk.Button(window,text='清空相机', width=25, height=2)
clearButton.grid(row = 4, column = 0) 
activateFlashButton = tk.Button(window,text='闪光灯激活', width=25, height=2)
activateFlashButton.grid(row = 5, column = 0)  
captureButton = tk.Button(window,text='拍摄', width=25, height=2)
captureButton.grid(row = 6, column = 0)  
downloadButton = tk.Button(window,text='下载图片', width=25, height=2)
downloadButton.grid(row = 7, column = 0) 
exitButton = tk.Button(window,text='退出', width=25, height=2)
exitButton.grid(row = 8, column = 0) 


previewButton.configure(state='disabled')
endPreviewButton.configure(state='disabled')
#captureButton.configure(state='disabled')

def clearCamera():
	a=os.system('sh/ClearCanon.sh')
	var.set("Clear Done.")

def DownloadCamera():
	a=os.system('sh/DownloadCanon.sh')
	var.set("Download Done.")

def FocusCamera():
	a=os.system('sh/FocusCanon.sh')
	var.set("Params:(1/60, 5.6, 6400, IMG)")
	focusParamButton.configure(fg='red')
	captureParamButton.configure(fg='black')
	previewButton.configure(state='active')

def SetCanon():
	a=os.system('sh/SetCanon.sh')
	var.set("Params:(1/100, 16, 100, RAW)")
	captureParamButton.configure(fg='red')
	focusParamButton.configure(fg='black')
	previewButton.configure(state='disabled')
	endPreviewButton.configure(state='disabled')
	

def PreviewThread():
	t1 = Thread(target=Preview)
	t1.start()

def Preview():
	a=os.system('gphoto-live-preview/preview24.sh')
	var.set("preview")
	
	previewButton.configure(state='disabled')
	endPreviewButton.configure(state='active')

def EndPreview():
	a=os.system('gphoto-live-preview/quit.sh')
	var.set("end preview")

	previewButton.configure(state='active')
	endPreviewButton.configure(state='disabled')

def activateLight():
	ser = serial.Serial('/dev/ttyUSB0', 4800)
	if ser.isOpen() == False:
	    ser.open()
	#print "port: ",ser.name, " isOpen:", ser.isOpen()
	ser.write("00".decode('hex'))

	#captureButton.configure(state='active')
	#time.sleep(5)

def capture():
	ser = serial.Serial('/dev/ttyUSB0', 4800)
	if ser.isOpen() == False:
	    ser.open()
	print "serial port: ",ser.name, " isOpen:", ser.isOpen()
	ser.write("04".decode('hex') )   #01 - 6lights sequence    

def exit():
	EndPreview()
	sys.exit(0)
    

focusParamButton.configure(command=FocusCamera)
previewButton.configure(command=PreviewThread)
endPreviewButton.configure(command=EndPreview)
captureParamButton.configure(command=SetCanon)
clearButton.configure(command=clearCamera)
activateFlashButton.configure(command=activateLight)
captureButton.configure(command=capture)
downloadButton.configure(command=DownloadCamera)
exitButton.configure(command=exit)    


displayLabel = tk.Label(window, textvariable=var, fg='blue', width=25, height=2)
displayLabel.grid(row = 10, column = 0)

window.mainloop()
