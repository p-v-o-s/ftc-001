#!/bin/sh

dir="/home/dwblair/gitwork"

watch -n120 "$dir/opk-soil-moisture-adafruit/pull-all -p /dev/ttyUSB1 | $dir/opk-phant-json/push"


