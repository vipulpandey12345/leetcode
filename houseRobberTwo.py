class Solution(object):
    def rob(self, arr):
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return arr[0]
        dp = [0] * len(arr)
        val_one = 0
        val_two = 0
        for i in range(len(arr)-1):
            if i == 0:
                dp[i] = arr[i]
            elif i == 1:
                dp[i] = max(dp[i-1], arr[i])
            else:
                dp[i] = max(dp[i-2] + arr[i], dp[i-1])
        val_one = max(dp)
        dp = [0] * len(arr)
        for i in range(1,len(arr)):
            if i == 0:
                dp[i] = arr[i]
            elif i == 1:
                dp[i] = max(dp[i-1], arr[i])
            else:
                dp[i] = max(dp[i-2] + arr[i], dp[i-1])
        val_two = max(dp)
        
        return max(val_one, val_two)
        
