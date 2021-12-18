from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_cost(self, u, v, weight):
        self.edges[u][v] = weight

def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D        

def processFile():
    with open('input.txt', 'r',-1,"utf-8") as listing:
        lines = []
        for line in listing.readlines():
            line = line.strip()
            numberLine = []
            for character in line:
                numberLine.append(int(character))
            lines.append(numberLine)

        square = len(lines[0]) * 5
        graph = Graph(square * square)
        expandLines(lines)
        addCosts(graph, lines, square)

        # for line in lines:
        #     for number in line:
        #         print(number,end="")
        #     print()
        # print(len(lines))
        #print(lines)
        #print(graph.edges)
        result = dijkstra(graph,0)
        #print(result)
        print("Result for last vertex is: " + str(result[graph.v-1]))

def expandLines(lines):
    originalLineLength = len(lines[0])
    for line in lines:
        mutateLine(line)

    for i in range(5):
        skipIndex = i * originalLineLength
      #  print("beforemutate " + str(len(lines)))
        for index in range(len(lines)):
           # print("\tskip index = " + str(skipIndex))
           # print("\tactual index = " + str(index))
            if index < skipIndex:
                continue
            else:
                mutateLineDown(lines, lines[index])
               # print("\t\tafter mutate " + str(len(lines)))

def addCosts(graph, lines, square):
        for i in range(square):
            # print(square)
            # print(i)
            # print(len(lines))
            # print()
            line = lines[i]
            for j in range(square):
                cost = line[j]
                currentVertex = i * square + j
                #print(currentVertex)
                #left
                if j > 0:
                    graph.add_cost(currentVertex-1 ,currentVertex ,int(cost))
                    
                #right
                if j < square-1:
                    graph.add_cost(currentVertex+1 ,currentVertex ,int(cost))

                #up
                if i > 0:
                    graph.add_cost(currentVertex-square ,currentVertex ,int(cost))
                    
                #down
                if i < square-1:
                    graph.add_cost(currentVertex+square ,currentVertex ,int(cost))

def mutateLineDown(lines, line):
    length = len(line)
    newLine = []
    for j in range(length):
        offset = j
        updatedValue = int(line[offset]) + 1
        if updatedValue > 9:
            updatedValue = 1
        newLine.append(updatedValue)
    
    lines.append(newLine)

def mutateLine(line):
    length = len(line)
    for i in range(4):
        for j in range(length):
            offset = i * length + j
            updatedValue = int(line[offset]) + 1
            if updatedValue > 9:
                updatedValue = 1
            line.append(updatedValue)



def mutateLines(lines):
    newLines = lines.copy()
    square = len(newLines[0])

    for i in range(square):
        line = newLines[i]
        for j in range(square):
            updatedValue = int(line[j]) + 1
            if updatedValue > 9:
                updatedValue = 1
            newLines[i][j] = updatedValue

    return newLines
        

processFile()