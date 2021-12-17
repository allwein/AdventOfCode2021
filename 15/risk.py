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
    with open('input2.txt', 'r',-1,"utf-8") as listing:
        lines = []
        for line in listing.readlines():
            line = line.strip()
            numberLine = []
            for character in line:
                numberLine.append(int(character))
            lines.append(numberLine)

        square = len(lines[0])
        graph = Graph(square * square * 25)

        lines2 = mutateLines(lines)
        lines3 = mutateLines(lines2)
        lines4 = mutateLines(lines3)
        lines5 = mutateLines(lines4)
        lines6 = mutateLines(lines5)
        lines7 = mutateLines(lines6)
        lines8 = mutateLines(lines7)
        lines9 = mutateLines(lines8)

        addCosts(graph, lines, square, 0, 0)
        addCosts(graph, lines2, square, 0,  1)
        addCosts(graph, lines3, square, 0,  2)
        addCosts(graph, lines4, square, 0, 3)
        addCosts(graph, lines5, square, 0,  4)

        addCosts(graph, lines2, square, square * 1, 0)
        addCosts(graph, lines3, square, square * 1, 1)
        addCosts(graph, lines4, square, square * 1, 2)
        addCosts(graph, lines5, square, square * 1, 3)
        addCosts(graph, lines6, square, square * 1, 4)

        addCosts(graph, lines3, square, square * 2, 0)
        addCosts(graph, lines4, square, square * 2, 1)
        addCosts(graph, lines5, square, square * 2, 2)
        addCosts(graph, lines6, square, square * 2, 3)
        addCosts(graph, lines7, square, square * 2, 4)

        addCosts(graph, lines4, square, square * 3, 0)
        addCosts(graph, lines5, square, square * 3, 1)
        addCosts(graph, lines6, square, square * 3, 2)
        addCosts(graph, lines7, square, square * 3, 3)
        addCosts(graph, lines8, square, square * 3, 4)

        addCosts(graph, lines5, square, square * 4, 0)
        addCosts(graph, lines6, square, square * 4, 1)
        addCosts(graph, lines7, square, square * 4, 2)
        addCosts(graph, lines8, square, square * 4, 3)
        addCosts(graph, lines9, square, square * 4, 4)

        #print(graph.edges)
        result = dijkstra(graph,0)
        #print(result)
        print("Result for last vertex is: " + str(result[graph.v-1]))

def addCosts(graph, lines, square, xoffset, yoffset):
        for i in range(square):
            line = lines[i]
            for j in range(square):
                cost = line[j]
                currentVertex = i * square + j + xoffset + (yoffset * square * square * 5)
                print(currentVertex)
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