import os

def processFile():
    with open('input.txt', 'r',-1,"utf-8") as listing:
        count = 0
        for line in listing.readlines():
            input = line.split(" | ")
            digits = input[0].split()
            code = input[1].split()

            for digit in code:
                length = len(digit)
                # print("Processing digit: " + digit)
                # print("length: " + str(length))

                if length == 2 or length == 4 or length == 3 or length == 7:
                    count += 1
                    # print("Count is now " + str(count))

        print("Result is " + str(count))

processFile()