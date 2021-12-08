import os

def processFile():
    with open('input.txt', 'r',-1,"utf-8") as listing:
        codeSum = 0
        for line in listing.readlines():
            input = line.split(" | ")
            digits = input[0].split()
            code = input[1].split()

            #print(digits)
            for index in range(len(digits)):
                digits[index] = sortKey(digits[index])

            decodedDigits = decodeDigits(digits)
            decodedCode = ""

            # print(digits)
            # print(decodedDigits)
            for digit in code:
                value = decodedDigits[sortKey(digit)]
                #print("Value is " + str(value))
                decodedCode = decodedCode + str(value)
            
            codeSum = codeSum + int(decodedCode)

        print("Result is " + str(codeSum))

def findSegmentB(digits):
    # segment b is the only one that's used 6 times
    digitCounts = {}
    digitCounts["a"] = 0
    digitCounts["b"] = 0
    digitCounts["c"] = 0
    digitCounts["d"] = 0
    digitCounts["e"] = 0
    digitCounts["f"] = 0
    digitCounts["g"] = 0

    for digit in digits:
        for character in digit:
            digitCounts[character] = digitCounts[character] + 1

    for character in digitCounts:
        if digitCounts[character] == 6:
            return character

    print("COULD NOT FIND SEGMENT B")


def decodeDigits(digits):
    decodedDigits = {}
    one = findDigitByCodeLength(digits, 2)
    #print("1 = " + one)
    four = findDigitByCodeLength(digits, 4)
    #print("4 = " + four)
    seven = findDigitByCodeLength(digits, 3)
    #print("7 = " + seven)
    eight = findDigitByCodeLength(digits, 7)
    #print("8 = " + eight)
    segmentA = subtractString(seven, one)
    #print("segmentA = " + segmentA)
    nine = findNine(digits, four, segmentA)
    #print("9 = " + nine)
    segmentG = subtractString(subtractString(nine, four), segmentA)
    segmentE = subtractString(eight, nine)
    segmentB = findSegmentB(digits)
    segmentD = subtractString(subtractString(four, one), segmentB)
    zero = subtractString(eight, segmentD)

    temp = digits.copy()
    temp.remove(zero)
    temp.remove(one)
    temp.remove(four)
    temp.remove(seven)
    temp.remove(eight)
    temp.remove(nine)

    six = findDigitByCodeLength(temp, 6)
    temp.remove(six)
    segmentC = subtractString(eight, six)
    five = subtractString(nine, segmentC)
    temp.remove(five)

    # That leaves two digits: 2 and 3
    two = ""
    three = ""

    if subtractString(temp[0], nine) == "":
        three = temp[0]
        two = temp[1]
    else:
        two = temp[0]
        three = temp[1]

    decodedDigits[zero] = 0
    decodedDigits[one] = 1
    decodedDigits[two] = 2
    decodedDigits[three] = 3
    decodedDigits[four] = 4
    decodedDigits[five] = 5
    decodedDigits[six] = 6
    decodedDigits[seven] = 7
    decodedDigits[eight] = 8
    decodedDigits[nine] = 9

    # decodedDigits[sortKey("ab")] = 1
    # decodedDigits[sortKey("gcdfa")] = 2
    # decodedDigits[sortKey("fbcad")] = 3
    # decodedDigits[sortKey("eafb")] = 4
    # decodedDigits[sortKey("cdfbe")] = 5
    # decodedDigits[sortKey("cdfgeb")] = 6
    # decodedDigits[sortKey("dab")] = 7
    # decodedDigits[sortKey("acedgfb")] = 8
    # decodedDigits[sortKey("cefabd")] = 9

    return decodedDigits

def findDigitByCodeLength(digits, length):
    for digit in digits:
        if len(digit) == length:
            return sortKey(digit)

def sortKey(keyString):
    return "".join(sorted(keyString))

def subtractString(sourceString, subtractString):
    for character in subtractString:
        sourceString = sourceString.replace(character, '')

    return sourceString

def findNine(digits, four, segmentA):
    for digit in digits:
        digit = sortKey(digit)
        if len(digit) == 6:
            if segmentA in digit:
                foundAll = True
                for character in four:
                    if (character in digit) == False:
                        foundAll = False

                if foundAll:
                    return sortKey(digit)

    print("DID NOT FIND NINE")


processFile()