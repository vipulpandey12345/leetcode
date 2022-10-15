class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = collections.defaultdict(int)
        counter = 0
        for i in time:
            if not (i % 60):
                counter += remainders[0]
            else:
                counter += remainders[60 - (i % 60)]
            remainders[i % 60] += 1
        return counter  
