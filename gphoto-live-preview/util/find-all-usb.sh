#!/bin/bash

while read uu r
do
	allusb="$allusb $uu"
done <<EOFFFF
`gphoto2 --list-ports | grep usb`
EOFFFF

for usb in $allusb
do
	echo $usb
done
