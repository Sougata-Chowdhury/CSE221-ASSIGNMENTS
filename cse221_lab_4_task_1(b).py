
#Task 1b
def graphRep(data):
  vertices = int(data[0].split(" ")[0])
  edge = int(data[0].split(" ")[1])
  ad_list = [[] for i in range(vertices + 1)]
  for i in range(1, edge + 1):
    n = int(data[i].split(" ")[1])
    weight = int(data[i].split(" ")[2])
    ad_list[int(data[i][0])].append((n,weight))

  return ad_list

inputfile = open("input1b.txt","r")
outputfile = open("output1b.txt","w")

l = inputfile.readlines()
ad_list = graphRep(l)
for i in range(len(ad_list)):
  elem = list(map(str,ad_list[i]))
  outputfile.write(f"{str(i)} :" + " ".join(elem) + "\n")

outputfile.close()