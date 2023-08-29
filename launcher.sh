#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/automatic_cat_feeder
sudo python src/automatic_cat_feeder/main.py
cd /
