

#Task 2
import heapq

def findPath(source, graph, nodes):
    distance = {}
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

    return distance

inputfile = open("input2.txt", "r")
outputfile = open("output2.txt", "w")
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

source1 = l[len(l) - 1].pop(0)
source2 = l[len(l) - 1].pop()

path1 = findPath(source1, graph, nodes)
path2 = findPath(source2, graph, nodes)

meeting_node = None
min_time = 99999999

for node in path1:
    if node in path2:
        total_time = max(path1[node], path2[node])
        if total_time < min_time:
            min_time = total_time
            meeting_node = node

if meeting_node is None:
    outputfile.write("Impossible")
else:
    outputfile.write(f"Time {min_time}\nNode {meeting_node}")

inputfile.close()
outputfile.close()