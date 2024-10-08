#1a
def graphRep(data):
  vertices = int(data[0].split(" ")[0])
  edges = int(data[0].split(" ")[1])
  adjacencyMatrix = [[0]*(vertices + 1) for j in range(vertices + 1)]

  for i in range(1,edges+1):
    adjacencyMatrix[int(data[i].split(" ")[0])][int(data[i].split(" ")[1])] = int(data[i].split(" ")[2])

  return adjacencyMatrix

inputfile = open("input1a.txt","r")
outputfile = open("output1a.txt","w")

l = inputfile.readlines()
adjacencyMatrix = graphRep(l)

for j in adjacencyMatrix:
  elem = list(map(str, j))
  outputfile.write(" ".join(elem) + "\n")

outputfile.close()