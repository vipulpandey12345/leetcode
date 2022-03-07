#greedy approach
#checks if the position plus the actual element can get you to the last good element


def jumpGame(arr):
  if len(arr) == 0:
    return True
  lastGood = len(arr) - 1
  i = len(arr) - 1
  while i != 0:
    if arr[i] + i >= lastGood:
      lastGood = i
    i -= 1
return lastGood == 0
