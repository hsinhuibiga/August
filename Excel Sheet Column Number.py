#Excel Sheet Column Number

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        count = 0
        for i in s[::-1]:
            result += 26**count*(ord(i)-ord('A')+1)
            count += 1
        return result