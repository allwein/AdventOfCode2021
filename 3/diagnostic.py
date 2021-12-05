import os

def processFile():
    gamma = ""
    epsilon = ""
    sums = []
    count = 0
    with open('input.txt', 'r',-1,"utf-8") as listing:
        for line in listing.readlines():
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

    limit = count / 2
    for x in range(len(sums)):
        if sums[x] >= limit:
            gamma = gamma + str(1)
            epsilon = epsilon + str(0)
        else:
            gamma = gamma + str(0)
            epsilon = epsilon + str(1)

        rawSum = rawSum + " " + str(sums[x])

    print("Count is " + str(count)) 
    print("Raw Sum is " + str(rawSum))        
    print("Gamma Rate is " + gamma + " or " + str(int(gamma,2)))
    print("Epsilon Rate is " + epsilon + " or " + str(int(epsilon,2)))
    print("Result is " + str(int(gamma,2) * int(epsilon,2)))

processFile()