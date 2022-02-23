class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_of_numbers_so_far = set()
        dp_arr = []
        for i in nums:
  #keep adding on
