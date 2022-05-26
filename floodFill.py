def flood_fill(matrix, sr, sc, newNum):
  originalNum = matrix[sr][sc]
  length = len(matrix)
  height = len(matrix[0])
  visited = set()
  helper(visited,matrix,sr,sc,length,height,newNum,originalNum)
  return matrix

def helper(visited,matrix,sr,sc,length,height,newNum, originalNum):
  current_position = (sr,sc)
  if current_position in visited:
    return
  visited.add(current_position)
  for x1, y1 in [(0,1),(1,0),(-1,0),(0,-1)]:
    x, y = current_position# (0,1) => x = 0, y = 1
    new_x, new_y = x + x1, y + y1
    if 0 <= new_x < length and 0 <= new_y < height:
      new_position = matrix[new_x][new_y]
      if new_position == originalNum:
        new_position = newNum
        helper(visited,matrix,new_x,new_y,length,height,newNum, originalNum)
