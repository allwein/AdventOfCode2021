import os

class Point:
    def __init__(self, x,y):
        self.x = int(x)
        self.y = int(y)

    def print(self):
        return "POINT: x=" + str(self.x) + " y=" + str(self.y)

class Fold:
    def __init__(self, direction, value):
        self.direction = direction
        self.value = int(value)

points = []
folds = []

def processFile():
    global points
    with open('input.txt', 'r',-1,"utf-8") as listing:
        for line in listing.readlines():
            loadLine(line)
        
        for fold in folds:
            performFold(fold.direction, fold.value)
            #printData()
            #break

        #print("Result is " + str(len(points)))
        printDots()

def printDots():
    global points
    points = sorted(points, key=lambda p: (p.y, p.x), reverse=False)
    maxX = 0
    maxY = 0
    for point in points:
        if point.x > maxX:
            maxX = point.x
        if point.y > maxY:
            maxY = point.y

    for y in range(maxY + 1):
        for x in range(maxX + 1):
            exists = [p for p in points if p.x == x and p.y == y]        
            if len(exists) > 0:
                print("*", end="")
            else:
                print(" ", end="")
        print("\n", end="")



def performFold(direction, index):
    global points
    newPoints = []

    for point in points:
        if direction == "x":
            if point.x < index:
                exists = [p for p in newPoints if p.x == point.x and p.y == point.y]
                if len(exists) == 0:
                    newPoints.append(point)
            else:
                delta = point.x - index
                point.x = index - delta
                exists = [p for p in newPoints if p.x == point.x and p.y == point.y]
                if len(exists) == 0:
                    newPoints.append(point)

        if direction == "y":
            if point.y < index:
                exists = [p for p in newPoints if p.x == point.x and p.y == point.y]
                if len(exists) == 0:
                    newPoints.append(point)
            else:
                delta = point.y - index
                point.y = index - delta
                exists = [p for p in newPoints if p.x == point.x and p.y == point.y]
                if len(exists) == 0:
                    newPoints.append(point)

    points = newPoints
                
def loadLine(line):
    line = line.strip()
    if len(line) > 13:
        direction = line[11:12]
        value = line[13:]
        fold = Fold(direction,value)
        folds.append(fold)
    else:
        if len(line) == 0:
            return

        pointLine = line.split(",")
        point = Point(pointLine[0], pointLine[1])
        points.append(point)

def printData():
    for point in points:
        print("Point: x=" + str(point.x) + " y=" + str(point.y))

    for fold in folds:
        print("Fold on " + str(fold.direction) + " at " + str(fold.value))

    print("Number of dots is " + str(len(points)))
    print("\n")

processFile()