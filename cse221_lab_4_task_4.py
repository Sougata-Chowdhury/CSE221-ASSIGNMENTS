#task 4
def graphRep(data):
  vertex, edges = map(int, data[0].split(" "))
  graph = {n:[] for n in [i for i in range(1,int(vertex)+1)]}

  for j in range(1,int(edges)+1):
    vertex, neighbour = map(int, data[j].split(" "))
    graph[vertex] += [neighbour]

  return graph

def cycleDetection(graph):
  color=["White"]*((len(graph))+1)
  queue=[]
  result=[]
  for i in graph:
    if color[i]=="White":
      color[i]="Grey"
      queue.append(i)
  while queue:
    n=queue.pop(0)
    if color[n]!="Black":
      color[n]="Black"
      result.append(n)
    for j in graph:
      if j in result and color[j]=="Black":
        return True
      elif color[j]=="White":
        color[j]="Grey"
        queue.append(j)
  return False
inputfile = open("input4.txt","r")
outputfile = open("output4.txt","w")

elements = inputfile.readlines()

if cycleDetection(graphRep(elements)):
  outputfile.write("Yes")
else:
  outputfile.write("No")

outputfile.close()