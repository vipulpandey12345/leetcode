#binary search problem using weights as the upper and lower bounds


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lowest = max(weights)
        highest = sum(weights)
        ans = 0
        while lowest < highest:
            middle = (lowest + highest) // 2
            if self.searchDays(weights, middle, days) == True:
                ans = middle
                highest = middle
            else:
                lowest = middle + 1
        return ans
        
    def searchDays(self,weights, weight, days):
        temp_days = 1
        capacity = weight
        i = 0
        while i <= len(weights) - 1:
            capacity -= weights[i]
            if capacity < 0:
                temp_days += 1
                capacity = weight
                capacity -= weights[i]
            i += 1
        return temp_days <= days
