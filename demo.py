#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import os
import sys
import matplotlib.pyplot as plt
from threading import Thread

import Tkinter as tk
from tkFileDialog import askopenfilename


window = tk.Tk()
window.title('Cameras Console')
window.geometry('230x350+50+30')
window.resizable(0, 0)      
var = tk.StringVar()  

#filename=tk.StringVar()

#def Open_Img():
#    filename = askopenfilename()
#    var.set(filename.split('/')[-1])

def clearCamera():
	a=os.system('sh/ClearCanon.sh')
	var.set("Clear Done.")

def DownloadCamera():
	a=os.system('sh/DownloadCanon.sh')
	var.set("Download Done.")

def FocusCamera():
	a=os.system('sh/FocusCanon.sh')
	var.set("Params:(1/60, 5.6, 6400, IMG)")

def SetCanon():
	a=os.system('sh/SetCanon.sh')
	var.set("Params:(1/100, 16, 100, RAW)")

def PreviewThread():
	t1 = Thread(target=Preview)
	t1.start()

def Preview():
	a=os.system('gphoto-live-preview/preview24.sh')
	var.set("preview")

def EndPreview():
	a=os.system('gphoto-live-preview/quit.sh')
	var.set("end preview")

def exit():
	EndPreview()
	sys.exit(0)
    

tk.Button(window,text='Focus(1/60, 5.6, 6400, IMG)', width=25, height=2, command=FocusCamera).grid(row = 0, column = 0) 
tk.Button(window,text=' Set (1/100, 16, 100, RAW)', width=25, height=2, command=SetCanon).grid(row = 1, column = 0) 
tk.Button(window,text='Clear', width=25, height=2, command=clearCamera).grid(row = 2, column = 0) 
tk.Button(window,text='Download', width=25, height=2, command=DownloadCamera).grid(row = 3, column = 0) 
tk.Button(window,text='Preview24', width=25, height=2, command=PreviewThread).grid(row = 4, column = 0) 
tk.Button(window,text='EndPreview24', width=25, height=2, command=EndPreview).grid(row = 5, column = 0)
tk.Button(window,text='Exit', width=25, height=2, command=exit).grid(row = 6, column = 0)     
tk.Label(window, textvariable=var, fg='red', width=25, height=2).grid(row = 10, column = 0)


window.mainloop()
