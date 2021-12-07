import os

def processFileOld():
    fish = []
    with open('input2.txt', 'r',-1,"utf-8") as listing:
        for line in listing.readlines():
            fish = line.split(",")

    fishreport = []
    for i in range(9):
        fishreport.append(0)
    
    for fishy in fish:
        fishreport[int(fishy)] = fishreport[int(fishy)] + 1

    print("Initial State: " + str(fishreport))            

    for day in range(18):
        newFish = []
        for index in range(len(fish)):
            fish[index] = int(fish[index]) - 1
            if fish[index] == -1:
                fish[index] = 6
                newFish.append(8)

        fish.extend(newFish)

        # print("Day " + str(day+1) + ": " + str(fish))
        fishreport = []
        for i in range(9):
            fishreport.append(0)
        
        for fishy in fish:
            fishreport[int(fishy)] = fishreport[int(fishy)] + 1

        print("Day " + str(day+1) + ": " + str(fishreport))

    print("Result is " + str(len(fish)))

def processFile():
    fish = []
    with open('input.txt', 'r',-1,"utf-8") as listing:
        for i in range(9):
            fish.append(0)
        
        for line in listing.readlines():
            finput = line.split(",")
            for fin in finput:
                fish[int(fin)] = fish[int(fin)] + 1

    print("\n***************************\nInitial State: " + str(fish))

    for day in range(256):
        newfish = fish[0]
        fish[0] = fish[1]
        fish[1] = fish[2]
        fish[2] = fish[3]
        fish[3] = fish[4]
        fish[4] = fish[5]
        fish[5] = fish[6]
        fish[6] = fish[7] + newfish #include the number of fish resetting from 0
        fish[7] = fish[8]
        fish[8] = newfish
        # print("Day " + str(day+1) + ": " + str(fish))

    sum = 0
    for fishies in fish:
        sum = sum + fishies

    print("Result is " + str(sum))

# processFileOld()
processFile()