#Distribute Candies to People

class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        n = num_people
        res = [0] * n

        c = 0
        while candies > 0:
            res[c % n] += min(candies, c + 1)
            c += 1
            candies -= c

        return res