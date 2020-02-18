#!/usr/bin/env python3

import requests
# Python program to print 
# red text with green background 

from colorama import Fore, Back, Style 

print(Style.RESET_ALL) 


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
	 #resp = requests.post(i, headers=headers, timeout=10)
	 resp = requests.post(i,timeout=10,verify=True) 
	 print(i , Fore.BLUE, resp.status_code, sep="------------>")
	 with open("file.txt", "r") as f:
    	  lines = f.readlines() 
    	  lines.remove(i+"\n")
    	  with open("file.txt", "w") as new_f:
        	    for line in lines:             new_f.write(line)
	
except requests.exceptions.HTTPError as httpErr: 
    print ("Http Error:",httpErr) 
except requests.exceptions.ConnectionError as connErr: 
    print ("Error Connecting:",connErr) 
except requests.exceptions.Timeout as timeOutErr: 
    print ("Timeout Error:",timeOutErr) 
except requests.exceptions.RequestException as reqErr: 
    print ("Something Else:",reqErr) 
except requests.exceptions.Connecting as ConErr: 
    print ("Something Else:",ConErr) 
    
