#!/usr/bin/env python3
import urllib3
import sys
urllib3.disable_warnings()
import requests
from colorama import Fore, Back, Style
print(Style.RESET_ALL)

# define an empty list
list = []
var =1
# open file and read the content in a list
def reader():
    with open('file.txt', 'r') as filehandle:
        var = 0
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentPlace = line[:-1]
            var += 1
            # add item to the list
            list.append(currentPlace)

def scanner():
    for i in list:
        # resp = requests.post(i, headers=headers, timeout=10)
        resp = requests.get(i, timeout=(3.2, 30), verify=False)
        print(i, resp.status_code, sep="------------>")
        with open("file.txt", "r") as f:
            lines = f.readlines()
            lines.remove(i + "\n")
            with open("file.txt", "w") as new_f:
                for line in lines:
                    new_f.write(line)
reader()

while (var > 0):
    try:
        print("URL", "Status_code", sep="------------>")
        while (1):
            try:
                scanner()

            except:
                reader()
                print(list[0]+"<<<----error Occure, Due To Connection Time Out...!!---->")
                with open("file.txt", "r") as f:
                    lines = f.readlines()
                    lines.remove(list[0] + "\n")
                    with open("file.txt", "w") as new_f:
                        for line in lines:
                                new_f.write(line)
                        scanner()

    except:
        print("DONE!! \nPlease Enter the Url's In file.txt")
        sys.exit(0)
