#Longest Palindrome

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        res = 0
        prime = 0
        for k, v in count.items():
            if v % 2 == 1:
                res += v - 1
                prime = 1
            else:
                res += v
        return res + prime