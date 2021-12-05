import os

def processFile():
    position = 0
    queue = []

    previousSlidingSum = 0
    slidingSum = 0
    increases = 0

    with open('input.txt', 'r',-1,"utf-8") as listing:
        for line in listing.readlines():
            position += 1
            queue.append(int(line))
            
            if len(queue) < 4:
                continue

            previousSlidingSum = queue[0] + queue[1] + queue[2]
            queue.pop(0)
            slidingSum = queue[0] + queue[1] + queue[2]

            if slidingSum > previousSlidingSum:
                increases += 1

            print("\n\n********************************")
            print("previousSlidingSum is " + str(previousSlidingSum))
            print("slidingSum is " + str(slidingSum))


        print("# Increases is " + str(increases))



processFile()