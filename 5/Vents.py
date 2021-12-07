import os

class Point:
    def __init__(self, data):
        temp = data.split(",")
        self.x = int(temp[0])
        self.y = int(temp[1])

class VentLine:
    def __init__(self, data):
        temp = data.split(" -> ")
        self.start = Point(temp[0])
        self.end = Point(temp[1])
        self.data = data

def processFile():
    ventLines = []
    vents = []

    with open('input2.txt', 'r',-1,"utf-8") as listing:
        for line in listing.readlines():
            ventLines.append(VentLine(line))

        #Find size of map
        maxX = 0
        maxY = 0

        for ventLine in ventLines:
            if ventLine.start.x > maxX:
                maxX = ventLine.start.x

            if ventLine.end.x > maxX:
                maxX = ventLine.end.x

            if ventLine.start.y > maxY:
                maxY = ventLine.start.y

            if ventLine.end.y > maxY:
                maxY = ventLine.end.y

        #Bump since points are 0 based, and we want size here.
        sizeX = maxX + 1
        sizeY = maxY + 1

        #initialize map with 0 vents
        for yindex in range(sizeY):
            row = []
            for xindex in range(sizeX):
                row.append(0)
            vents.append(row)

        
        # for row in range(len(vents)):
        #     print(vents[row])

        print ("Map is size of " + str(sizeY) + " rows by " + str(sizeX) + " columns")

        for ventLine in ventLines:
            if(ventLine.start.x == ventLine.end.x):
                startY = min(ventLine.start.y, ventLine.end.y)
                endY = max(ventLine.start.y, ventLine.end.y)
                while endY >= startY:
                    vents[startY][ventLine.start.x] = vents[startY][ventLine.start.x] + 1
                    startY += 1
            elif (ventLine.start.y == ventLine.end.y):
                startX = min(ventLine.start.x, ventLine.end.x)
                endX = max(ventLine.start.x, ventLine.end.x)
                while endX >= startX:
                    vents[ventLine.start.y][startX] = vents[ventLine.start.y][startX] + 1
                    startX += 1

        overlaps = 0
        for row in range(sizeY):
            for column in range(sizeX):
                if vents[row][column] > 1:
                    overlaps += 1

        print("OVerlaps = " + str(overlaps))
                

processFile()