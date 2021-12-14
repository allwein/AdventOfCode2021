import os

def processFile():
    with open('input.txt', 'r',-1,"utf-8") as listing:
        corrupted = []
        scores = []
        for line in listing.readlines():
            stack = []
            for character in line:
                if len(stack) == 0:
                    stack.append(character)
                    continue
                
                if isOpen(character):
                    stack.append(character)
                    continue

                if isClose(character):
                    if stack[len(stack)-1] != getOpenForClose(character): #corrupted
                        #print("Corrupted: " + line)
                        corrupted.append(character)
                        stack = []
                        break
                    stack.pop()

            if len(stack) == 0:
                continue

            lineScore = 0
            if len(stack) != 0: #incomplete
                #print("Incomplete: " + line)
                length = len(stack)
                while length > 0:
                    character = stack[length-1]
                    lineScore = lineScore * 5
                    lineScore = lineScore + getScore(character)
                    length = length -1
            #print("lineScore is " + str(lineScore))
            scores.append(lineScore)

        scores.sort()

        for score in scores:
            print(score)

        print("Score is " + str(scores[len(scores)//2]))

def getScore(character):
    if character == "(":
        return 1
         
    if character == "[":
        return 2
         
    if character == "{":
        return 3
         
    if character == "<":
        return 4
         
    return 0

def isOpen(character):
    return character == "(" or character == "[" or character == "{" or character == "<"

def isClose(character):
    return character == ")" or character == "]" or character == "}" or character == ">"

def getCloseForOpen(character):
    if character == "(":
        return ")"
         
    if character == "[":
        return "]"
         
    if character == "{":
        return "}"
         
    if character == "<":
        return ">"
         
    return "0"

def getOpenForClose(character):
    if character == ")":
        return "("
         
    if character == "]":
        return "["
         
    if character == "}":
        return "{"
         
    if character == ">":
        return "<"
         
    return "0"    

processFile()