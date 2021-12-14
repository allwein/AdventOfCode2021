import os
from types import LambdaType

octoMap = []
flashes = 0
tempFlashes = 0
octopi = 0

def processFile():
    global tempFlashes
    global octopi
    with open('input.txt', 'r',-1,"utf-8") as listing:
        for line in listing.readlines():
            octoLine = []
            for number in line:
                if number != '\n':
                   octoLine.append(int(number))
                   octopi = octopi + 1

            octoMap.append(octoLine)

        for step in range(10000):
            tempFlashes = 0
            IncreaseEnergy()
            ProcessFlashes()
            print(str(tempFlashes) + " out of " + str(octopi))
            if tempFlashes == octopi:
                print("Synchronized at step: " + str(step+1))
                break

        print("Result is " + str(flashes))

def IncreaseEnergy():
    for rowIndex in range(len(octoMap)):
        for columnIndex in range(len(octoMap[rowIndex])):
            octoMap[rowIndex][columnIndex] = octoMap[rowIndex][columnIndex] + 1

def ProcessFlashes():
    global flashes
    global tempFlashes
    while True:
        HadFlashes = False
        for rowIndex in range(len(octoMap)):
            for columnIndex in range(len(octoMap[rowIndex])):
                if octoMap[rowIndex][columnIndex] > 9:
                    flash(rowIndex,columnIndex)
                    flashes = flashes + 1
                    tempFlashes = tempFlashes + 1
                    HadFlashes = True

        if not HadFlashes:
            break

def flashIncrement(rowIndex, columnIndex):
    if rowIndex < 0:
        return
    if columnIndex < 0:
        return
    if rowIndex > len(octoMap) - 1:
        return
    if columnIndex > len(octoMap[rowIndex]) - 1:
        return

    if octoMap[rowIndex][columnIndex] > 0:
        octoMap[rowIndex][columnIndex] = octoMap[rowIndex][columnIndex] + 1
    

def flash(rowIndex,columnIndex):
    octoMap[rowIndex][columnIndex] = 0
    flashIncrement(rowIndex-1, columnIndex-1)
    flashIncrement(rowIndex-1, columnIndex)
    flashIncrement(rowIndex-1, columnIndex+1)
    flashIncrement(rowIndex, columnIndex-1)
    flashIncrement(rowIndex, columnIndex+1)
    flashIncrement(rowIndex+1, columnIndex)
    flashIncrement(rowIndex+1, columnIndex-1)
    flashIncrement(rowIndex+1, columnIndex+1)

processFile()