import os

def processFile():
    with open('input.txt', 'r',-1,"utf-8") as listing:
        corrupted = []
        score = 0
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
                        print("Corrupted: " + line)
                        corrupted.append(character)
                        score = score + getScore(character)
                        break
                    stack.pop()

            if len(stack) != 0: #incomplete        
                print("Incomplete: " + line)
                continue

        print("Score is " + str(score))

def getScore(character):
    if character == ")":
        return 3
         
    if character == "]":
        return 57
         
    if character == "}":
        return 1197
         
    if character == ">":
        return 25137
         
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