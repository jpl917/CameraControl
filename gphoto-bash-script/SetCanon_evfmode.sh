#!/bin/bash

count=0

for portname in $(gphoto2 --auto-detect | grep "usb" | sed 's/^.*usb://g');do
{
	#echo "---------------------------------------------------------" 
	echo "Camera Id:" $count
	#echo 'Port: '$portname

	gphoto2 --port "usb:$portname" --set-config-index  evfmode=1           
	#Choice: 0 1
	#Choice: 1 0


	let "count=$count+1"
}
done

echo 'Set Done'

