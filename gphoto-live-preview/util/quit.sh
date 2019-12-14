#!/bin/bash

ps -A | grep liveview | 
	while read psn rest 
	do
		kill -9 $psn 
	done

