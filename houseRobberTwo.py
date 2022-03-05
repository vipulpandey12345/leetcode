class Solution(object):
    def rob(self, arr):
        if len(arr) == 0:
            return 0
        dp = [0] * len(arr)
        for i in range(len(arr)):
            if i == 0:
                dp[i] = arr[i]
            elif i == 1:
                dp[i] = max(dp[i-1], arr[i])
            elif i == len(arr) - 1:
                dp[i] = dp[i-1]
            else:
                dp[i] = max(dp[i-2] + arr[i], dp[i-1])
        return max(dp)
        
