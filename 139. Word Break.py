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
    
    """定义dfs
    递归的出口
    如果起始点已经在字符串的尾部
        停止，返回可以组成该字符串
    如果还未到结尾，枚举下一个字符串。
        对于每种可能，判断该字符串是否是原字符串的前缀
        如果是前缀：
            取出该字符串，判断剩下的是否可以
    找完所有可能后，仍然不行，直接返回这段字符串无法找到答案"""