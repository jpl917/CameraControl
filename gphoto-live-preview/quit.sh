#!/bin/bash

ps -A | grep liveview | 
	while read psn rest 
	do
		kill -9 $psn 
	done

echo "Preview Quit"

ps -A | grep gphoto | 
	while read psn rest 
	do
		kill -SIGINT $psn 
	done


