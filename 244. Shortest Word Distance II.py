class WordDistance(object):

    def __init__(self, wordsDict):
        """
        :type wordsDict: List[str]
        """
        from collections import defaultdict
        self.words = wordsDict
        self.record = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.record[word].append(i)
        # print self.record
    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res = len(self.words)
        for pos1 in self.record[word1]:
            for pos2 in self.record[word2]:
                res = min(res, abs(pos1 - pos2))
        return res
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)