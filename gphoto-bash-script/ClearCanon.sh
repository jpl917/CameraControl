#!/bin/bash
count=0


for portname in $(gphoto2 --auto-detect | grep "usb" | sed 's/^.*usb://g');do
{
	#echo "---------------------------------------------------------" 
	echo "Camera Id:" $count
	#echo 'Port: '$portname

	gphoto2 --port "usb:$portname" -f /store_00020001/DCIM/100CANON  -D

	
	let "count=$count+1"
	
}
done

echo 'Clear Done'

