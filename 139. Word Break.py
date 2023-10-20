class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(s) == 0:
            return True      
        memo = [None] * len(s)
        return self.dfs(0, s, wordDict, memo)
    
    def dfs(self, start, s, wordDict, memo):
        if start == len(s):
            return True 
        if memo[start] != None:
            return memo[start]
        for j in range(start, len(s)):
            if s[start: j + 1] in wordDict and self.dfs(j + 1, s, wordDict, memo):
                memo[start] = True 
                return True            
        memo[start] = False                
        return False