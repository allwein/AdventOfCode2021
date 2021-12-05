import os

def processFile():
    horizontal = 0
    depth = 0
    with open('input.txt', 'r',-1,"utf-8") as listing:
        for line in listing.readlines():
            tokens = line.split(" ")
            if tokens[0] == "forward":
                horizontal += int(tokens[1])
            elif tokens[0] == "up":
                depth -= int(tokens[1])
            else:
                depth += int(tokens[1])

    print("Horizontal is " + str(horizontal))
    print("Depth is " + str(depth))
    print("Result is " + str(depth * horizontal))

processFile()