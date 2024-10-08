#Task 2
import heapq

def bfs_topological_sort(graph, indegree):
  queue = []
  result = []

  for node, degree in indegree.items():
    if degree == 0:
      heapq.heappush(queue, node)

  while queue:
    current = heapq.heappop(queue)
    result.append(current)

    for neighbor in graph[current]:
      indegree[neighbor] -= 1
      if indegree[neighbor] == 0:
        heapq.heappush(queue, neighbor)

  return result

inputfile = open("input2.txt", "r")
outputfile = open("output2.txt", "w")
var = inputfile.read().split('\n')
temp = var[0].split(" ")
vertices = int(temp[0])
edges = int(temp[1])
graph = {i: [] for i in range(1, vertices + 1)}
indegree = {i: 0 for i in range(1, vertices + 1)}

for k in range(1, len(var)):
    s_temp = var[k].split(" ")
    n1 = int(s_temp[0])
    n2 = int(s_temp[1])
    graph[n1].append(n2)
    indegree[n2] += 1

sorted_nodes = bfs_topological_sort(graph, indegree)
if len(sorted_nodes) == len(graph):
    outputfile.write(" ".join(map(str, sorted_nodes)) + " ")
else:
    outputfile.write("Impossible")

inputfile.close()
outputfile.close()
