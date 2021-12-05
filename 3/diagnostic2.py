import os

def processFile():
    mostCommon = ""
    leastCommon = ""
    sums = []
    count = 0
    oxygen = []
    co2 = []

    with open('input.txt', 'r',-1,"utf-8") as listing:
        for line in listing.readlines():
            oxygen.append(line)
            co2.append(line)
            count += 1
            if len(sums) == 0:
                for x in range(len(line)):
                    if line[x:x+1] != "\n":
                        sums.append(0)

            for x in range(len(line)):
                if line[x:x+1] != "\n":
                    sums[x] += int(line[x:x+1])

    rawSum = ""
    for x in range(len(sums)):
        rawSum = rawSum + " " + str(sums[x])

    for x in range(len(sums)):
        oxygenLimit = len(oxygen) / 2
        oxygenSums = []

        if len(oxygenSums) == 0:
            for y in range(len(sums)):
                oxygenSums.append(0)

        for y in range(len(oxygen)):
            oxygenSums[x] += int(oxygen[y][x:x+1])

        if oxygenSums[x] >= oxygenLimit:
            mostCommon =   str(1)
            leastCommon =   str(0)
        else:
            mostCommon =   str(0)
            leastCommon =  str(1)

        temp = oxygen.copy()
        validIndex = 0
        for o in range(len(temp)):
            #print(oxygen)
            # print("o is " + str(o))
            # print("len(temp) is " + str(len(temp)))
            if len(oxygen) == 1:
                continue
            if temp[o][x] == mostCommon :
                validIndex += 1
            else: 
                #print("Popping " + str (oxygen[validIndex]) + "because ")
                oxygen.pop(validIndex)

        print("mostCommon is " + str(mostCommon))
        print("leastCommon is " + str(leastCommon))

        co2Limit = len(co2) / 2
        co2Sums = []

        if len(co2Sums) == 0:
            for y in range(len(sums)):
                co2Sums.append(0)

        for y in range(len(co2)):
            co2Sums[x] += int(co2[y][x:x+1])

        if co2Sums[x] >= co2Limit:
            mostCommon =   str(1)
            leastCommon =   str(0)
        else:
            mostCommon =   str(0)
            leastCommon =  str(1)
        #oxygen = temp.copy()

        temp = co2.copy()
        validIndex = 0
        for c in range(len(temp)):
            if len(co2) == 1:
                continue
            if temp[c][x] != leastCommon :
                co2.pop(validIndex)
            else: 
                validIndex += 1

        #co2 = temp.copy()

    print("Count is " + str(count)) 
    print("Raw Sum is " + str(rawSum))
    print("oxygen is " + str(oxygen[0])  + " or " + str(int(oxygen[0],2)))
    print("co2 is " + str(co2[0])  + " or " + str(int(co2[0],2)))




    print("Result is " + str(int(oxygen[0],2) * int(co2[0],2)))

processFile()