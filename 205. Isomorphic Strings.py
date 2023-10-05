class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        
        return self.bi_iso(s,t) and self.bi_iso(t,s)
    
    def bi_iso(self,s,t):
        d = {}
        for i in range(len(s)):
            if s[i] not in d:# 格式是一样的 只是字母不同  所以s中的可以匹配到t
                d[s[i]] = t[i]
            elif d[s[i]] != t[i]:
                return False
        return True
            