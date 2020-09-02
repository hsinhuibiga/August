#Pancake Sorting

class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res = list()
        for i in range(len(arr), 1, -1):
            idx = arr.index(i) + 1
            arr = arr[:idx][::-1] + arr[idx:]
            arr = arr[:i][::-1]
            res += [idx, i]

        return res