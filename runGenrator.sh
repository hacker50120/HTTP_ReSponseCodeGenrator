#!/bin/bash
 
nano file.txt 
echo "Paste your Http/Https Urls Here and Save It. [Press Enter to Continue..!]"
#will wait 300 seconds only
read -t 300 -n 1
while true
do
blank=`tail -1 file.txt`
if [ -z "$blank"  ]
then
exit;
else
python3 Generator.py
fi
done

