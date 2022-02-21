def spiral_copy(inputMatrix):
  stop_up = 0
  stop_left = 0
  stop_right = len(inputMatrix[0]) -1
  stop_down = len(inputMatrix) -1
  counter = 0
  output = []
  while len(output) <= len(inputMatrix) * len(inputMatrix[0]):
    if counter % 4 == 0: # process elements going to the right
      for i in range(stop_left,stop_right):
        output.append(inputMatrix[stop_up][i])
        stop_up += 1
        counter += 1
    if counter % 4 == 1: # process elements going down
      for i in range(stop_up,stop_down):
        output.append(inputMatrix[i][stop_right])
        stop_right -= 1
        counter += 1
    if counter % 4 == 2: # process elements going left
      for i in range(stop_right,stop_left):
        output.append(inputMatrix[stop_down][i])
        stop_down -= 1
        counter += 1
    if counter % 4 == 3: # process elements going up
      for i in range(stop_down,stop_up):
        output.append(inputMatrix[i][stop_left])
        stop_left += 1
        counter += 1
  return output

