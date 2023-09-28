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
                left = d[ch]+1 #出现重复了  挪动左pointer
            d[ch]=i #记录当前值的index
            res = max(res,i-left+1)
        return res    
