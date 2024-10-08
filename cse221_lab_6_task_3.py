

#Task 3
import heapq

def findPath(source, graph, nodes):
    max_danger_levels = {}
    min_heap = [(0, source)]

    while min_heap:
        danger_level, node = heapq.heappop(min_heap)

        if node in max_danger_levels:
            continue

        max_danger_levels[node] = danger_level

        for neighbor, danger in graph[node]:
            max_danger = max(danger_level, danger)
            if neighbor not in max_danger_levels:
                heapq.heappush(min_heap, (max_danger, neighbor))

    return max_danger_levels

inputfile = open("input3.txt", "r")
var = inputfile.readlines()

nodes, edges = map(int, var[0].split())
graph = {}
for i in range(1, nodes + 1):
    graph[i] = []

for j in range(1, edges + 1):
    u, v, w = map(int, var[j].split())
    graph[u].append((v, w))

source = 1
destination = nodes

paths = findPath(source, graph, nodes)

if destination in paths:
    min_danger_level = paths[destination]
else:
    min_danger_level = "Impossible"

outputfile = open("output3.txt", "w")
outputfile.write(str(min_danger_level))
outputfile.close()