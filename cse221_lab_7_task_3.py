

#Task-3
def count_ways_to_climb_stairs(N, memo):
  if N <= 1:
    return 1

  if memo[N] != -1:
    return memo[N]

  memo[N] = count_ways_to_climb_stairs(N - 1, memo) + count_ways_to_climb_stairs(N - 2, memo)

  return memo[N]

def count_ways(N):
  memo = [-1] * (N + 1)

  return count_ways_to_climb_stairs(N, memo)

inputfile=open("input3.txt","r")
outputfile=open("output3.txt","w")
N = inputfile.readlines()

outputfile.write(str(count_ways(int(N.pop()))))
outputfile.close()