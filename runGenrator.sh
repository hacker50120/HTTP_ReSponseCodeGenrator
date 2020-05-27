#!/bin/bash
 
gedit file.txt 
echo "Paste your Http/Https Urls Here and Save It. [Press Enter to Continue..!]"
#for wating 300 seconds for Press any key 
read -t 300 -n 1
while true
do
blank=`tail -1 file.txt`
if [ -z "$blank"  ]
then
exit;
else
python3 genrator.py
fi
done

