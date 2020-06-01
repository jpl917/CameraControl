#!/bin/bash

count=0

for portname in $(gphoto2 --auto-detect | grep "usb" | sed 's/^.*usb://g');do
{
	#echo "---------------------------------------------------------" 
	echo "Camera Id:" $count
	#echo 'Port: '$portname

	gphoto2 --port "usb:$portname" --set-config-index  drivemode=1           
	#Choice: 0 Single
	#Choice: 1 Continuous high speed
	#Choice: 2 Continuous low speed
	#Choice: 3 Timer 10 sec
	#Choice: 4 Timer 2 sec
	#Choice: 5 Unknown value 0007  

	
	let "count=$count+1"
	
	
}
done

echo 'Set Done'

