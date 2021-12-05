import os

def processFile():
    position = 0
    previousDepth = 0
    currentDepth = 0
    increases = 0

    with open('input.txt', 'r',-1,"utf-8") as listing:
        for line in listing.readlines():
            position += 1
            previousDepth = currentDepth
            currentDepth = int(line)

            if position == 1:
                continue

            if currentDepth > previousDepth:
                increases += 1

        print("# Increases is " + str(increases))



processFile()