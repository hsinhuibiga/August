#H-Index

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        citations.sort()
        h = 0
        for i, c in enumerate(citations):
            h = max(h, min(N - i, c))
        return h