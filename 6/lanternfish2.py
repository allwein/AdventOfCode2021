import os

def processFile():
    fish = []
    with open('input3.txt', 'r',-1,"utf-8") as listing:
        for line in listing.readlines():
            fish = line.split(",")

    print("Initial State: " + str(fish))
    for day in range(64):
        newFish = []
        for index in range(len(fish)):
            fish[index] = int(fish[index]) - 1
            if fish[index] == -1:
                fish[index] = 6
                newFish.append(8)

        fish.extend(newFish)
        # print('\n')
        # print("Day " + str(day+1) + ": " + str(len(fish)))
        # print("Fish is: " ) 
        # print(fish)        


        # print("Day " + str(day+1) + ": " + str(fish))

    # print("Fish is: " ) 
    # print(fish)        
    print("Result is " + str(len(fish)))

# 0 -> 107
# 1 -> 106
# 2 -> 86
# 3 -> 86
# 4 -> 71
# 5 -> 70
# 6 -> 64

# 0 -> 350
# 1 -> 348
# 2 -> 292
# 3 -> 285
# 4 -> 257
# 5 -> 236
# 6 -> 228

processFile()