
#Task 2
def graphRep(data):
  vertexCount, edgeCount = map(int, data[0].split(" "))
  graph = {node:[] for node in [i for i in range(1,int(vertexCount)+1)]}


  for j in range(1,int(edgeCount)+1):
    vertex, neighbour = map(int, data[j].split(" "))
    graph[vertex] += [neighbour]

  return graph


def BFS(graph):
  color = ["white"]*(len(graph)+1)
  queue = []
  result = []

  for vertex in graph:
    if color[vertex] == "white":
      color[vertex] = "grey"
      queue.append(vertex)

      while queue:
        node = queue.pop(0)
        if color[node] != "black":
          result.append(node)
          color[node] = "black"

        for neighbour in graph[node]:
          if color[neighbour] == "white":
            color[neighbour] = "grey"
            queue.append(neighbour)

  return result

inputfile = open("input2.txt","r")
outputfile = open("output2.txt","w")

elements = inputfile.readlines()
path = BFS(graphRep(elements))

outputfile.write(" ".join(list(map(str, path))))
outputfile.close()