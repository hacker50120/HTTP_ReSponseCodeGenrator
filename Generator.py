#!/usr/bin/env python3
import urllib3
urllib3.disable_warnings()
import requests
from colorama import Fore, Back, Style
print(Style.RESET_ALL)

# define an empty list
list = []

# open file and read the content in a list
with open('file.txt', 'r') as filehandle:
    var = 0
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]
        var += 1
        # add item to the list
        list.append(currentPlace)
while (var > 0):
    print("URL", "Status_code", sep="------------>")
    while (1):
        try:

            for i in list:
                # resp = requests.post(i, headers=headers, timeout=10)
                resp = requests.get(i, timeout=(6, 30), verify=False)
                print(i, resp.status_code, sep="------------>")
                with open("file.txt", "r") as f:
                    lines = f.readlines()
                    lines.remove(i + "\n")
                    with open("file.txt", "w") as new_f:
                        for line in lines:
                            new_f.write(line)



        except:
            print("error Occure, It may Be some reason Please Retry again...!!")
            with open("file.txt", "r") as f:
                lines = f.readlines()
                lines.remove(list[0] + "\n")
                with open("file.txt", "w") as new_f:
                    for line in lines:             new_f.write(line)

