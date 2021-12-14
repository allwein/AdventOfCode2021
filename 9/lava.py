import os
from types import LambdaType

lavaMap = []

def processFile():
    with open('input.txt', 'r',-1,"utf-8") as listing:
        for line in listing.readlines():
            lavaLine = []
            for character in line:
                if character != '\n':
                   lavaLine.append(int(character))

            lavaMap.append(lavaLine)

        lowPoints = []
        for rowIndex in range(len(lavaMap)):
            for columnIndex in range(len(lavaMap[rowIndex])):
                if isLowPoint(rowIndex,columnIndex):
                    lowPoints.append(lavaMap[rowIndex][columnIndex])

        result = sum(lowPoints, len(lowPoints))
        print("Lowpoint count: " + str(len(lowPoints)))
        print("Result is " + str(result))

def isLowPoint(rowIndex,columnIndex):
    left = columnIndex - 1
    right = columnIndex + 1
    up = rowIndex - 1
    down = rowIndex + 1

    row = lavaMap[rowIndex]
    current = lavaMap[rowIndex][columnIndex]

    if left >= 0:
        if current >= row[left]:
            return False

    if right < len(row):
        if current >= row[right]:
            return False

    if up >= 0:
        if current >= lavaMap[up][columnIndex]:
            return False

    if down < len(lavaMap):
        if current >= lavaMap[down][columnIndex]:
            return False
   
    return True

processFile()