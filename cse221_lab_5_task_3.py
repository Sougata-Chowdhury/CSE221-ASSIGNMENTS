

#Task 3
def dfs_for_stack(graph, start, visited, stack):
  if visited[start] == False:
    visited[start] = True
    stack.append(start)
    for connection in graph[start]:
      dfs_for_stack(graph, connection, visited, stack)

def edge_reverse(graph,courses):
  transpose={}
  for iter in range(courses + 1):
    transpose[iter] = []
  for k,v in graph.items():
    for elem in graph[k]:
      transpose[elem].append(k)
  return transpose

def dfs_for_scc(graph, start, visited, res):
  if visited[start] == False:
    visited[start] = True
    res.append(start)
    for connection in graph[start]:
      dfs_for_stack(graph, connection, visited, res)


inputfile=open("input3.txt","r")
var=inputfile.read().split('\n')
v=open("output3.txt","w")
temp=var[0].split(" ")
courses=int(temp[0])
preq=int(temp[1])
graph = {}
start=int(var[1][0])

visited1=[False]*(courses+1)
for i in range(courses + 1):
  graph[i] = []
for k in range(1, len(var)):
  s_temp = var[k].split(" ")
  n1 = int(s_temp[0])
  n2 = int(s_temp[1])
  graph[n1].append(n2)

stack=[]
dfs_for_stack(graph,start,visited1,stack)
for j in range(1,len(visited1)):
  if visited1[j]==False:
    dfs_for_stack(graph,j,visited1,stack)


ReversedGraph=edge_reverse(graph,courses)
visited2=[False]*(courses+1)
result=[]
scc=[]

while len(stack)!=0:
  start_new=stack.pop(0)
  dfs_for_scc(ReversedGraph,start_new,visited2,result)
  scc.append(result)
  result=[]
for elem in scc:
  if len(elem)!=0:
    for elem2 in elem:
      v.write(str(elem2)+" ")
    v.write("\n")