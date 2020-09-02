#Find Right Interval

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        intervals = sorted((e[0], i, e[1]) for i, e in enumerate(intervals))
        l = len(intervals)
        res = [0] * l
        for e in intervals:
            r = bisect.bisect_left(intervals, (e[2], ))
            res[e[1]] = intervals[r][1] if r < l else -1
        return res