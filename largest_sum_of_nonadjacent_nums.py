'''
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

[5]

'''

def largest_sum_of_nonadjacent_nums(arr):
  if len(arr) == 0:
    return 0
  elif len(arr) == 1:
    return arr[0]
  dp = [0] * len(arr)
  for i in range(len(arr)):
    if i == 0 or i == 1:
      dp[i] = arr[i]
    else:
      dp[i] = max(dp[i-2] + dp[i], dp[i-1])
  print(dp)
  return dp[-1]
print(largest_sum_of_nonadjacent_nums([2, 4, 6, 2, 5]))
