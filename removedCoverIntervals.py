class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 1:
            return 1
        ans = []
        intervals.sort(key = lambda i: i[0], -i[1])
        ans.append(interval[0])
        for i in range(1, len(intervals)):
            start, end = ans[-1][0], ans[-1][1]
            if intervals[i][0] <= start and end <= intervals[i][1]:
                ans.append(intervals[i])
        return len(ans)
