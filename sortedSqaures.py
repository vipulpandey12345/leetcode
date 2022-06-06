def sortedSquares(nums):
  finArr = []
  l = len(nums)//2
  r = len(nums)//2 + 1

  while l < r and (l>-1 or r < len(nums)):
    if nums[l]*-1 <= nums[r] or r>len(nums):
      finArr.append(nums[l]**2)
      l-=1
    #when right value less than left
    if nums[l]*-1 > nums[r] or l < 0:
      finArr.append(nums[r]**2)
      r+=1

  return finArr
    
      
nums = [-4,-1,0,3,10]
print(sortedSquares(nums))
    
