import os

def processFile():
    horizontal = 0
    depth = 0
    aim = 0
    with open('input.txt', 'r',-1,"utf-8") as listing:
        for line in listing.readlines():
            tokens = line.split(" ")
            if tokens[0] == "forward":
                horizontal += int(tokens[1])
                depth += int(tokens[1]) * aim
            elif tokens[0] == "up":
                aim -= int(tokens[1])
            else:
                aim += int(tokens[1])

    print("Horizontal is " + str(horizontal))
    print("Aim is " + str(aim))
    print("Depth is " + str(depth))
    print("Result is " + str(depth * horizontal))

processFile()