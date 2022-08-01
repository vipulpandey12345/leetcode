def rechargeBatteries(capacity, recharge, t):
  if t == 0:
    return 0
  queue = []
  i = 0
  currentTime = 0
  num = 0
  while i != len(capacity):
    queue.append((capacity[i], 0, recharge[i]))
    i += 1
  
  
  while queue:
    currentTuple = queue.popleft()
    if currentTuple[1] <= currentTime:
      currentTime += currentTuple[0]
      num += 1
      queue.append((currentTuple[0], currentTuple[2] + currentTime, currentTuple[2]))
      if currentTime > t:
        return num
    else:
      queue.append(currentTuple)
  return num

