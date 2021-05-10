#!/bin/bash

count=0

for portname in $(gphoto2 --auto-detect | grep "usb" | sed 's/^.*usb://g');do
{
	#echo "---------------------------------------------------------" 
	echo "Camera Id:" $count
	#echo 'Port: '$portname

	gphoto2 --port "usb:$portname"                  \
	--set-config          shutterspeed="1/60"      \
	--set-config          aperture=8	        \
	--set-config          iso=100                   \
	--set-config-index    imageformat=7             \


	
	
	let "count=$count+1"
}
done

echo 'Preset Done'

