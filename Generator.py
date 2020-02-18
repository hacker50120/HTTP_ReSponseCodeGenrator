#!/usr/bin/env python3

import requests

# define an empty list
list = []

# open file and read the content in a list
with open('file.txt', 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]

        # add item to the list
        list.append(currentPlace)

print("URL", "Status_code",sep="------------>")
try: 

	for i in list:
	 resp = requests.get(i,timeout=10)
	 print(i ,resp.status_code, sep="------------>")
	 resp.raise_for_status()                 # Raise error in case of failure 
except requests.exceptions.HTTPError as httpErr: 
    print ("Http Error:",httpErr) 
except requests.exceptions.ConnectionError as connErr: 
    print ("Error Connecting:",connErr) 
except requests.exceptions.Timeout as timeOutErr: 
    print ("Timeout Error:",timeOutErr) 
except requests.exceptions.RequestException as reqErr: 
    print ("Something Else:",reqErr) 
