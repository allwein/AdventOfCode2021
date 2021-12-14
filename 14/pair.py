import os

class PairInsertion:
    def __init__(self, pair, value):
        self.pair = pair
        self.value = value

polymer = ""
pairs = []

def processFile():
    global polymer
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
        for i in range(10):
            processPairs()

        start = ord("A")
        counts=[]
        for i in range(26):
            counts.append(0)

        for character in polymer:
            value = ord(character) - start
            counts[value] = counts[value] + 1

        mostCommon = 0
        leastCommon = 999999999
        for value in range(26):
            if counts[value] > mostCommon:
                mostCommon = counts[value]

            if counts[value] < leastCommon and counts[value] > 0:
                leastCommon = counts[value]

        print("Result is " + str(mostCommon - leastCommon))

        
        
def processPairs():
    global polymer
    global pairs

    startString = polymer
    polymer = ""
    for i in range(len(startString)-1):
        substring = startString[i:i+2]
        for pair in pairs:
            if substring == pair.pair:
                polymer = polymer + substring[0:1] + pair.value
                break

        if i == len(startString)-2:
            #We're at the end, add the last letter
            polymer = polymer + substring[1:2]
        
        

def loadLine(line):
    global pairs
    line = line.strip()
    input = line.split(" -> ")
    pairs.append(PairInsertion(input[0],input[1]))

processFile()