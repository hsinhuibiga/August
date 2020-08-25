#Minimum Cost For Tickets

class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [float("inf")] * 366
        for day in days:
            dp[day] = 0
        dp[0] = 0
        for i in range(1, 366):
            if dp[i] == float("inf"):
                dp[i] = dp[i - 1]
            else:
                cur = dp[i - 1] + costs[0]
                cur = min(dp[max(0, i - 7)] + costs[1], cur)
                cur = min(dp[max(0, i - 30)] + costs[2], cur)
                dp[i] = cur
        return dp[days[-1]]