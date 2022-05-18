def searchMatrix(matrix, target):
  current_length = 0
  current_width = len(matrix[0]) - 1
  length = len(matrix)
  width = len(matrix[0])
  current_pointer = matrix[current_length][current_width]
  while 0 <= current_length <= length - 1 and 0 <= current_width <= width - 1:
    if current_pointer > target:
      current_width -= 1
      current_pointer = matrix[current_length][current_width]
    elif current_pointer < target:
      current_length += 1
      current_pointer = matrix[current_length][current_width]
    else:
      return True
  return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
target = 13
print(searchMatrix(matrix, target))
