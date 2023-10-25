class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def isOneEditDistance(self, s, t):
        # write your code here
        n, m = len(s), len(t) 
        if abs(n - m) > 1: 
          return False 
        
        for i in range(min(n, m)): #idx要按小的走
          if s[i] != t[i]: 
            if m == n: # ab cb
              return s[i + 1:] == t[i + 1:]
            if n == m + 1:  # abc bc
              return s[i + 1:] == t[i:]
            else:  #ab cab
              return s[i:] == t[i + 1:]
        return n != m  # 都是c 不行  没有操作，所以得长度不等