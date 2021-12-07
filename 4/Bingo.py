import os

class Board:
    def __init__(self, data):
        self.data = data

    def add_call(self, number):
        for row in range(len(self.data)):
            for column in range(len(self.data[row])):
                if self.data[row][column] == number:
                    self.data[row][column] = -1

    def hasWin(self):
        for row in range(len(self.data)):
            rowSum = 0
            for column in range(len(self.data[row])):
                rowSum = rowSum + int(self.data[row][column])

            if rowSum == -5:
                return True

        for column in range(5):
            columnSum = 0
            for row in range(len(self.data)):
                columnSum = columnSum + int(self.data[row][column])
            
            if columnSum == -5:
                return True

    def calculateValue(self, call):
        valueSum = 0
        for row in range(len(self.data)):
            for column in range(len(self.data[row])):
                if(int(self.data[row][column]) != -1):
                    valueSum = valueSum + int(self.data[row][column])

        print("Value Sum is: " + str(valueSum))
        print("Win Value is " + str(valueSum * int(call)))


def processFile():
    calls = []
    boards = []
    index = 0
    with open('input.txt', 'r',-1,"utf-8") as listing:
        temp = []
        for line in listing.readlines():
            index += 1
            line = line[:-1]
            if index == 1:
                calls = line.split(",")
                continue
            
            if line == "":
                if(len(temp)>0):
                    boards.append(Board(temp))

                temp = []
                continue

            temp.append(line.split())


    print(str(len(calls)) + " calls")
    print(calls)

    print(str(len(boards)) + " boards")

    for board in boards:
        for row in board.data:
            print(row)
        print("\n")  

    print ("PROCESSING CALLS")

    for call in calls:
        print("CALLING " + str(call))
        for board in boards:
            board.add_call(call)
            for row in board.data:
                print(row)
            print("\n")  
            if board.hasWin():
                print("WINNER")
                board.calculateValue(call)
                exit()

    for board in boards:
        for row in board.data:
            print(row)
        print("\n")            

processFile()