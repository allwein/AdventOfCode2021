
riskMap = []

def processFile():
    with open('input2.txt', 'r',-1,"utf-8") as listing:
        for line in listing.readlines():
            riskLine = []
            for character in line.strip():
                riskLine.append(int(character))

            riskMap.append(riskLine)

        printRisk()


def printRisk():
    global riskMap
    for riskLine in riskMap:
        for risk in riskLine:
            print(str(risk), end = "")
        print()

processFile()