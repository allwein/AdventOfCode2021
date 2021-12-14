import os

class PairInsertion:
    def __init__(self, pair, value):
        self.pair = pair
        self.value = value
        self.count = 0
        self.split1 = pair[0:1] + value
        self.split2 = value + pair[1:2]

polymer = ""
pairs = []
pairsDict = {}
counts = []

def processFile():
    global polymer
    global pairsDict
    global pairs
    with open('input.txt', 'r',-1,"utf-8") as listing:
        index = 0
        for line in listing.readlines():
            if len(line.strip()) == 0:
                continue

            if index == 0:
                polymer = line.strip()
                index = index + 1
                continue
            
            loadLine(line)

        print(polymer)
        initCounts()
        for character in polymer:
            addCountForLetter(character,1)

        for i in range(len(polymer)-1):
            substring = polymer[i:i+2]
            pairsDict[substring].count = pairsDict[substring].count + 1

        for i in range(40):
            processPairs()
            processCounts()

def addCountForLetter(letter, count):
    global counts
    start = ord("A")
    value = ord(letter) - start
    counts[value] = counts[value] + count
    print("Adding " + str(count) + " to " + letter + " for total of " + str(counts[value]))

def initCounts():
    global counts
    counts=[] 
    for i in range(26):
        counts.append(0)
        
def processCounts():
    global counts
    start = ord("A")
    for character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if counts[ord(character) - start] > 0:
            print (character + ": " + str(counts[ord(character) - start]))
        
    mostCommon = 0
    leastCommon = 0
    sum = 0
    for value in range(26):
        if leastCommon == 0:
            leastCommon = counts[value]
            
        if counts[value] > mostCommon:
            mostCommon = counts[value]

        if counts[value] < leastCommon and counts[value] > 0:
            leastCommon = counts[value]
        
        sum = sum + counts[value]

    print("Most Common is " + str(mostCommon))
    print("Least Common is " + str(leastCommon))
    print("Result is " + str(mostCommon - leastCommon))
    print("Length is " + str(sum))
    print("")
        
def processPairs():
    global pairs
    global pairsDict

    updateDict = {}
    for pair in pairs:
        updateDict[pair.pair] = 0
        
    for pair in pairs:
        print("Processing " + pair.pair)
        addCountForLetter(pair.value, pair.count)
        updateDict[pair.split1] = updateDict[pair.split1] + pair.count
        updateDict[pair.split2] = updateDict[pair.split2] + pair.count
        updateDict[pair.pair] = updateDict[pair.pair] - pair.count

    for pairKey in updateDict:
        pairsDict[pairKey].count = pairsDict[pairKey].count + updateDict[pairKey]


    # for pair in pairs:    
    #     print(pair.pair + ": " + str(pair.count))

def loadLine(line):
    global pairs
    global pairsDict
    line = line.strip()
    input = line.split(" -> ")
    pair = PairInsertion(input[0],input[1])
    pairs.append(pair)
    pairsDict[input[0]] = pair

processFile()