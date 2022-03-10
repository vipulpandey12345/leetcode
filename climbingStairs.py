class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        for i in range(len(dp)):
            if i == 0:
                dp[i] = 0
            elif i == 1:
                dp[i] = 1
            elif i == 2:
                dp[i] = 2
            else:
                dp[i] =  dp[i-1] + dp[i-2]
        print(dp)
        return dp[-1]
