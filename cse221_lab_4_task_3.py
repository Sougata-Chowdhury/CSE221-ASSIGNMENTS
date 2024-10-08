

#Task 3
def graphRep(data):
  vertexCount, edgeCount = int(data[0].split(" ")[0]), int(data[0].split(" ")[1])
  graph = {node:[] for node in [i for i in range(1,int(vertexCount)+1)]}

  for edge in range(1,int(edgeCount)+1):
    vertex, neighbour = map(int, data[edge].split(" "))
    graph[vertex] += [neighbour]
    if vertex not in graph[neighbour]:
      graph[neighbour] += [vertex]

  return graph


def DFS(graph):
  color = ["white"]*(len(graph)+1)
  stack = []
  result = []

  for vertex in graph:
    if color[vertex] == "white":
      color[vertex] = "grey"
      stack.append(vertex)

      while stack:
        node = stack.pop()
        if color[node] != "black":
          result.append(node)
          color[node] = "black"

        for neighbour in graph[node]:
          if neighbour not in result:
            if color[neighbour] == "grey":
              color[neighbour] = "black"
              result.append(neighbour)
            elif color[neighbour] == "white":
              color[neighbour] = "white"
              stack.append(neighbour)

  return result

inputfile = open("input3.txt","r")
outputfile = open("output3.txt","w")

elements = inputfile.readlines()
path = DFS(graphRep(elements))

outputfile.write(" ".join(list(map(str, path))))
outputfile.close()