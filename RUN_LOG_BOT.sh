#!/bin/sh
cd screenshot
wait $!
python screenshot.py
wait $!
cd ../
pwd
cd bot_detection/CROP_LOG/
pwd
python run.py