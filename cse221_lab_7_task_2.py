

#Task2
inputfile = open("input2.txt", "r")
outputfile = open("output2.txt", "w")

def disjoint_set(n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    u = find(n1)
    v = find(n2)
    if u > v:
        for i in range(len(parent)):
            if parent[i] == u:
                parent[i] = v
    elif u < v:
        for i in range(len(parent)):
            if parent[i] == v:
                parent[i] = u

def find(r):
    if parent[r] == r:
        return r
    return find(parent[r])

input_data = inputfile.read().split("\n")
cities = int(input_data[0][0])
roads = int(input_data[0][2])
graph = []

for line in input_data[1:-1]:
    parts = line.split(" ")
    n1 = int(parts[0])
    n2 = int(parts[1])
    w = int(parts[2])
    graph.append((n1, n2, w))

parent = [None] * (cities + 1)
for i in range(cities + 1):
    parent[i] = i

def get_weight(edge):
    return edge[2]

sorted_edges = sorted(graph, key=get_weight)

minimal_cost = 0
for edge in sorted_edges:
    if parent[edge[0]] != parent[edge[1]]:
        disjoint_set(edge[0], edge[1])
        minimal_cost += edge[2]

outputfile.write(str(minimal_cost))
inputfile.close()
outputfile.close()