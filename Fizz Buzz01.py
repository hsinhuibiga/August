#Fizz Buzz

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1, n + 1):
            pos = ""
            if i % 3 == 0:
                pos += "Fizz"
            if i % 5 == 0:
                pos += "Buzz"
            if not pos:
                pos = str(i)
            res.append(pos)
        return res