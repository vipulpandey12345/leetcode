def square_root_of_num(n):
  if n == 0:
        return 0
  left, right = 1, n
  res = -1
  while left <= right:
      mid = (left + right) // 2
      if mid * mid <= n:
          res = mid
          left = mid + 1
      else:
          right = mid - 1
  return res

# the function works by checking whether the halfway point squared is less than or greater than the num
# if less than, update nums because we need a number that is rounded down to the nearest integer
# else, shift right boundary and return at the end of while loop
