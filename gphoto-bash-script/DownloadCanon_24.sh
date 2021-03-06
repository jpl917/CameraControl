#!/bin/bash


#gphoto2 -L -f /store_00020001/DCIM/100CANON | grep '.JPG' #| sed 's/^.*#1//g'

count=0

dirname="/home/huawei/Desktop/FaceData/"$(date '+%Y-%m-%d-%H-%M-%S')
#dirname="/media/huawei/Backup Plus/"$(date '+%Y-%m-%d-%H-%M-%S')
mkdir $dirname
cd $dirname

for portname in $(gphoto2 --auto-detect | grep "usb" | sed 's/^.*usb://g');do
{
	#echo "---------------------------------------------------------" 
	echo "Camera Id:" $count
	#echo 'Port: '$portname
	subdirname=$dirname"/camera_"$count
	echo $subdirname
	mkdir $subdirname
	cd $subdirname

	gphoto2 -f /store_00020001/DCIM/100CANON -P --port "usb:$portname" 

	
	#if(($count<10));then
	#{
	#	gphoto2 -f /store_00020001/DCIM/100CANON -P --port "usb:$portname" --force-overwrite --filename "0000000$count."%C -D
	#}
	#else
	#{
	#	gphoto2 -f /store_00020001/DCIM/100CANON -P --port "usb:$portname" --force-overwrite --filename "000000$count."%C -D
	#}
	#fi

	let "count=$count+1"
		
}
done


if [ $count != 24 ]; then
	echo 'Error: Only ' $count ' Images Captured.'
fi


for((i=0;i<$count;i++))
do
cd $dirname"/camera_"$i

flag_jpg=$(ls *.JPG 2> /dev/null | wc -l);
if [ "$flag_jpg" != "0" ];then

FILES_IMG=$(ls *.JPG)
cur_img=0

for file in $FILES_IMG
do
if [ ! -d "$dirname/IMG_$cur_img" ];then
mkdir $dirname"/IMG_"$cur_img
fi
if(($i<10))
then
mv $file $dirname"/IMG_"$cur_img"/0000000"$i".JPG"
else
mv $file $dirname"/IMG_"$cur_img"/000000"$i".JPG"
fi
((cur_img++))
done

fi

flag_cr=$(ls *.CR2 2> /dev/null | wc -l);
if [ "$flag_cr" != "0" ];then
FILES_RAW=$(ls *.CR2)
cur_img=0
for file in $FILES_RAW
do
if [ ! -d "$dirname/RAW_$cur_img" ];then
mkdir $dirname"/RAW_"$cur_img
fi
if(($i<10));then
mv $file $dirname"/RAW_"$cur_img"/0000000"$i".CR2"
else
mv $file $dirname"/RAW_"$cur_img"/000000"$i".CR2"
fi
((cur_img++))
done
fi

flag_dv=$(ls *.MP4 2> /dev/null | wc -l);
if [ "$flag_dv" != "0" ];then
FILES_DV=$(ls *.MP4)
cur_img=0
for file in $FILES_DV
do
if [ ! -d "$dirname/VIDEO_$cur_img" ];then
mkdir $dirname"/VIDEO_"$cur_img
fi
if(($i<10));then
mv $file $dirname"/VIDEO_"$cur_img"/0000000"$i".MP4"
else
mv $file $dirname"/VIDEO_"$cur_img"/000000"$i".MP4"
fi
((cur_img++))
done
fi


done

for((i=0;i<$count;i++))
do
rm -r $dirname"/camera_"$i
done

echo 'Download Done'

sudo chmod -R 777 $dirname


