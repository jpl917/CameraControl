#!/bin/bash

cd $1
namelist=$(ls)
for name in $namelist
do
	echo $name
	splitvar=(${name//_/ })
	newname=${splitvar[0]}'.JPG'
	echo $newname
	mv $name $newname
done

cd ~
