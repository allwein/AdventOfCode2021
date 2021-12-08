import os

def processFile():
    crabs = []
    with open('input.txt', 'r',-1,"utf-8") as listing:
        for line in listing.readlines():
            finput = line.split(",")
            max = 0
            for fin in finput:
                if int(fin) > max:
                    max = int(fin)
            
            max = max + 1

            for i in range(max):
                crabs.append(0)

            for fin in finput:
                crabs[int(fin)] = crabs[int(fin)] + 1

            min = 999999999999999999999999

            for movePosition in range(max):
                cost = 0
                for i in range(max):
                    perCost = abs(movePosition - i)
                    cost = cost + (crabs[i] * perCost)

                if cost < min:
                    min = cost

                print("Cost for position " + str(movePosition) + " is " + str(cost))

            print("Result is " + str(min))


processFile()