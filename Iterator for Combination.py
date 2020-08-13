#Iterator for Combination

class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        # from itertools import permututations
        self.s = list(itertools.combinations(characters, combinationLength))
        self.index = 0

    def next(self):
        """
        :rtype: str
        """
        self.index += 1
        return "".join(self.s[self.index - 1])

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < len(self.s)