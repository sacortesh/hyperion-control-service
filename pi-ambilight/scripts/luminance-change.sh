#!/bin/bash
luminance=$1

if [[-n "$luminance"]]; then
	hyperion-remote -m luminance
	echo "Color changed..."
else
	echo "Argument error..."
fi