def get_number_of_islands(binaryMatrix):
  if len(binaryMatrix) == 0:
    return 0
  length = len(binaryMatrix)
  height = len(binaryMatrix[0])
  if length == 0 or height == 0:
    return 0
  num = 0
  visited = set()
  """
  visitied = [[False] * height for _ range(length)]
  """
  for i in range(length):
    for j in range(height):
      if binaryMatrix[i][j] == 1 and (i,j) not in visited:
        num += 1
        curr_position = (i,j)
        helper(visited,binaryMatrix,curr_position,length,height)
  return num

def helper(visited,binaryMatrix,curr_position,length,height):
  if curr_position in visited:
    return
  visited.add(curr_position)
  for x1, y1 in [(0,1),(1,0),(-1,0),(0,-1)]:
    x, y = curr_position# (0,1) => x = 0, y = 1
    new_x, new_y = x + x1, y + y1
    if 0 <= new_x < length and 0 <= new_y < height:
      new_position = binaryMatrix[new_x][new_y]
      if new_position == 1:
        helper(visited,binaryMatrix,(new_x,new_y),length,height)
