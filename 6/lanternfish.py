import os

def processFile():
    fish = []
    with open('input.txt', 'r',-1,"utf-8") as listing:
        for line in listing.readlines():
            fish = line.split(",")

    print("Initial State: " + str(fish))
    for day in range(80):
        newFish = []
        for index in range(len(fish)):
            fish[index] = int(fish[index]) - 1
            if fish[index] == -1:
                fish[index] = 6
                newFish.append(8)

        fish.extend(newFish)

        # print("Day " + str(day+1) + ": " + str(fish))

    # print("Fish is: " ) 
    # print(fish)        
    print("Result is " + str(len(fish)))

processFile()