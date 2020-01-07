#!/bin/bash

count=0
autoexposuremode_count=0
focusmode_count=0

for portname in $(gphoto2 --auto-detect | grep "usb" | sed 's/^.*usb://g');do
{
	#echo "---------------------------------------------------------" 
	echo "Camera Id:" $count
	#echo 'Port: '$portname
	let "count=$count+1"	

	## manual mode
	autoexposuremode_value=$(gphoto2 --port "usb:$portname" --get-config autoexposuremode | grep 'Current' | sed 's/^Current: *//g')

	if [ $autoexposuremode_value = "Manual" ]; then
		let "autoexposuremode_count=$autoexposuremode_count+1"
	fi

	## manual focus
	focusmode_value=$(gphoto2 --port "usb:$portname" --get-config focusmode | grep 'Current' | sed 's/^Current: *//g')

	if [ $focusmode_value = "Manual" ]; then
		let "focusmode_count=$focusmode_count+1"
	fi

	
}
done

echo "" 
echo "-------------------Check Results---------------------------" 

if [ $autoexposuremode_count != 24 ]; then
	echo 'Error: Only ' $autoexposuremode_count ' Camera Set Manual Mode.'
fi

if [ $focusmode_count != 24 ]; then
	echo 'Error: Only ' $focusmode_count ' Camera Set Manual Focus.'
fi

echo "-----------------------------------------------------------" 
echo "" 

