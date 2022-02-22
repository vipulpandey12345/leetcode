
     def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return []
        left = [0] * len(nums)
        right = [0] * len(nums)
        product = 1
        for i in range(len(nums)):
            left[i]= product
            product *= nums[i]
        product = 1
        for i in reversed(range(len(nums))):
            right[i] = product
            product *= nums[i]
        arr = [0] * len(nums)
        for i in range(len(nums)):
            arr[i] = left[i] * right[i]
        return arr

