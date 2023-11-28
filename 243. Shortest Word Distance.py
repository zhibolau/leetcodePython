class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """

        size=len(wordsDict)
        ans=idx1=idx2=size

        for i,j in enumerate(wordsDict):
            if j ==word1:
                idx1=i
                ans=min(ans,abs(idx1-idx2))

            elif j==word2:
                idx2=i
                ans=min(ans,abs(idx1-idx2))

        return ans
        