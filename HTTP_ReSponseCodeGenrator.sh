#!/usr/bin/sh

sudo apt-get update
sudo apt-get install gedit
sudo pip uninstall requests
pip install requests==2.0
sudo apt-get install ca-certificates
sudo apt-get install ntpdate
sudo ntpdate -u ntp.ubuntu.com
pip install --upgrade certifi
touch file.txt
gedit file.txt
