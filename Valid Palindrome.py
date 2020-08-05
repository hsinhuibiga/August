#Valid Palindrome

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleanlist = [c for c in s.lower() if c.isalnum()]
        return cleanlist == cleanlist[::-1]