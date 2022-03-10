class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) == 2:
            return min(cost)
        dp = [0] * (len(cost) + 1)
        for i in range(len(dp)):
            if i == 0:
                dp[i] = 0
            elif i == 1:
                dp[i] = min(cost[i], cost[i-1])
            else:
                dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        return dp[-1]
