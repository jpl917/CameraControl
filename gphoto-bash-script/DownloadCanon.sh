#!/bin/bash


#gphoto2 -L -f /store_00020001/DCIM/100CANON | grep '.JPG' #| sed 's/^.*#1//g'

count=0

dirname="/home/jpl/Desktop/FaceData/"$(date '+%Y-%m-%d-%H-%M-%S')
mkdir $dirname
cd $dirname

for portname in $(gphoto2 --auto-detect | grep "usb" | sed 's/^.*usb://g');do
{
	echo "---------------------------------------------------------" 
	echo "Camera Id:" $count
	echo 'Port: '$portname
	
	if(($count<10));then
	{
		gphoto2 -f /store_00020001/DCIM/100CANON -P --port "usb:$portname" --force-overwrite --filename "0000000$count."%C -D
	}
	else
	{
		gphoto2 -f /store_00020001/DCIM/100CANON -P --port "usb:$portname" --force-overwrite --filename "000000$count."%C -D
	}
	fi
	

	let "count=$count+1"
	
}
done

echo 'Download Done'
