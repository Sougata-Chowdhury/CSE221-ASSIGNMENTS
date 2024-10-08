

#Task 1
inputfile=open("input1.txt","r")
outputfile=open("output1.txt",'w')
var=inputfile.read().split("\n")
people=int(var[0].split(" ")[0])
queries=int(var[0].split(" ")[1])
parent=[None]*(people+1)
for i in range(people+1):
	parent[i]=i

def find(r):
	if parent[r]==r:
		return r
	return find(parent[r])

for j in range(1,queries+1):
	number1,number2=var[j].split(" ")
	number1=int(number1)
	number2=int(number2)
	u = find(number1)
	v = find(number2)
	if u>v:
		for i2 in range(len(parent)):
			if parent[i2]==u:
				parent[i2]=v
		count=0
		for elem in parent:
			if elem==v:
				count+=1
	elif u<v:
		count = 0
		for i2 in range(len(parent)):
			if parent[i2]==v:
				parent[i2]=u
		count=0
		for elem in parent:
			if elem==u:
				count+=1
	elif u==v:
		count=0
		for elem in parent:
			if elem == parent[number1]:
				count += 1
	outputfile.write(str(count)+"\n")
outputfile.close()