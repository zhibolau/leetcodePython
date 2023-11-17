class Solution:
    """
    @param str: s string
    @return: return an integer, denote the number of the palindromic substrings
    """
    def countPalindromicSubstrings(self, s):
        # write your code here
        cnt = 0
        for i in range(len(s)):
            l=0
            while i-l >= 0 and i+l <= len(s)-1 and s[i-l] == s[i+l]:
                l+=1
                cnt+=1
            
            l=0
            while i-l >= 0 and i+l+1 <= len(s)-1 and s[i-l] == s[i+l+1]:
                l+=1
                cnt+=1
        return cnt