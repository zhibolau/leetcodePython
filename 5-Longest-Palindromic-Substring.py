class Solution:

    #方法1：O(n^3)  暴力
#从最长的子串（它本身）开始判断是否是回文，如果是则return，
#然后在判断长度减1的子串是否是回文。比如“babad”，先判断子串长度为5的所有子串是否是回文，
#如果是return，否则继续判断子串长度为4的所有子串是否是回文，
#如果某个子串是回文，则return
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        while length > 0:
            for i in range(len(s)):
                l,r = i, i+length
                if r<=len(s):
                    if self.isPalindrome(s[l:r]):
                        return s[l:r]
                else:
                    break
            length -=1
    def isPalindrome(self,s):
        i,j = 0, len(s)-1
        while i <= j:
            if s[i] == s[j]:
                i +=1
                j -= 1
            else:
                break
        if i>j:
            return True
        return False


#O(n^2) 从中心向两边扩散
#如果s[left]==s[right]，left减一，right加1知道不相等或者超出边界范围，
#同时比较当前满足回文的子串的长度与当前最长子串的长度，如果更长，则更新最长子串的长度。

    def longestPalindrome(self, s: str) -> str:
        p = ''
        
        for i in range(len(s)):
            #"bab"
            len1 = len(self.get_longest_p(s,i,i))
            if len1>len(p):
                p = self.get_longest_p(s,i,i)
            #"bb"
            len2 = len(self.get_longest_p(s,i,i+1))
            if len2>len(p):
                p = self.get_longest_p(s,i,i+1)
        return p
    
    def get_longest_p(self, s, l, r):
        while l>= 0 and r<len(s) and s[l] == s[r]: #找到一样的字母 往两边扩
            l -= 1
            r+=1
        return s[l+1:r] #当前l是出现不一样的字母了，所以要选择上一个的l 所以+1