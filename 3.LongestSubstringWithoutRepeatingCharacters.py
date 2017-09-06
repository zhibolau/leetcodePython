class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        left = 0
        d = {}
        for i,ch in enumerate(s):
            if ch in d and d[ch]>=left:
                left = d[ch]+1
                res = max(res,i-left+1)
            d[ch]=i
            
        return len(s) if res == 0 else res    
