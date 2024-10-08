#Task 5
def graphRep(data):
  vertexCount, edgeCount = int(data[0].split(" ")[0]), int(data[0].split(" ")[1])
  graph = {node:[] for node in [i for i in range(1,int(vertexCount)+1)]}
  for edge in range(1,int(edgeCount)+1):
    vertex, neighbour = map(int, data[edge].split(" "))
    graph[vertex] += [neighbour]
    if vertex not in graph[neighbour]:
      graph[neighbour] += [vertex]

  return graph


def shortestPath(graph, destination):
  color = ["white"]*(len(graph)+1)
  queue = []
  parent = ["Null"]*(len(graph)+1)
  cost = [0]*(len(graph)+1)

  for vertex in graph:
    if color[vertex] == "white":
      color[vertex] = "grey"
      queue.append(vertex)

      while queue:
        node = queue.pop(0)
        if color[node] != "black":
          color[node] = "black"
          if parent[node] != "Null":
            cost[node] = cost[parent[node]] + 1


        for neighbour in graph[node]:
          if color[neighbour] == "white":
            color[neighbour] = "grey"
            parent[neighbour] = node
            queue.append(neighbour)

  path = []
  currentNode = destination
  while currentNode != "Null":
    path.append(currentNode)
    currentNode = parent[currentNode]

  return cost[destination], list(reversed(path))


inputfile = open("input5.txt","r")
outputfile = open("output5.txt","w")

elements = inputfile.readlines()
graph = graphRep(elements)
destination = int(elements[0].split(" ")[2])

cost, path = shortestPath(graph, destination)

outputfile.write("Time: " + str(cost) + "\n")
outputfile.write("Shortest Path: " + " ".join(list(map(str, path))))
outputfile.close()