'''
[7,1,5,3,6,4]
min_val = 1
min_val = 1
max = max(max, prices[i] - min)
return max
'''




class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        maximum_price = 0
        i = 1
        while i < len(prices):
            if prices[i] <= min_val:
                min_val = prices[i]
            maximum_price = max(maximum_price, prices[i] - min_val)
            i += 1
        return maximum_price
