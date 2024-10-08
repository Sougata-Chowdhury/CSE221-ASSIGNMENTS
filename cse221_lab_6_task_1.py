

#task 1
import heapq

inputfile = open("input1.txt", "r")
outputfile = open("output1.txt", "w")
var = inputfile.readlines()
l = []
for i in range(len(var)):
    v = list(map(int, var[i].split(" ")))
    l.append(v)

graph = {}
nodes = l[0][0]
edges = l[0][1]
for e in range(nodes + 1):
    graph[e] = []
for j in range(1, len(l) - 1):
    graph[l[j][0]].append((l[j][1], l[j][2]))

distance = {}
source = l[len(l) - 1].pop()
parent = [0] * (nodes + 1)
parent[source] = source

min_heap = [[0, source]]
while min_heap:
    dist, n = heapq.heappop(min_heap)
    if n in distance:
        continue
    distance[n] = dist
    for n2, w2 in graph[n]:
        if n2 not in distance:
            heapq.heappush(min_heap, [dist + w2, n2])
for j in range(1, nodes + 1):
    if j not in distance:
        distance[j] = -1

for node in range(1, nodes + 1):
    outputfile.write(f"{distance.get(node, -1)} ")

inputfile.close()
outputfile.close()