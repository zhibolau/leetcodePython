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
        
        for i in range(min(n, m)):
          if s[i] != t[i]: 
            if m == n: 
              return s[i + 1:] == t[i + 1:]
            if n == m + 1: 
              return s[i + 1:] == t[i:]
            else: 
              return s[i:] == t[i + 1:]
        return n != m 