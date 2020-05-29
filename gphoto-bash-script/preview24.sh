#!/bin/bash

#------------------------------------------------------
# 安装依赖
#sudo apt install gphoto2
#sudo apt install libsdl2-dev
#sudo apt install libsdl2-image-dev
#
# 编译可视化程序
#cd program
#mkdir build && cd build
#cmake ..
#make -j4
#------------------------------------------------------

#------------------------------------------------------
# 执行preview
#------------------------------------------------------
winx=0
winy=0
count=0
wintitle_prefix="Camera"
for portname in $(gphoto2 --auto-detect | grep "usb" | sed 's/^.*usb://g');do
{
        let "winx=100+count%6*300"
 	let "winy=count/6*230"
        wintitle=$wintitle_prefix$count
	gphoto2 --port "usb:$portname" --capture-movie --stdout | gphoto-live-preview/program/build/liveview $wintitle $winx $winy &


	let "count=$count+1"
	
}
done
