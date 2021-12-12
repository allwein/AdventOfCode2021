import os

class Cave:
    def __init__(self, name):
        self.name = name
        self.connections = []
    
    def isBigCave(self):
        return self.name == self.name.upper()

    def isSmallCave(self):
        return self.name == self.name.lower()

class Path:        
    def __init__(self):
        self.steps = []

caves = []
count = 0

def processFile():
    with open('input.txt', 'r',-1,"utf-8") as listing:
        for line in listing.readlines():
            loadCaves(line)
        
        findPaths(Path(), "start", 1)
        # printCaves()
        print("Result is " + str(count))

def findPaths(path, nextStep, depth):
    global count
    # for i in range(depth):
    #     print("\t", end="")
    # print("Trying next step " + nextStep)

    if nextStep == "end":
        # print("FOUND A PATH: ")
        # print(path.steps)
        count = count + 1
        return

    nextCave = [cave for cave in caves if cave.name == nextStep][0]

    if any(visitedCave == nextStep for visitedCave in path.steps):
        if nextCave.isSmallCave():
            return

    path.steps.append(nextStep)

    for connection in nextCave.connections:
        findPaths(path, connection, depth + 1)

    path.steps.pop()



def loadCaves(line):
    line = line.strip()
    newCaves = line.split("-")

    if not any(cave.name == newCaves[0] for cave in caves):
        # print("Adding Cave " + newCaves[0] + " as 0")
        newCave = Cave(newCaves[0])
        newCave.connections.append(newCaves[1])
        caves.append(newCave)
    else:
        cave = [cave for cave in caves if cave.name == newCaves[0]][0]
        if not any(c == newCaves[1] for c in cave.connections):
            cave.connections.append(newCaves[1])

    if not any(cave.name == newCaves[1] for cave in caves):
        # print("Adding Cave " + newCaves[1] + " as 1")
        newCave = Cave(newCaves[1])
        newCave.connections.append(newCaves[0])
        caves.append(newCave)
    else:
        cave = [cave for cave in caves if cave.name == newCaves[1]][0]
        if not any(c == newCaves[0] for c in cave.connections):
            cave.connections.append(newCaves[0])  

def printCaves():
    for cave in caves:
        print("Cave: " + cave.name)
        print("\tConnections:")
        for connection in cave.connections:
            print("\t" + connection)

processFile()