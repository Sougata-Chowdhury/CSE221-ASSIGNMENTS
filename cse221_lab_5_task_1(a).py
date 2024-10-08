#Task1a
def dfs(graph,start,visited,stack):

  if visited[start] == False:
    visited[start] = True
    stack.append(start)
    for connection in graph[start]:
      dfs(graph,connection,visited,stack)


inputfile = open("input1a.txt","r")
var= inputfile.read().split('\n')
v= open("output1a.txt","w")
temp = var[0].split(" ")
courses = int(temp[0])
preq = int(temp[1])
graph = {}
start = int(var[1][0])

for i in range(courses + 1):
  graph[i] = []
for k in range(1, len(var)):
  s_temp = var[k].split(" ")
  n1 = int(s_temp[0])
  n2 = int(s_temp[1])
  graph[n1].append(n2)

visited = [False]*(courses+1)
top_sort=[]
dfs(graph,start,visited,top_sort)

for j in range(1,len(visited)):
  if visited[j]==False:
    dfs(graph,j,visited,top_sort)

flag = False
for i in range(len(top_sort)):
  for elem in graph[top_sort[i]]:
    for iter in range(i):
      if top_sort[iter] == elem:
        flag = True
    for j in range(i + 1, len(top_sort)):
      if top_sort[j] == top_sort[i]:
        flag = True

if flag==False:
  for elem2 in top_sort:
    v.write(str(elem2)+" ")
else:
  v.write("Impossible")