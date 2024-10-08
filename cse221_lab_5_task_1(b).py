#task 1b
def bfs_topological_sort(graph, indegree):
  queue = []
  result = []

  for node in graph:
    if indegree[node] == 0:
      queue.append(node)

  while queue:
    current = queue.pop(0)
    result.append(current)

    for neighbor in graph[current]:
      indegree[neighbor] -= 1
      if indegree[neighbor] == 0:
        queue.append(neighbor)

  return result

inputfile = open("input1b.txt", "r")
outputfile = open("output1b.txt", "w")
var = inputfile.read().split('\n')
temp = var[0].split(" ")
vertices = int(temp[0])
edges = int(temp[1])
graph = {}
for i in range(1, vertices + 1):
    graph[i] = []
for k in range(1, len(var)):
    s_temp = var[k].split(" ")

    n1 = int(s_temp[0])
    n2 = int(s_temp[1])
    graph[n1].append(n2)

indegree = {node: 0 for node in graph}
for node in graph:
    for neighbor in graph[node]:
        indegree[neighbor] += 1

sorted_nodes = bfs_topological_sort(graph, indegree)
if len(sorted_nodes) == len(graph):
    for node in sorted_nodes:
        outputfile.write(str(node) + " ")
else:
    outputfile.write("Impossible")