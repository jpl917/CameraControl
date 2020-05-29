#!/bin/bash

#------------------------------------------------------
# 安装依赖
#sudo apt install gphoto2
#sudo apt install libsdl2-dev
#sudo apt install libsdl2-image-dev
#
# 编译可视化程序
#cd program
#make
#cd ..
#------------------------------------------------------

#------------------------------------------------------
# 执行preview
#------------------------------------------------------
while read usb wintitle winx winy 
do
	#echo $usb $winx $winy
	gphoto2 --port=$usb --capture-movie --stdout | gphoto-live-preview/program/build/liveview $wintitle $winx $winy &
done <<HereDocumentHaha
usb:003,007 Camra-0 300 50
usb:003,008 Camra-1 500 50
usb:003,008 Camra-2 700 50
usb:003,008 Camra-3 900 50
HereDocumentHaha
#------------------------------------------------------
#上面here document 中内容为运行参数，每行的具体含义为
#   相机usb端口  preview窗口标题  位置x 位置y
#
#------------------------------------------------------
'''
sleep 1
cat <<heredoc
注意事项：
	1. 确保camera不忙（没有mount在系统中）
	2. 运行./util/find-all-usb.sh 获得并确认每一个相机的usb端口信息
	3. 手动填入正确的usb端口
	4. 
heredoc
'''

#------------------------------------------------------
#等待退出
#------------------------------------------------------
#read -p "按任意键结束预览" ans

#------------------------------------------------------
#kill所有liveview进程
#------------------------------------------------------
'''
ps -A | grep liveview | 
	while read proc rest 
	do
		kill -9 $proc 
	done

echo "预览结束"
'''

