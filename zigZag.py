def convert(s, numRows):
  lst = []
  for i in range(0,numRows):
    lst.append([])
  #outer while loop to hit all chars
  i = 0
  row = 0
  boolean = True
  while i < len(s):
    
    if row < numRows and boolean:
      lst[row].append(s[i])
      row += 1
      i += 1
    else:
      boolean = False
      if row == numRows:
        row = row - 1
      row = row - 1
      lst[row].append(s[i])
      
      if row == 0:
        boolean = True
        row = 1
      i += 1
  string = ''
  for innerlst in lst:
    for j in innerlst:
      string += j

  return string
