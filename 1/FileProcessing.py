import os

def processFile():
    with open('input.txt', 'r',-1,"utf-8") as listing:
        for line in listing.readlines():
            print(line)

processFile()