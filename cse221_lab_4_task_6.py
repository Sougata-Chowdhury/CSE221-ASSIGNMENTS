
#task 6
def findDiamonds(grid, rows, columns):
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

  def bfs(grid, start):

    queue = []
    queue.append(start)
    diamonds_collected = 0
    visited = []

    while queue:
      row, col = queue.pop(0)
      if (row, col) in visited:
        continue
      visited.append((row, col))
      if grid[row][col] == 'D':
        diamonds_collected += 1
      for r, c in directions:
        new_row, new_col = row + r, col + c
        if 0 <= new_row < rows and 0 <= new_col < columns and grid[new_row][new_col] != '#':
          queue.append((new_row, new_col))

    return diamonds_collected

  max_diamonds = 0

  for i in range(rows):
    for j in range(columns):
      if grid[i][j] != '#':
        max_diamonds = max(max_diamonds, bfs(grid, (i, j)))

  return max_diamonds

inputfile = open("input6.txt","r")
outputfile = open("output6.txt","w")

elements = inputfile.readlines()
rows, columns = map(int, elements[0].split(" "))
grid = [elem for elem in elements[1:]]
result = findDiamonds(grid, rows, columns)

outputfile.write(str(result))
outputfile.close()