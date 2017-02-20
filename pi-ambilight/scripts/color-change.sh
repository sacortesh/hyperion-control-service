#!/bin/bash
color=$1

if [[-n "$color"]]; then
	hyperion-remote -c color
	echo "Color changed..."
else
	echo "Argument error..."
fi