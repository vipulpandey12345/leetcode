class Solution:
    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1,-1]
        one = self.first_occurence(nums, target)
        two = self.last_occurence(nums, target)
        return [one,two]
    
    def first_occurence(nums,target):
        ans = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) / 2
            if nums[middle] == target:
                ans = middle
                right = middle - 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return ans
        
    def last_occurence(nums, target):
        ans = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) / 2
            if nums[middle] == target:
                ans = middle
                left = middle + 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return ans
nums = [1,2,3,4,5,6] # Array of numbers
target = 7 # Target
s = Solution()
print(s.searchRange(nums,target))
