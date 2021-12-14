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
        basins = []
        for rowIndex in range(len(lavaMap)):
            for columnIndex in range(len(lavaMap[rowIndex])):
                if isLowPoint(rowIndex,columnIndex):
                    lowPoints.append(lavaMap[rowIndex][columnIndex])
                    print("Checking Row: " + str(rowIndex) + " Column: " + str(columnIndex))
                    basinSize = findBasinSize(rowIndex, columnIndex)
                    print(basinSize)
                    basins.append(basinSize)

        basins.sort()
        basin1 = basins[len(basins)-1]
        basin2 = basins[len(basins)-2]
        basin3 = basins[len(basins)-3]

        result = basin1 * basin2 * basin3
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

points = []

def findBasinSize(rowIndex, columnIndex):
    if rowIndex < 0 or columnIndex < 0:
        return 0
    if rowIndex >= len(lavaMap) or columnIndex >= len(lavaMap[rowIndex]):
        return 0
    if lavaMap[rowIndex][columnIndex] == 9:
        return 0

    point = str(rowIndex) + ',' + str(columnIndex)
    if point in points:
        return 0

    left = columnIndex - 1
    right = columnIndex + 1
    up = rowIndex - 1
    down = rowIndex + 1
    current = lavaMap[rowIndex][columnIndex]
    
    points.append(point)
    #print("\tReturning 1 for Row: " + str(rowIndex) + " Column: " + str(columnIndex) + " Value: " + str(current))
    return 1 + findBasinSize(rowIndex, left) + findBasinSize(rowIndex, right) + findBasinSize(up, columnIndex) + findBasinSize(down, columnIndex)       

processFile()